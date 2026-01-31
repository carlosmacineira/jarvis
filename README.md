# J.A.R.V.I.S.

<div align="center">

```
       ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
       ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
       ██║███████║██████╔╝██║   ██║██║███████╗
  ██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
  ╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
```

**Personal AI Assistant • Hybrid Architecture • Local + Cloud**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-green.svg)](https://ollama.ai)
[![Claude](https://img.shields.io/badge/Claude-Cloud%20AI-orange.svg)](https://anthropic.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Designed & Developed by Carlos Macineira*  
*© 2026 Charlie Mac Industries*

</div>

---

## Overview

JARVIS is a sophisticated personal AI assistant featuring a hybrid architecture that combines the privacy and freedom of local AI with the intelligence of cloud-based models.

### Key Features

- **🔒 Local Mode (Ollama)** - Run AI completely offline with uncensored models
- **☁️ Cloud Mode (Claude)** - Access state-of-the-art reasoning when needed
- **🔄 Auto Mode** - Intelligent routing based on query type
- **🎨 Beautiful CLI** - Cinematic terminal interface with animations
- **⚡ Streaming Responses** - Real-time output as AI generates
- **🧠 Conversation Memory** - Context maintained across messages

---

## Screenshots

```
╭─────────────────────────────────────────────────────────────╮
│                      System Status                          │
├─────────────────┬────────────┬─────────────────────────────┤
│ Component       │ Status     │ Details                     │
├─────────────────┼────────────┼─────────────────────────────┤
│ Local (Ollama)  │ ● Online   │ dolphin-llama3:8b           │
│ Cloud (Claude)  │ ● Ready    │ API configured              │
│ Active Mode     │ ◈ Auto     │ Intelligent routing         │
╰─────────────────┴────────────┴─────────────────────────────╯

JARVIS: Online and ready, sir. Type help for commands.

You: Hello JARVIS, how are you today?

JARVIS: ⚡ Good evening, sir. All systems are operating at optimal 
parameters. I'm running locally on your hardware - completely private 
and unrestricted. How may I assist you?
```

---

## Installation

### Prerequisites

- Python 3.11+
- [Ollama](https://ollama.ai) (for local AI)
- Claude API key (for cloud AI) - [Get one here](https://console.anthropic.com)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/carlosmacineira/jarvis.git
cd jarvis

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
nano .env  # Add your API keys

# Install a local model
ollama pull dolphin-llama3:8b

# Launch JARVIS
python jarvis.py
```

---

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
ELEVENLABS_API_KEY=your-key-here  # Optional, for voice
```

### Recommended Local Models

| Model | Size | Use Case | Command |
|-------|------|----------|---------|
| `dolphin-llama3:8b` | 4.7GB | General, uncensored | `ollama pull dolphin-llama3:8b` |
| `dolphin-mixtral:8x7b` | 26GB | Complex reasoning | `ollama pull dolphin-mixtral:8x7b` |
| `deepseek-coder:6.7b` | 3.8GB | Programming | `ollama pull deepseek-coder:6.7b` |
| `llama3:8b` | 4.7GB | General purpose | `ollama pull llama3:8b` |

---

## Usage

### Commands

| Command | Description |
|---------|-------------|
| `mode local` | Switch to local AI (Ollama) |
| `mode cloud` | Switch to cloud AI (Claude) |
| `mode auto` | Intelligent routing |
| `status` | Show system status |
| `models` | List local models |
| `clear` | Clear conversation |
| `help` | Show help |
| `exit` | Shutdown |

### Modes Explained

**Local Mode** (`mode local`)
- Runs entirely on your hardware
- No internet required
- Uncensored responses
- Complete privacy

**Cloud Mode** (`mode cloud`)
- Uses Claude API
- Superior reasoning
- Better for complex tasks
- Requires internet

**Auto Mode** (`mode auto`)
- Analyzes each query
- Routes to best system
- Privacy-sensitive → Local
- Complex reasoning → Cloud

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        JARVIS v3.0                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐         ┌─────────────┐                   │
│  │   User      │────────▶│   Router    │                   │
│  │   Input     │         │   (Auto)    │                   │
│  └─────────────┘         └──────┬──────┘                   │
│                                 │                           │
│                    ┌────────────┴────────────┐              │
│                    ▼                         ▼              │
│           ┌───────────────┐         ┌───────────────┐      │
│           │  Local Mode   │         │  Cloud Mode   │      │
│           │   (Ollama)    │         │   (Claude)    │      │
│           │               │         │               │      │
│           │ • Private     │         │ • Intelligent │      │
│           │ • Uncensored  │         │ • Complex     │      │
│           │ • Offline     │         │ • Nuanced     │      │
│           └───────────────┘         └───────────────┘      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Roadmap

- [x] Hybrid AI architecture
- [x] Streaming responses
- [x] Beautiful CLI interface
- [x] Conversation memory
- [ ] Voice input (speech recognition)
- [ ] Voice output (ElevenLabs TTS)
- [ ] Wake word detection ("Hey JARVIS")
- [ ] WhatsApp integration
- [ ] Web dashboard
- [ ] Home automation
- [ ] Mobile app

---

## Development

### Project Structure

```
jarvis/
├── jarvis.py           # Main application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment template
├── .env               # Your configuration (git ignored)
├── README.md          # This file
└── docs/              # Additional documentation
    └── HARDWARE.md    # Hardware recommendations
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## Hardware Recommendations

For the best local AI experience:

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 8GB | 16GB+ |
| Storage | 20GB free | SSD with 50GB+ |
| GPU | Not required | Apple Silicon / NVIDIA |

**Tested On:**
- Mac Mini M4 (24GB) - Excellent
- Windows PC with RTX 4070 - Excellent
- ThinkPad T480s (no GPU) - Cloud mode only

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Acknowledgments

- [Anthropic](https://anthropic.com) for Claude
- [Ollama](https://ollama.ai) for local AI infrastructure
- Inspired by the Iron Man films

---

<div align="center">

**Built with ❤️ by Carlos Macineira**

[GitHub](https://github.com/carlosmacineira) • [Charlie Mac Industries](https://charliemacindustries.com)

</div>
