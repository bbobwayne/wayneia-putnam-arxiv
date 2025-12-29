"""
Figure 1: WayneIA System Architecture (Final Publication Version)
Refined from draw.io specification - 300 DPI
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

fig, ax = plt.subplots(figsize=(11, 8.5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 8.5)
ax.set_aspect('equal')
ax.axis('off')

def draw_box(x, y, w, h, title, subtitle, color, border, title_size=10):
    rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.1', 
                          facecolor=color, edgecolor=border, linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 0.25, title, ha='center', va='top', fontsize=title_size, fontweight='bold')
    if subtitle:
        ax.text(x + w/2, y + 0.25, subtitle, ha='center', va='bottom', fontsize=8, color='#555')

ax.text(5.5, 8.1, 'WayneIA System Architecture', ha='center', va='center', fontsize=16, fontweight='bold')

draw_box(4, 6.8, 3, 0.9, 'Problem Input', 'Putnam Competition (600 problems)', '#fff2cc', '#d6b656')

codekey = FancyBboxPatch((0.8, 3.8), 9.4, 2.6, boxstyle='round,pad=0.05,rounding_size=0.15', 
                          facecolor='#f9f9f9', edgecolor='#888888', linewidth=1.5, linestyle='--')
ax.add_patch(codekey)
ax.text(1.0, 6.2, 'CODE_KEY Composition Layer', fontsize=10, fontweight='bold', color='#666666')

draw_box(1, 4, 2, 2.1, 'Reasoning\nRouter', 'CODE_KEY[210]\n+1.16%', '#d5e8d4', '#82b366')
draw_box(3.3, 4, 2, 2.1, 'Fractal\nDispatcher', 'CODE_KEY[211]\n+0.84%', '#dae8fc', '#6c8ebf')
draw_box(5.6, 4, 2, 2.1, 'Self-Evolving\nComponents', 'CODE_KEY[212]\n+0.66%', '#ffe6cc', '#d79b00')
draw_box(7.9, 4, 2.1, 2.1, 'Universal\nLanguage', 'CODE_KEY[220]\n+1.67%', '#e1d5e7', '#9673a6')

draw_box(0.8, 1.8, 2.4, 1.5, 'Isabelle', '6.5% (13/200)', '#c8e6c9', '#388e3c')
draw_box(4.3, 1.8, 2.4, 1.5, 'Lean 4', '4.5% (9/200)', '#bbdefb', '#1976d2')
draw_box(7.8, 1.8, 2.4, 1.5, 'Coq', '4.0% (8/200)', '#ffe0b2', '#f57c00')

output = FancyBboxPatch((3.5, 0.2), 4, 1.2, boxstyle='round,pad=0.03,rounding_size=0.1', 
                         facecolor='#0066cc', edgecolor='#004c99', linewidth=2)
ax.add_patch(output)
ax.text(5.5, 0.95, 'Verified Proof Output', ha='center', va='center', fontsize=11, fontweight='bold', color='white')
ax.text(5.5, 0.55, '30/600 (5.0%) | +3025% vs GPT-4o', ha='center', va='center', fontsize=9, color='white')

arrows = [
    ((5.5, 6.8), (5.5, 6.5)),
    ((2.0, 4.0), (2.0, 3.3)),
    ((4.3, 4.0), (5.5, 3.3)),
    ((6.6, 4.0), (5.5, 3.3)),
    ((9.0, 4.0), (9.0, 3.3)),
    ((2.0, 1.8), (4.5, 1.4)),
    ((5.5, 1.8), (5.5, 1.4)),
    ((9.0, 1.8), (6.5, 1.4)),
]

for start, end in arrows:
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))

legend_x, legend_y = 8.8, 7.2
ax.text(legend_x, legend_y + 0.5, 'Legend', fontsize=9, fontweight='bold')
legend_items = [
    ('#fff2cc', 'Input/Output'),
    ('#dae8fc', 'CODE_KEY'),
    ('#c8e6c9', 'Proof Assistants'),
]
for i, (color, label) in enumerate(legend_items):
    rect = FancyBboxPatch((legend_x, legend_y - i*0.35), 0.3, 0.25, facecolor=color, edgecolor='#999')
    ax.add_patch(rect)
    ax.text(legend_x + 0.4, legend_y - i*0.35 + 0.12, label, fontsize=8, va='center')

plt.tight_layout()
fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig1_architecture.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig1_architecture.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig1_architecture.png and .pdf (final publication version)")
plt.close()
