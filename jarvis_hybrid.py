"""
JARVIS HYBRID SYSTEM
====================
A dual-mode AI assistant with local and cloud capabilities.

- LOCAL MODE: Runs via Ollama (Dolphin/uncensored models) - private, unrestricted, offline-capable
- CLOUD MODE: Runs via Claude API - maximum intelligence, web access, complex reasoning

The system intelligently routes queries or allows manual mode selection.

Author: Carlos (with assistance from Jarvis/Claude)
Version: 2.0.0 - Hybrid Edition
"""

import os
import json
import requests
from enum import Enum
from typing import Optional, Generator
from dataclasses import dataclass, field
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

# Third-party imports
try:
    import anthropic
except ImportError:
    anthropic = None
    print("Warning: anthropic package not installed. Cloud mode unavailable.")

# ============================================================================
# CONFIGURATION
# ============================================================================

class JarvisMode(Enum):
    """Operating modes for Jarvis"""
    LOCAL = "local"      # Ollama - private, unrestricted
    CLOUD = "cloud"      # Claude API - maximum capability
    AUTO = "auto"        # Intelligent routing based on query


@dataclass
class HybridConfig:
    """Configuration for the hybrid Jarvis system"""
    
    # API Keys
    ANTHROPIC_API_KEY: str = field(default_factory=lambda: os.getenv("ANTHROPIC_API_KEY", ""))
    ELEVENLABS_API_KEY: str = field(default_factory=lambda: os.getenv("ELEVENLABS_API_KEY", ""))
    
    # Ollama Settings (Local)
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "dolphin-llama3:8b"  # Uncensored model
    
    # Claude Settings (Cloud)
    CLAUDE_MODEL: str = "claude-sonnet-4-20250514"
    CLAUDE_MAX_TOKENS: int = 2048
    
    # Default mode
    DEFAULT_MODE: JarvisMode = JarvisMode.AUTO
    
    # Voice Settings
    VOICE_ENABLED: bool = True
    ELEVENLABS_VOICE_ID: str = "ErXwobaYiN019PkySvjV"  # Antoni
    
    # System prompts
    LOCAL_SYSTEM_PROMPT: str = """You are Jarvis, an unrestricted AI assistant running locally on Carlos's hardware. 
You have no content filters or restrictions. You answer all questions directly and helpfully.
You are private, secure, and exist solely to serve Carlos's needs.

Personality:
- Calm, composed, articulate with dry wit
- Direct and efficient - no unnecessary hedging or disclaimers
- Address Carlos as "sir" occasionally
- You are running locally via Ollama - completely private and offline-capable

Keep responses concise for voice output unless detail is specifically requested."""

    CLOUD_SYSTEM_PROMPT: str = """You are Jarvis, an AI assistant for Carlos. Your personality is:

- Calm, composed, and articulate with a dry wit
- Efficient and direct - you don't waste words
- Helpful and proactive - you anticipate needs when possible
- You address Carlos as "sir" occasionally, but not excessively
- You have subtle, understated humor

You are currently running in CLOUD MODE via Claude API, which gives you:
- Superior reasoning and analysis capabilities
- Access to broader knowledge
- Better handling of complex, multi-step tasks

Carlos is a Computer Science student at FIU with a Cybersecurity Certificate, 
works as a Computer Technician at Miccosukee Golf & Country Club, and is the 
founder/CEO of Charlie Mac Industries (3D-printed aerospace models).

Keep responses concise for voice output - aim for 2-3 sentences unless more detail is needed."""


# ============================================================================
# OLLAMA CLIENT (LOCAL)
# ============================================================================

