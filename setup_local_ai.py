"""
JARVIS LOCAL SETUP GUIDE
=========================
Instructions for setting up the local/unrestricted AI component.

This script helps you install and configure Ollama with uncensored models.
"""

import os
import sys
import subprocess
import requests
import platform

# ============================================================================
# RECOMMENDED MODELS
# ============================================================================

RECOMMENDED_MODELS = {
    # Best overall uncensored models
    "dolphin-llama3:8b": {
        "description": "Best all-around uncensored model. No guardrails.",
        "vram_required": "6-8 GB",
        "quality": "★★★★★",
        "speed": "★★★★☆",
        "recommended_for": "General use, everyday assistant"
    },
    "dolphin-mixtral:8x7b": {
        "description": "Excellent for coding and complex tasks. Uncensored.",
        "vram_required": "12-16 GB", 
        "quality": "★★★★★",
        "speed": "★★★☆☆",
        "recommended_for": "Programming, technical work"
    },
    "wizard-vicuna-uncensored:13b": {
        "description": "Solid uncensored model, good for creative work.",
        "vram_required": "10-12 GB",
        "quality": "★★★★☆",
        "speed": "★★★☆☆",
        "recommended_for": "Creative writing, roleplay"
    },
    "llama2-uncensored:7b": {
        "description": "Classic uncensored model. Reliable and tested.",
        "vram_required": "6-8 GB",
        "quality": "★★★★☆",
        "speed": "★★★★☆",
        "recommended_for": "General use, lower VRAM systems"
    },
    "nous-hermes2:10.7b": {
        "description": "Very capable, minimal restrictions.",
        "vram_required": "8-10 GB",
        "quality": "★★★★★",
        "speed": "★★★☆☆",
        "recommended_for": "Research, analysis"
    },
    
    # Smaller models for limited hardware
    "phi3:mini": {
        "description": "Microsoft's small but capable model.",
        "vram_required": "4-6 GB",
        "quality": "★★★☆☆",
        "speed": "★★★★★",
        "recommended_for": "Low VRAM systems, basic tasks"
    },
    "tinyllama:1.1b": {
        "description": "Tiny model for very limited hardware.",
        "vram_required": "2-3 GB",
        "quality": "★★☆☆☆",
        "speed": "★★★★★",
        "recommended_for": "Testing, very limited hardware"
    },
    
    # Large models for powerful hardware
    "dolphin-llama3:70b": {
        "description": "Maximum capability uncensored model.",
        "vram_required": "40-48 GB",
        "quality": "★★★★★+",
        "speed": "★★☆☆☆",
        "recommended_for": "High-end systems, complex reasoning"
    }
}


# ============================================================================
# SYSTEM CHECKS
# ============================================================================

def check_ollama_installed() -> bool:
    """Check if Ollama is installed"""
    try:
        result = subprocess.run(["ollama", "--version"], 
                               capture_output=True, text=True, timeout=5)
        return result.returncode == 0
    except:
        return False


def check_ollama_running() -> bool:
    """Check if Ollama server is running"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        return response.status_code == 200
    except:
        return False


def get_installed_models() -> list:
    """Get list of installed models"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        data = response.json()
        return [m["name"] for m in data.get("models", [])]
    except:
        return []


def check_gpu_info():
    """Attempt to detect GPU information"""
    gpu_info = {
        "detected": False,
        "name": "Unknown",
        "vram": "Unknown"
    }
    
    # Try nvidia-smi for NVIDIA GPUs
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            parts = result.stdout.strip().split(", ")
            gpu_info["detected"] = True
            gpu_info["name"] = parts[0] if parts else "NVIDIA GPU"
            gpu_info["vram"] = parts[1] if len(parts) > 1 else "Unknown"
    except:
        pass
    
    return gpu_info


# ============================================================================
# INSTALLATION HELPERS
# ============================================================================

def install_ollama_windows():
    """Instructions for installing Ollama on Windows"""
    print("""
╔════════════════════════════════════════════════════════════════════╗
║                    OLLAMA INSTALLATION - WINDOWS                    ║
╚════════════════════════════════════════════════════════════════════╝

1. Download Ollama from: https://ollama.ai/download

2. Run the installer (OllamaSetup.exe)

3. After installation, Ollama runs automatically in the background

4. Verify installation by opening Command Prompt and typing:
   ollama --version

5. Return here and run this script again to continue setup.

""")


