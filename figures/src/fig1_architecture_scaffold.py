"""
Figure 1: WayneIA System Architecture (Scaffold for draw.io)
Branch B - generates placeholder with component layout
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

def draw_box(x, y, w, h, label, color='#e3f2fd', border='#1976d2'):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05', 
                                   facecolor=color, edgecolor=border, linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=9, fontweight='bold')

ax.text(5, 6.7, 'WayneIA System Architecture', ha='center', va='center', fontsize=14, fontweight='bold')

draw_box(3.5, 5.5, 3, 0.8, 'Problem Input\n(Putnam)', '#fff3e0', '#ff9800')

draw_box(0.5, 3.8, 2.5, 1.2, 'Reasoning\nRouter', '#e8f5e9', '#4caf50')
draw_box(3.5, 3.8, 3, 1.2, 'Fractal\nDispatcher', '#e3f2fd', '#2196f3')
draw_box(7, 3.8, 2.5, 1.2, 'Self-Evolving\nComponents', '#fce4ec', '#e91e63')

draw_box(0.5, 2, 2, 1.2, 'Isabelle\n(6.5%)', '#c8e6c9', '#388e3c')
draw_box(4, 2, 2, 1.2, 'Lean 4\n(4.5%)', '#bbdefb', '#1976d2')
draw_box(7.5, 2, 2, 1.2, 'Coq\n(4.0%)', '#ffe0b2', '#f57c00')

draw_box(3.5, 0.3, 3, 1.2, 'Universal Language\nTransformer', '#e1bee7', '#7b1fa2')

for start, end in [((5, 5.5), (5, 5.0)), ((1.75, 3.8), (1.5, 3.2)), ((5, 3.8), (5, 3.2)), 
                   ((8.25, 3.8), (8.5, 3.2)), ((1.5, 2), (3.5, 1.0)), ((5, 2), (5, 1.5)),
                   ((8.5, 2), (6.5, 1.0))]:
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))

ax.text(5, -0.3, 'Scaffold for draw.io refinement - Branch B Hybrid Workflow', 
        ha='center', va='center', fontsize=8, style='italic', color='#666')

plt.tight_layout()

fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig1_architecture_scaffold.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig1_architecture_scaffold.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig1_architecture_scaffold.png and .pdf (for draw.io refinement)")
plt.close()