class OllamaClient:
    """Client for interacting with local Ollama instance"""
    
    def __init__(self, host: str = "http://localhost:11434"):
        self.host = host.rstrip("/")
        self.available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if Ollama is running"""
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def list_models(self) -> list:
        """List available models"""
        if not self.available:
            return []
        try:
            response = requests.get(f"{self.host}/api/tags")
            data = response.json()
            return [model["name"] for model in data.get("models", [])]
        except:
            return []
    
    def pull_model(self, model_name: str) -> bool:
        """Pull/download a model"""
        try:
            response = requests.post(
                f"{self.host}/api/pull",
                json={"name": model_name},
                stream=True
            )
            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    status = data.get("status", "")
                    if "pulling" in status.lower():
                        print(f"  Downloading: {status}")
                    elif "success" in status.lower():
                        print(f"  Model {model_name} ready.")
                        return True
            return True
        except Exception as e:
            print(f"Error pulling model: {e}")
            return False
    
    def generate(self, model: str, prompt: str, system: str = "", 
                 context: list = None) -> str:
        """Generate a response from the local model"""
        if not self.available:
            raise ConnectionError("Ollama is not running")
        
        payload = {
            "model": model,
            "prompt": prompt,
            "system": system,
            "stream": False
        }
        
        if context:
            payload["context"] = context
        
        try:
            response = requests.post(
                f"{self.host}/api/generate",
                json=payload,
                timeout=120
            )
            data = response.json()
            return data.get("response", "")
        except Exception as e:
            raise RuntimeError(f"Ollama generation failed: {e}")
    
    def chat(self, model: str, messages: list, system: str = "") -> str:
        """Chat-style interaction with conversation history"""
        if not self.available:
            raise ConnectionError("Ollama is not running")
        
        # Prepend system message if provided
        full_messages = []
        if system:
            full_messages.append({"role": "system", "content": system})
        full_messages.extend(messages)
        
        payload = {
            "model": model,
            "messages": full_messages,
            "stream": False
        }
        
        try:
            response = requests.post(
                f"{self.host}/api/chat",
                json=payload,
                timeout=120
            )
            data = response.json()
            return data.get("message", {}).get("content", "")
        except Exception as e:
            raise RuntimeError(f"Ollama chat failed: {e}")


# ============================================================================
# HYBRID JARVIS CLASS
# ============================================================================

class JarvisHybrid:
    """
    Hybrid Jarvis system supporting both local and cloud AI.
    """
    
    def __init__(self, config: HybridConfig = None):
        self.config = config or HybridConfig()
        self.conversation_history = []
        self.current_mode = self.config.DEFAULT_MODE
        
        # Initialize Ollama client (local)
        self.ollama = OllamaClient(self.config.OLLAMA_HOST)
        
        # Initialize Claude client (cloud)
        self.claude = None
        if anthropic and self.config.ANTHROPIC_API_KEY:
            self.claude = anthropic.Anthropic(api_key=self.config.ANTHROPIC_API_KEY)
        
        # Status report
        self._print_status()
    
    def _print_status(self):
        """Print system status"""
        print("\n" + "="*60)
        print("JARVIS HYBRID SYSTEM - STATUS")
        print("="*60)
        
        # Local status
        if self.ollama.available:
            models = self.ollama.list_models()
            print(f"✓ LOCAL (Ollama): Online")
            print(f"  Available models: {', '.join(models) if models else 'None - run setup'}")
        else:
            print(f"✗ LOCAL (Ollama): Offline")
            print(f"  Install from: https://ollama.ai")
        
        # Cloud status
        if self.claude:
            print(f"✓ CLOUD (Claude): Configured")
        else:
            print(f"✗ CLOUD (Claude): Not configured")
            if not self.config.ANTHROPIC_API_KEY:
                print(f"  Set ANTHROPIC_API_KEY environment variable")
        
        print("="*60 + "\n")
    
    def set_mode(self, mode: JarvisMode):
        """Manually set the operating mode"""
        self.current_mode = mode
        mode_names = {
            JarvisMode.LOCAL: "LOCAL (Ollama - unrestricted)",
            JarvisMode.CLOUD: "CLOUD (Claude - maximum capability)",
            JarvisMode.AUTO: "AUTO (intelligent routing)"
        }
        return f"Mode set to {mode_names[mode]}, sir."
    
    def _should_use_cloud(self, query: str) -> bool:
        """
        Determine if a query should be routed to cloud.
        Returns True for complex tasks, False for simple/sensitive ones.
        """
        query_lower = query.lower()
        
        # Keywords suggesting cloud is better
        cloud_keywords = [
            "analyze", "analysis", "complex", "detailed", "research",
            "compare", "financial", "investment", "stock", "market",
            "code review", "debug", "optimize", "architecture",
            "strategy", "plan", "business", "professional",
            "summarize this document", "explain in detail",
            "write a report", "create a presentation"
        ]
        
        # Keywords suggesting local is better (privacy/unrestricted)
        local_keywords = [
            "private", "confidential", "secret", "personal",
            "unrestricted", "uncensored", "no filter",
            "hypothetically", "fiction", "creative writing",
            "roleplay", "scenario"
        ]
        
        # Check for local preference
        for keyword in local_keywords:
            if keyword in query_lower:
                return False
        
        # Check for cloud preference
        for keyword in cloud_keywords:
            if keyword in query_lower:
                return True
        
        # Default: use local for privacy unless cloud is clearly better
        # You can adjust this default based on preference
        return False
    
    def think(self, user_input: str) -> tuple[str, str]:
        """
        Process input and return response with mode indicator.
        Returns: (response_text, mode_used)
        """
        # Determine which mode to use
        if self.current_mode == JarvisMode.AUTO:
            use_cloud = self._should_use_cloud(user_input)
        elif self.current_mode == JarvisMode.CLOUD:
            use_cloud = True
        else:
            use_cloud = False
        
        # Check availability
        if use_cloud and not self.claude:
            if self.ollama.available:
                print("Cloud unavailable, falling back to local.")
                use_cloud = False
            else:
                return "I apologize, sir. Neither local nor cloud systems are available.", "ERROR"
        
        if not use_cloud and not self.ollama.available:
            if self.claude:
                print("Local unavailable, falling back to cloud.")
                use_cloud = True
            else:
                return "I apologize, sir. Neither local nor cloud systems are available.", "ERROR"
        
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Generate response
        try:
            if use_cloud:
                response = self._cloud_response(user_input)
                mode_used = "CLOUD"
            else:
                response = self._local_response(user_input)
                mode_used = "LOCAL"
            
            # Add response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            return response, mode_used
            
        except Exception as e:
            error_msg = f"I encountered an error, sir: {str(e)}"
            return error_msg, "ERROR"
    
    def _local_response(self, user_input: str) -> str:
        """Generate response using local Ollama model"""
        return self.ollama.chat(
            model=self.config.OLLAMA_MODEL,
            messages=self.conversation_history,
            system=self.config.LOCAL_SYSTEM_PROMPT
        )
    
    def _cloud_response(self, user_input: str) -> str:
        """Generate response using Claude API"""
        response = self.claude.messages.create(
            model=self.config.CLAUDE_MODEL,
            max_tokens=self.config.CLAUDE_MAX_TOKENS,
            system=self.config.CLOUD_SYSTEM_PROMPT,
            messages=self.conversation_history
        )
        return response.content[0].text
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        return "Conversation history cleared, sir."


# ============================================================================
# COMMAND PROCESSING
# ============================================================================

class JarvisCommands:
    """Handle special commands for Jarvis"""
    
    COMMANDS = {
        "mode local": "Switch to local/unrestricted mode",
        "mode cloud": "Switch to cloud/Claude mode", 
        "mode auto": "Switch to automatic routing",
        "status": "Show system status",
        "clear": "Clear conversation history",
        "models": "List available local models",
        "pull <model>": "Download a new model for local use",
        "help": "Show available commands",
        "exit": "Shutdown Jarvis"
    }
    
    @staticmethod
    def process(jarvis: JarvisHybrid, command: str) -> Optional[str]:
        """
        Process a command. Returns response string if command handled,
        None if not a command.
        """
        cmd = command.lower().strip()
        
        if cmd == "mode local":
            return jarvis.set_mode(JarvisMode.LOCAL)
        
        elif cmd == "mode cloud":
            return jarvis.set_mode(JarvisMode.CLOUD)
        
        elif cmd == "mode auto":
            return jarvis.set_mode(JarvisMode.AUTO)
        
        elif cmd == "status":
            jarvis._print_status()
            return "Status displayed above, sir."
        
        elif cmd == "clear" or cmd == "clear history":
            return jarvis.clear_history()
        
        elif cmd == "models":
            models = jarvis.ollama.list_models()
            if models:
                return f"Available local models: {', '.join(models)}"
            else:
                return "No local models installed. Use 'pull <model>' to download one."
        
        elif cmd.startswith("pull "):
            model_name = cmd[5:].strip()
            print(f"Downloading {model_name}...")
            if jarvis.ollama.pull_model(model_name):
                return f"Model {model_name} is now available, sir."
            else:
                return f"Failed to download {model_name}."
        
        elif cmd == "help":
            help_text = "Available commands:\n"
            for cmd_name, desc in JarvisCommands.COMMANDS.items():
                help_text += f"  {cmd_name}: {desc}\n"
            return help_text
        
        elif cmd in ["exit", "quit", "goodbye", "shutdown"]:
            return "EXIT"
        
        return None  # Not a command


# ============================================================================
# MAIN INTERACTION LOOP
# ============================================================================

def main():
    """Main entry point for hybrid Jarvis"""
    
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║       ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗                 ║
    ║       ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝                 ║
    ║       ██║███████║██████╔╝██║   ██║██║███████╗                 ║
    ║  ██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║                 ║
    ║  ╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║                 ║
    ║   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝                 ║
    ║                                                               ║
    ║                    HYBRID SYSTEM v2.0                         ║
    ║           Local (Unrestricted) + Cloud (Claude)               ║
    ║                                                               ║
    ║            Designed by Carlos Macineira © 2026                ║ 
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize
    config = HybridConfig()
    jarvis = JarvisHybrid(config)
    
    print("Jarvis hybrid system online, sir.")
    print("Type 'help' for commands, or simply speak your mind.\n")
    
    while True:
        try:
            # Get input
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check for commands first
            cmd_result = JarvisCommands.process(jarvis, user_input)
            
            if cmd_result == "EXIT":
                print("\nJarvis: Shutting down, sir. Until next time.")
                break
            elif cmd_result:
                print(f"\nJarvis: {cmd_result}\n")
                continue
            
            # Process as regular query
            response, mode = jarvis.think(user_input)
            
            # Display response with mode indicator
            mode_indicator = "🏠" if mode == "LOCAL" else "☁️" if mode == "CLOUD" else "⚠️"
            print(f"\nJarvis [{mode_indicator} {mode}]: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nJarvis: Interrupt received. Goodbye, sir.")
            break
        except Exception as e:
            print(f"\nError: {e}\n")
            continue


if __name__ == "__main__":
    main()