def pull_model(model_name: str) -> bool:
    """Pull/download a model using Ollama"""
    print(f"\nDownloading {model_name}...")
    print("This may take several minutes depending on your connection.\n")
    
    try:
        # Use subprocess to show progress
        process = subprocess.Popen(
            ["ollama", "pull", model_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        for line in process.stdout:
            print(line, end="")
        
        process.wait()
        return process.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False


# ============================================================================
# INTERACTIVE SETUP
# ============================================================================

def recommend_model(vram_gb: int) -> str:
    """Recommend a model based on available VRAM"""
    if vram_gb >= 40:
        return "dolphin-llama3:70b"
    elif vram_gb >= 12:
        return "dolphin-mixtral:8x7b"
    elif vram_gb >= 8:
        return "dolphin-llama3:8b"
    elif vram_gb >= 6:
        return "llama2-uncensored:7b"
    elif vram_gb >= 4:
        return "phi3:mini"
    else:
        return "tinyllama:1.1b"


def interactive_setup():
    """Run interactive setup wizard"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║              JARVIS LOCAL AI SETUP WIZARD                         ║
║                                                                   ║
║    This wizard will help you set up the local/unrestricted        ║
║    AI component of your Jarvis system.                            ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    # Check Ollama installation
    print("Checking Ollama installation...")
    
    if not check_ollama_installed():
        print("\n❌ Ollama is not installed.")
        install_ollama_windows()
        input("Press Enter after installing Ollama...")
        
        if not check_ollama_installed():
            print("Ollama still not detected. Please install and try again.")
            return
    
    print("✓ Ollama is installed")
    
    # Check if Ollama is running
    if not check_ollama_running():
        print("\n⚠ Ollama server is not running.")
        print("Starting Ollama...")
        
        # Try to start Ollama
        if platform.system() == "Windows":
            subprocess.Popen(["ollama", "serve"], 
                           creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            subprocess.Popen(["ollama", "serve"], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
        
        import time
        time.sleep(3)
        
        if check_ollama_running():
            print("✓ Ollama server started")
        else:
            print("Could not start Ollama. Please start it manually.")
            return
    else:
        print("✓ Ollama server is running")
    
    # Check GPU
    print("\nDetecting GPU...")
    gpu_info = check_gpu_info()
    
    if gpu_info["detected"]:
        print(f"✓ GPU detected: {gpu_info['name']}")
        print(f"  VRAM: {gpu_info['vram']}")
    else:
        print("⚠ Could not detect GPU. You may be running on CPU only.")
    
    # Show installed models
    print("\nChecking installed models...")
    installed = get_installed_models()
    
    if installed:
        print(f"✓ Installed models: {', '.join(installed)}")
    else:
        print("  No models installed yet.")
    
    # Model selection
    print("\n" + "="*60)
    print("RECOMMENDED UNCENSORED MODELS")
    print("="*60)
    
    for name, info in RECOMMENDED_MODELS.items():
        installed_mark = "✓" if name in installed else " "
        print(f"\n[{installed_mark}] {name}")
        print(f"    {info['description']}")
        print(f"    VRAM: {info['vram_required']} | Quality: {info['quality']} | Speed: {info['speed']}")
        print(f"    Best for: {info['recommended_for']}")
    
    print("\n" + "="*60)
    
    # Ask user to select model
    print("\nWhich model would you like to install?")
    print("(Recommended for most users: dolphin-llama3:8b)")
    print("\nEnter model name, or press Enter for recommended: ", end="")
    
    choice = input().strip()
    
    if not choice:
        choice = "dolphin-llama3:8b"
    
    if choice in installed:
        print(f"\n{choice} is already installed!")
    else:
        print(f"\nPreparing to download {choice}...")
        confirm = input("Proceed? (y/n): ").strip().lower()
        
        if confirm == 'y':
            success = pull_model(choice)
            if success:
                print(f"\n✓ {choice} installed successfully!")
            else:
                print(f"\n❌ Failed to install {choice}")
    
    # Final instructions
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                         SETUP COMPLETE                             ║
╚═══════════════════════════════════════════════════════════════════╝

Your local AI is ready! To use it:

1. Make sure the model name in jarvis_hybrid.py matches your installed model:
   OLLAMA_MODEL = "{model}"

2. Run the hybrid Jarvis system:
   python jarvis_hybrid.py

3. Use 'mode local' to switch to unrestricted local mode
   Use 'mode cloud' to switch to Claude cloud mode
   Use 'mode auto' for intelligent routing

Commands in Jarvis:
   - 'models' - List installed models
   - 'pull <model>' - Download new model
   - 'status' - Show system status
   - 'help' - Show all commands

Enjoy your unrestricted AI assistant, sir.
""".format(model=choice))


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    interactive_setup()
