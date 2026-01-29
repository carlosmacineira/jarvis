# JARVIS HARDWARE SPECIFICATIONS
## Recommended Builds for Local AI

---

## Quick Reference: What Can Your Hardware Run?

| Your VRAM | Best Model | Intelligence Level |
|-----------|------------|-------------------|
| 4 GB | Phi-3 Mini, TinyLlama | Basic assistant |
| 6 GB | Llama 3 8B (Q4) | Good - GPT-3.5 level |
| 8 GB | Dolphin-Llama3 8B | Very Good |
| 12 GB | Dolphin-Mixtral, 13B models | Excellent |
| 16 GB | 30B models | Near cloud quality |
| 24 GB | 70B models (quantized) | Rivals Claude |
| 48 GB+ | 70B+ full precision | Maximum capability |

---

## BUILD OPTION 1: Budget Build (~$400-500)
### "The Starter"

**Best for:** Testing, light use, learning

| Component | Recommendation | Price (Est.) |
|-----------|---------------|--------------|
| GPU | Used RTX 3060 12GB | $200-250 |
| CPU | Any modern 6+ core | $100-150 |
| RAM | 16 GB DDR4 | $40-50 |
| Storage | 500GB NVMe SSD | $40-50 |
| PSU | 550W 80+ Bronze | $50-60 |

**What it runs:**
- Dolphin-Llama3 8B ✓
- 13B models ✓
- Mixtral 8x7B (slower) ✓
- 70B models ✗

**Performance:** ~40-50 tokens/second on 8B models

---

## BUILD OPTION 2: Sweet Spot Build (~$800-1000)
### "The Workhorse" ⭐ RECOMMENDED

**Best for:** Daily driver, serious local AI use

| Component | Recommendation | Price (Est.) |
|-----------|---------------|--------------|
| GPU | RTX 4070 12GB or Used RTX 3090 24GB | $500-600 |
| CPU | Ryzen 5 5600 or Intel i5-12400 | $120-150 |
| RAM | 32 GB DDR4 | $70-90 |
| Storage | 1TB NVMe SSD | $70-80 |
| PSU | 650W 80+ Gold | $70-80 |

**What it runs:**
- All 8B models ✓ (fast)
- All 13B models ✓
- Mixtral 8x7B ✓
- 30B models ✓ (with RTX 3090)
- 70B quantized ✓ (RTX 3090 only, slower)

**Performance:** 
- RTX 4070: ~60 tokens/sec on 8B, ~30 on 13B
- RTX 3090: ~50 tokens/sec on 8B, can run 70B

---

## BUILD OPTION 3: High-End Build (~$1500-2000)
### "The Powerhouse"

**Best for:** Maximum local capability, approaching cloud quality

| Component | Recommendation | Price (Est.) |
|-----------|---------------|--------------|
| GPU | RTX 4090 24GB | $1600-1800 |
| CPU | Ryzen 7 5800X or Intel i7-12700 | $200-250 |
| RAM | 64 GB DDR4/DDR5 | $150-200 |
| Storage | 2TB NVMe SSD | $120-150 |
| PSU | 850W 80+ Gold | $100-120 |

**What it runs:**
- Everything up to 70B ✓
- Multiple models simultaneously ✓
- Fast inference on large models ✓

**Performance:** ~80-100 tokens/sec on 8B, ~40 on 70B quantized

---

## BUILD OPTION 4: Mac Alternative
### "The Silent Server"

**Apple Silicon is exceptionally good for local LLMs due to unified memory.**

| Model | Unified Memory | Best For | Price |
|-------|---------------|----------|-------|
| Mac Mini M4 | 16 GB | 8-13B models | $599 |
| Mac Mini M4 Pro | 24 GB | Up to 30B models | $1,399 |
| Mac Mini M4 Pro | 48 GB | 70B models | $1,999 |
| Mac Studio M2 Ultra | 64-192 GB | Everything | $3,999+ |

**Advantages:**
- Silent operation (no fans at idle)
- Very power efficient
- Excellent Ollama support
- macOS reliability

