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

**Personal AI Assistant — Local + Cloud Hybrid**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-green.svg)](https://ollama.ai)
[![Claude](https://img.shields.io/badge/Claude-Cloud%20AI-orange.svg)](https://anthropic.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Built by Carlos Macineira — Charlie Mac Industries*

</div>

---

## Overview

JARVIS is a personal AI assistant with a hybrid architecture: local inference via Ollama for privacy, cloud inference via Claude for complex reasoning, and automatic routing between the two.

**Core features:**

- **Local mode** — Run completely offline with Ollama (uncensored models supported)
- **Cloud mode** — Tap into Claude for harder problems
- **Auto mode** — Queries get routed to the right backend automatically
- **Streaming CLI** — Rich terminal UI with live-streamed responses
- **Conversation memory** — Context carries across messages
- **Web dashboard** — visionOS-inspired spatial UI built with React, Tailwind, and Framer Motion

---

## Quick Start

```bash
# Clone and setup
git clone https://github.com/carlosmacineira/jarvis.git
cd jarvis

python3 -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
nano .env                  # Add your ANTHROPIC_API_KEY

# Pull a local model (optional)
ollama pull dolphin-llama3:8b

# Run
python jarvis.py
```

### Dashboard

The web dashboard lives in `dashboard/`. To run it:

```bash
cd dashboard
npm install
npm run dev
```

Open `http://localhost:5173` — you'll see the spatial UI with a live terminal, system vitals, and the Jarvis orb.

---

## Configuration

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
ELEVENLABS_API_KEY=your-key-here   # optional, for voice
```

### Recommended Local Models

| Model | Size | Good for | Install |
|-------|------|----------|---------|
| `dolphin-llama3:8b` | 4.7 GB | General use, uncensored | `ollama pull dolphin-llama3:8b` |
| `dolphin-mixtral:8x7b` | 26 GB | Complex reasoning | `ollama pull dolphin-mixtral:8x7b` |
| `deepseek-coder:6.7b` | 3.8 GB | Programming | `ollama pull deepseek-coder:6.7b` |
| `llama3:8b` | 4.7 GB | General purpose | `ollama pull llama3:8b` |

---

## Commands

| Command | What it does |
|---------|-------------|
| `mode local` | Switch to Ollama |
| `mode cloud` | Switch to Claude |
| `mode auto` | Let JARVIS decide |
| `status` | System health check |
| `models` | List installed Ollama models |
| `clear` | Wipe conversation history |
| `help` | Show commands |
| `exit` | Shut down |

---

## Architecture

```
┌───────────────────────────────────────────────┐
│                  JARVIS                        │
│                                               │
│   User Input ──► Router (auto / manual)       │
│                     │                         │
│            ┌────────┴────────┐                │
│            ▼                 ▼                │
│     ┌────────────┐   ┌────────────┐          │
│     │   Ollama   │   │   Claude   │          │
│     │  (local)   │   │  (cloud)   │          │
│     └────────────┘   └────────────┘          │
│                                               │
│   Web Dashboard (React) ◄── System Vitals    │
└───────────────────────────────────────────────┘
```

---

## Project Structure

```
jarvis/
├── jarvis.py              # Main CLI application
├── requirements.txt       # Python dependencies
├── .env                   # Your API keys (git-ignored)
├── dashboard/             # Web dashboard (React + Vite)
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.css      # Tailwind config + glass theme
│   │   └── components/
│   │       ├── Orb.jsx             # Animated central orb
│   │       ├── GlassCard.jsx       # Glassmorphism wrapper
│   │       ├── Dock.jsx            # Bottom navigation dock
│   │       ├── TerminalWindow.jsx  # Boot sequence terminal
│   │       └── SystemVitals.jsx    # CPU/memory gauges
│   ├── package.json
│   └── vite.config.js
├── README.md
└── UPDATES.md             # Changelog
```

---

## Roadmap

- [x] Hybrid local/cloud architecture
- [x] Streaming responses
- [x] Rich terminal UI
- [x] Conversation memory
- [x] Web dashboard
- [ ] Voice input/output (ElevenLabs TTS, speech recognition)
- [ ] Wake word detection ("Hey JARVIS")
- [ ] WhatsApp / messaging integrations
- [ ] Home automation hooks
- [ ] Mobile app

---

## Hardware

Works on anything that can run Python. For local AI:

| | Minimum | Recommended |
|--|---------|-------------|
| RAM | 8 GB | 16 GB+ |
| Storage | 20 GB free | SSD, 50 GB+ |
| GPU | Not required | Apple Silicon or NVIDIA |

Tested on Mac Mini M4 (24 GB), RTX 4070 desktop, and a ThinkPad T480s (cloud-only).

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

Built by [Carlos Macineira](https://github.com/carlosmacineira) — [Charlie Mac Industries](https://charliemacindustries.com)

</div>
