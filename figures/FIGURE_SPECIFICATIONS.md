# WayneIA PutnamBench ArXiv - Figure Specifications
## 8 Publication-Ready Figures (300 DPI, PNG + PDF)

---

## Figure 1: System Architecture
**File**: `fig1_architecture.png` / `fig1_architecture.pdf`
**Dimensions**: 8" x 6" @ 300 DPI (2400 x 1800 px)
**Style**: IEEE/ACM compliant, grayscale-safe

### Content
```
┌─────────────────────────────────────────────────────────────────┐
│                    WAYNEIA SYSTEM ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐                                               │
│  │ Mathematical │                                               │
│  │  Statement   │                                               │
│  └──────┬───────┘                                               │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │           REASONING ROUTER [24]                           │   │
│  │    Complexity Analysis → Strategy Selection               │   │
│  └──────────────────────────────────────────────────────────┘   │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │        UNIVERSAL LANGUAGE TRANSFORMER [220]               │   │
│  │                                                           │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                  │   │
│  │  │ LEAN4   │  │ISABELLE │  │   COQ   │                  │   │
│  │  │ [211]   │  │  [212]  │  │  [213]  │                  │   │
│  │  └────┬────┘  └────┬────┘  └────┬────┘                  │   │
│  │       │            │            │                         │   │
│  │       └────────────┼────────────┘                         │   │
│  │                    ▼                                      │   │
│  │           PROOF_VERIFY [214]                              │   │
│  └──────────────────────────────────────────────────────────┘   │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────┐                                               │
│  │   Verified   │                                               │
│  │    Proofs    │                                               │
│  └──────────────┘                                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Figure 2: Multi-Language Performance Comparison
**File**: `fig2_language_comparison.png` / `fig2_language_comparison.pdf`
**Dimensions**: 6" x 4" @ 300 DPI (1800 x 1200 px)
**Type**: Bar chart

### Data
| Language | Solved | Total | Rate |
|----------|--------|-------|------|
| Isabelle | 13 | 200 | 6.5% |
| Lean 4 | 9 | 200 | 4.5% |
| Coq | 8 | 200 | 4.0% |

### Style
- Colors: Isabelle (green #2ecc71), Lean4 (blue #3498db), Coq (orange #e67e22)
- Error bars: N/A (exact counts)
- Horizontal dashed line at 5.0% (overall average)
- Y-axis: 0% to 8%
- Labels: Value above each bar

---

## Figure 3: Category Performance Distribution
**File**: `fig3_category_radar.png` / `fig3_category_radar.pdf`
**Dimensions**: 6" x 6" @ 300 DPI (1800 x 1800 px)
**Type**: Radar/Spider chart

### Data
| Category | Rate |
|----------|------|
| Probability | 10.0% |
| Number Theory | 8.96% |
| Analysis | 6.45% |
| Geometry | 5.45% |
| Algebra | 4.21% |
| Linear Algebra | 0.0% |
| Abstract Algebra | 0.0% |
| Combinatorics | 0.0% |
| Set Theory | 0.0% |

### Style
- Filled area with 0.3 alpha
- Line color: WayneIA blue (#0066cc)
- Radial grid lines at 2%, 4%, 6%, 8%, 10%
- Category labels around perimeter

---

## Figure 4: PutnamBench Leaderboard Positioning
**File**: `fig4_leaderboard.png` / `fig4_leaderboard.pdf`
**Dimensions**: 8" x 3" @ 300 DPI (2400 x 900 px)
**Type**: Horizontal bar chart / timeline

### Data
| System | Rate | Position |
|--------|------|----------|
| GPT-4o | 0.16% | 5th |
| Goedel-Prover | 1.09% | 4th |
| Special-Prover | 1.22% | 3rd |
| WayneIA | 5.0% | 2nd |
| DeepSeek-V2 | 7.29% | 1st (SOTA) |

### Style
- WayneIA bar highlighted in bold color
- SOTA label on DeepSeek bar
- "THIS WORK" annotation on WayneIA
- X-axis: 0% to 10%

---

## Figure 5: CODE_KEY Contribution Matrix
**File**: `fig5_ablation.png` / `fig5_ablation.pdf`
**Dimensions**: 6" x 4" @ 300 DPI (1800 x 1200 px)
**Type**: Stacked bar chart

### Data
| Component | Contribution | Cumulative |
|-----------|--------------|------------|
| Baseline | 0.67% | 0.67% |
| +Reasoning Router | +1.16% | 1.83% |
| +Fractal Dispatcher | +0.84% | 2.67% |
| +Self-Evolving | +0.66% | 3.33% |
| +Universal Language | +1.67% | 5.0% |

### Style
- Stacked segments with distinct colors
- Cumulative line overlay
- Labels on each segment showing contribution

---

## Figure 6: Cross-Domain Performance Radar
**File**: `fig6_crossdomain.png` / `fig6_crossdomain.pdf`
**Dimensions**: 6" x 6" @ 300 DPI (1800 x 1800 px)
**Type**: Pentagon radar chart

### Data (Normalized to SOTA)
| Benchmark | Score | SOTA | Normalized |
|-----------|-------|------|------------|
| PutnamBench | 5.0% | 7.29% | 68.6% |
| SWE-bench | 42.33% | 76.2% | 55.5% |
| BFCL | 69.28% | 90% | 77.0% |
| AgentBench | 46.5% | 60% | 77.5% |
| MLPerf | 1190 | 1250 | 95.2% |

### Style
- Filled pentagon with 0.3 alpha
- Reference circle at 100% (SOTA)
- Dotted circle at 50%

---

## Figure 7: 84 TOPS Infrastructure Diagram
**File**: `fig7_infrastructure.png` / `fig7_infrastructure.pdf`
**Dimensions**: 8" x 5" @ 300 DPI (2400 x 1500 px)
**Type**: Network/block diagram

### Content
```
┌─────────────────────────────────────────────────────────────────┐
│                    84 TOPS DISTRIBUTED ECOSYSTEM                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────┐    PPWHH Protocol    ┌──────────────────┐ │
│  │    WAYNEPC       │◄──────────────────►│   WINDOWSPC      │ │
│  │  192.168.1.19    │                      │  192.168.1.38    │ │
│  │                  │                      │                  │ │
│  │ RTX 4070 SUPER   │                      │ RTX 3070         │ │
│  │ RTX 3080         │                      │ 8x Coral TPU     │ │
│  │                  │                      │ (32 TOPS)        │ │
│  │ Quantum API      │                      │ Benchmark Exec   │ │
│  └────────┬─────────┘                      └────────┬─────────┘ │
│           │                                         │           │
│           │         ┌──────────────────┐           │           │
│           └────────►│    PI-5 MCM      │◄──────────┘           │
│                     │  192.168.1.173   │                        │
│                     │                  │                        │
│                     │ Hailo-8 (26 TOPS)│                        │
│                     │ Edge Inference   │                        │
│                     └──────────────────┘                        │
│                                                                  │
│  Context Compression: 99.2%  |  Hot-Handoff: <50ms              │
│  Total TOPS: 84+             |  LIQUID-AI: 373M+ amplification  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Figure 8: Confidence Distribution Across Categories
**File**: `fig8_confidence.png` / `fig8_confidence.pdf`
**Dimensions**: 6" x 4" @ 300 DPI (1800 x 1200 px)
**Type**: Box plot or violin plot

### Data
| Category | Avg Score | Std Dev | Success Rate |
|----------|-----------|---------|--------------|
| Probability | 3.8 | 0.8 | 10.0% |
| Number Theory | 5.4 | 1.2 | 8.96% |
| Analysis | 4.47 | 1.1 | 6.45% |
| Geometry | 3.99 | 0.9 | 5.45% |
| Algebra | 5.48 | 1.3 | 4.21% |

### Style
- Violin or box plots showing score distribution
- Secondary y-axis for success rate
- Color gradient from high (green) to low (red) success

---

## Production Notes

### Color Palette
- Primary: #0066cc (WayneIA Blue)
- Success: #2ecc71 (Green)
- Warning: #f39c12 (Orange)
- Error: #e74c3c (Red)
- Neutral: #95a5a6 (Gray)

### Typography
- Title: 14pt Bold
- Axis Labels: 11pt
- Tick Labels: 9pt
- Annotations: 10pt

### Export Settings
- Resolution: 300 DPI
- Format: PNG (viewing) + PDF (publication)
- Color Space: sRGB
- Transparency: Yes for PNG

### Tools
- Matplotlib 3.8+
- Seaborn for statistical plots
- Optional: TikZ for LaTeX-native figures