**Disadvantages:**
- More expensive per GB of memory
- Can't upgrade later

---

## GPU COMPARISON CHART

| GPU | VRAM | New Price | Used Price | Best For |
|-----|------|-----------|------------|----------|
| RTX 3060 | 12 GB | $330 | $200-250 | Budget builds |
| RTX 3070 | 8 GB | N/A | $250-300 | Avoid (less VRAM than 3060) |
| RTX 3080 | 10 GB | N/A | $350-450 | Decent mid-range |
| RTX 3090 | 24 GB | N/A | $600-800 | Best value for VRAM |
| RTX 4060 | 8 GB | $300 | N/A | Entry level, efficient |
| RTX 4070 | 12 GB | $550 | N/A | Great efficiency |
| RTX 4080 | 16 GB | $1,000 | N/A | High-end |
| RTX 4090 | 24 GB | $1,800 | N/A | Maximum consumer |
| RTX 3090 Ti | 24 GB | N/A | $700-900 | Great used option |

**Key Insight:** The RTX 3090 used market offers the best value for raw VRAM. 
24GB lets you run 70B quantized models that smaller cards simply cannot.

---

## VRAM REQUIREMENTS BY MODEL

| Model | Parameters | Q4 VRAM | Q8 VRAM | FP16 VRAM |
|-------|------------|---------|---------|-----------|
| TinyLlama | 1.1B | 1 GB | 2 GB | 3 GB |
| Phi-3 Mini | 3.8B | 3 GB | 5 GB | 8 GB |
| Llama 3 8B | 8B | 5 GB | 9 GB | 16 GB |
| Llama 3 13B | 13B | 8 GB | 14 GB | 26 GB |
| Mixtral 8x7B | 47B (MoE) | 12 GB | 24 GB | 48 GB |
| Llama 3 70B | 70B | 40 GB | 70 GB | 140 GB |

**Q4 = 4-bit quantized (recommended for most users)**
**Q8 = 8-bit quantized (better quality, more VRAM)**
**FP16 = Full precision (maximum quality, requires enterprise hardware)**

---

## MY RECOMMENDATION FOR YOU, SIR

Given your goals of a powerful personal assistant with both local and cloud capabilities:

### Immediate (Use Existing Hardware):
1. Test with your ThinkPad to understand the workflow
2. Use cloud mode (Claude) for heavy lifting
3. Install Ollama and try smaller models to gauge performance

### Short-Term Upgrade (~$600-800):
**Used RTX 3090 24GB** + basic desktop components
- Runs 70B models (quantized)
- Matches or exceeds most cloud AI for many tasks
- Complete privacy for sensitive queries
- Pays for itself vs API costs within months of heavy use

### Future Expansion:
- Dedicated quiet server (could be Mac Mini for silence)
- Located in a closet/corner, accessed remotely
- Always-on Jarvis available from any device

---

## COST COMPARISON: Local vs Cloud

| Usage Level | Cloud Cost/Month | Local Hardware (Amortized) |
|-------------|------------------|---------------------------|
| Light (10K tokens/day) | $3-5 | $0 after hardware |
| Medium (50K tokens/day) | $15-25 | $0 after hardware |
| Heavy (200K tokens/day) | $60-100 | $0 after hardware |
| Very Heavy (1M tokens/day) | $300-500 | $0 after hardware |

**Break-even point:** Most users recoup hardware costs in 6-12 months of moderate use.

---

## FINAL NOTES

The hybrid approach gives you the best of both worlds:

- **Local (Ollama):** Privacy, no costs, unrestricted, offline capability
- **Cloud (Claude):** Maximum intelligence, current information, complex reasoning

Use local for:
- Personal/sensitive queries
- Unrestricted conversations
- Offline situations
- High-volume simple tasks

Use cloud for:
- Complex analysis
- Tasks requiring current information
- Professional document work
- Maximum accuracy requirements

Your Jarvis hybrid system handles this routing automatically in AUTO mode, 
or you can manually select with "mode local" and "mode cloud" commands.

---

*Document prepared by Jarvis for Carlos*
*Last updated: January 2026*
