# Changelog

## v4.0 — OpenClaw Migration (Feb 4, 2026)

Migrated from standalone Python CLI to an OpenClaw-based system running on Mac Mini M4.

**What changed:**
- Swapped the direct Ollama/Claude API calls for OpenClaw's tool ecosystem
- Added WhatsApp messaging as a primary interface alongside the CLI
- Upgraded memory from simple JSON to OpenClaw's semantic search + daily logs
- Integrated GitHub CLI for dev workflow automation
- Now running Claude Sonnet 4 via OpenClaw runtime (Node.js v25.5.0)

**New capabilities over v3:**
- Multi-channel messaging (WhatsApp live, Discord/Telegram planned)
- Browser automation, cron scheduling, file system tools
- Session management across multiple conversation threads

## v3.0 — CLI Redesign (Jan 2026)

Full rewrite of the terminal interface using Rich for styled output.

- Animated boot sequence with progress spinners
- Live-streaming responses from both Ollama and Claude
- System status table, mode switching, conversation memory
- Auto-routing: privacy-sensitive queries stay local, complex ones go to Claude

## v2.1 — UI Polish

Minor visual pass — improved layout and formatting in the terminal.

## v2.0 — Hybrid Architecture

Added Claude as a cloud backend alongside local Ollama, with automatic routing.

## v1.0 — Initial Release

Basic Ollama-powered CLI assistant with conversation history.
