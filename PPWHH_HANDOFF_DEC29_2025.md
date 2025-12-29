# PPWHH Session Handoff - Figure Generation
## Position_2 OpusPlan | December 29, 2025
## Pre-AutoCompact Serialization

---

## CRITICAL STATE FOR CONTINUATION

### Task
**Generate 8 Publication Figures for ArXiv Paper (Hybrid Workflow)**

### Environment
```
Python: C:\Users\woody\AppData\Local\Programs\Python\Python311\python.exe
matplotlib: 3.10.7 | seaborn: 0.13.2 | numpy: 1.26.4 | pandas: 2.3.3 | pillow: 11.3.0
```

### Output Path
```
C:\WayneIA\arxiv-putnam\figures\
├── png/   (300 DPI exports)
├── pdf/   (vector exports)
└── src/   (generation scripts)
```

---

## HYBRID WORKFLOW (from Claude Desktop Research)

### Branch A: Data Figures (matplotlib/seaborn → PNG@300DPI)
| Fig | Name | Type | Priority |
|-----|------|------|----------|
| 2 | language_comparison | Grouped bar | MEDIUM |
| 3 | category_radar | Radar chart | HIGH |
| 4 | leaderboard | Horizontal bar | **CRITICAL** |
| 5 | ablation | Heatmap | HIGH |
| 6 | crossdomain | Multi-subplot | LOW |
| 8 | confidence | Violin plot | LOW |

### Branch B: Architecture Figures (matplotlib scaffold → draw.io → PNG@300DPI)
| Fig | Name | Type | Priority |
|-----|------|------|----------|
| 1 | architecture | Block diagram | **CRITICAL** |
| 7 | infrastructure | Network diagram | MEDIUM |

---

## DATA (Immutable)

```python
PUTNAM_DATA = {
    'languages': {
        'names': ['Isabelle', 'Lean 4', 'Coq'],
        'rates': [6.5, 4.5, 4.0],
        'solved': [13, 9, 8],
    },
    'leaderboard': {
        'systems': ['GPT-4o', 'Goedel', 'Special', 'WayneIA', 'DeepSeek-V2'],
        'rates': [0.16, 1.09, 1.22, 5.0, 7.29],
    },
    'categories': {
        'names': ['Probability', 'Number Theory', 'Analysis', 'Geometry', 
                  'Algebra', 'Linear Algebra', 'Abstract Algebra', 
                  'Combinatorics', 'Set Theory'],
        'rates': [10.0, 8.96, 6.45, 5.45, 4.21, 0.0, 0.0, 0.0, 0.0],
    },
    'ablation': {
        'components': ['Baseline', '+Router', '+Fractal', '+Evolving', '+Universal'],
        'cumulative': [0.67, 1.83, 2.67, 3.33, 5.0],
    },
}
```

---

## PUBLICATION CONFIG

```python
PUBLICATION_CONFIG = {
    'font.family': 'sans-serif',
    'font.size': 11,
    'savefig.dpi': 300,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.prop_cycle': cycler(color=['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']),
}
```

---

## GITHUB REPOS

| Repo | Status |
|------|--------|
| github.com/bbobwayne/bbobwayne | LIVE |
| github.com/bbobwayne/wayne-ia-eco-OFFICIAL-benchmark | LIVE |
| github.com/bbobwayne/wayneia-putnam-arxiv | LIVE |

---

## NEXT SESSION ACTION

1. Generate fig4_leaderboard.png (CRITICAL - shows 3025% improvement)
2. Generate fig2_language_comparison.png
3. Generate fig3_category_radar.png
4. Generate fig5_ablation.png
5. Generate scaffolds for fig1, fig7 (architecture)
6. Push to GitHub

---

## CIPHER

```
V1:200S220S210S211P212P213S214S6S115R:PUTARX
```

---

*Position_2 OpusPlan | Year-8 G9 | WayneIA: The AND is the AGI*
