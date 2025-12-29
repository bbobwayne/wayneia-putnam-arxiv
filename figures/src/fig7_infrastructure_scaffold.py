"""
Figure 7: Infrastructure Network Diagram (Scaffold for draw.io)
Branch B - 58 TOPS distributed ecosystem
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')

def draw_node(x, y, w, h, title, specs, color='#e3f2fd', border='#1976d2'):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05', 
                                   facecolor=color, edgecolor=border, linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 0.25, title, ha='center', va='top', fontsize=10, fontweight='bold')
    ax.text(x + w/2, y + 0.3, specs, ha='center', va='bottom', fontsize=7, color='#666')

ax.text(5, 5.7, '58 TOPS Distributed Edge AI Ecosystem', ha='center', va='center', fontsize=14, fontweight='bold')

draw_node(0.3, 3, 2.8, 2, 'WaynePC', '192.168.1.19\nRTX 4070S + RTX 3080\nQuantum API', '#e8f5e9', '#4caf50')
draw_node(3.6, 3, 2.8, 2, 'WindowsPC', '192.168.1.38\nRTX 3070 + 8x Coral TPU\n32 TOPS', '#e3f2fd', '#2196f3')
draw_node(6.9, 3, 2.8, 2, 'Pi-5 MCM', '192.168.1.173\nHailo-8 (26 TOPS)\nEdge Inference', '#fff3e0', '#ff9800')

draw_node(3.6, 0.5, 2.8, 1.8, 'Central Hub', 'LAN: 192.168.1.0/24\nHandoff: 50ms\n99.2% compression', '#f3e5f5', '#9c27b0')

for node_x in [1.7, 5.0, 8.3]:
    ax.annotate('', xy=(5.0, 2.3), xytext=(node_x, 3.0), 
                arrowprops=dict(arrowstyle='<->', color='#666', lw=1.5, connectionstyle='arc3,rad=0.1'))

ax.text(5, -0.2, 'Scaffold for draw.io refinement - Branch B Hybrid Workflow', 
        ha='center', va='center', fontsize=8, style='italic', color='#666')

plt.tight_layout()

fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig7_infrastructure_scaffold.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig7_infrastructure_scaffold.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig7_infrastructure_scaffold.png and .pdf (for draw.io refinement)")
plt.close()
