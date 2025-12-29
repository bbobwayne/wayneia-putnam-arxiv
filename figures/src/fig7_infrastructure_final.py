"""
Figure 7: 58 TOPS Distributed Infrastructure (Final Publication Version)
Refined from draw.io specification - 300 DPI
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

fig, ax = plt.subplots(figsize=(11, 7))
ax.set_xlim(0, 11)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

def draw_node(x, y, w, h, title, ip, hw1, hw2, role, color, border):
    rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.1', 
                          facecolor=color, edgecolor=border, linewidth=2.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 0.2, title, ha='center', va='top', fontsize=12, fontweight='bold')
    ax.text(x + w/2, y + h - 0.5, ip, ha='center', va='top', fontsize=9, color='#666')
    
    hw_rect1 = FancyBboxPatch((x + 0.1, y + h - 1.3), w/2 - 0.15, 0.45, 
                               facecolor='white', edgecolor=border, linewidth=1, alpha=0.7)
    ax.add_patch(hw_rect1)
    ax.text(x + w/4, y + h - 1.05, hw1, ha='center', va='center', fontsize=8)
    
    hw_rect2 = FancyBboxPatch((x + w/2 + 0.05, y + h - 1.3), w/2 - 0.15, 0.45, 
                               facecolor='white', edgecolor=border, linewidth=1, alpha=0.7)
    ax.add_patch(hw_rect2)
    ax.text(x + 3*w/4, y + h - 1.05, hw2, ha='center', va='center', fontsize=8)
    
    role_rect = FancyBboxPatch((x + 0.15, y + 0.2), w - 0.3, 0.7, 
                                facecolor='white', edgecolor=border, linewidth=1, alpha=0.5)
    ax.add_patch(role_rect)
    ax.text(x + w/2, y + 0.55, role, ha='center', va='center', fontsize=9, fontweight='bold')

ax.text(5.5, 6.7, '58 TOPS Distributed Edge AI Ecosystem', ha='center', va='center', fontsize=16, fontweight='bold')

draw_node(0.3, 4.2, 3.0, 2.2, 'WaynePC', '192.168.1.19', 'RTX 4070S', 'RTX 3080', 
          'Quantum API', '#e8f5e9', '#4caf50')
draw_node(4.0, 4.2, 3.0, 2.2, 'WindowsPC', '192.168.1.38', 'RTX 3070', '8x TPU (32T)', 
          'Benchmark Exec', '#e3f2fd', '#2196f3')
draw_node(7.7, 4.2, 3.0, 2.2, 'Pi-5 MCM', '192.168.1.173', 'Hailo-8', '26 TOPS', 
          'Edge Inference', '#fff3e0', '#ff9800')

hub = FancyBboxPatch((3.2, 1.5), 4.6, 2.2, boxstyle='round,pad=0.03,rounding_size=0.1', 
                      facecolor='#fce4ec', edgecolor='#e91e63', linewidth=2.5)
ax.add_patch(hub)
ax.text(5.5, 3.5, 'Central Coordination Hub', ha='center', va='top', fontsize=12, fontweight='bold', color='#c2185b')

metrics = [('LAN', '192.168.1.0/24'), ('Handoff', '50ms'), ('Compress', '99.2%')]
for i, (label, value) in enumerate(metrics):
    mx = 3.5 + i * 1.4
    m_rect = FancyBboxPatch((mx, 2.0), 1.2, 0.9, facecolor='#f8bbd0', edgecolor='#c2185b', linewidth=1)
    ax.add_patch(m_rect)
    ax.text(mx + 0.6, 2.75, label, ha='center', va='center', fontsize=9, fontweight='bold')
    ax.text(mx + 0.6, 2.3, value, ha='center', va='center', fontsize=8)

ax.text(5.5, 1.65, 'Total: 58 TOPS', ha='center', va='center', fontsize=11, fontweight='bold', color='#c2185b')

conn_points = [(1.8, 4.2, 4.0, 3.7), (5.5, 4.2, 5.5, 3.7), (9.2, 4.2, 7.0, 3.7)]
for x1, y1, x2, y2 in conn_points:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), 
                arrowprops=dict(arrowstyle='<->', color='#666', lw=2, connectionstyle='arc3,rad=0.1'))

stats_rect = FancyBboxPatch((0.3, 0.3), 2.5, 1.8, facecolor='#fafafa', edgecolor='#ccc', linewidth=1)
ax.add_patch(stats_rect)
ax.text(1.55, 1.95, 'Performance', ha='center', va='center', fontsize=10, fontweight='bold')
stats = ['PutnamBench: 5.0%', '+3025% vs GPT-4o', 'MLPerf: 1190 img/s', 'LIQUID: 373M+']
for i, s in enumerate(stats):
    color = '#0066cc' if 'vs' in s else '#333'
    ax.text(0.5, 1.55 - i*0.35, s, fontsize=8, color=color)

legend_rect = FancyBboxPatch((8.2, 0.3), 2.5, 1.8, facecolor='#fafafa', edgecolor='#ccc', linewidth=1)
ax.add_patch(legend_rect)
ax.text(9.45, 1.95, 'Node Legend', ha='center', va='center', fontsize=10, fontweight='bold')
leg_items = [('#e8f5e9', 'WaynePC - Quantum'), ('#e3f2fd', 'WindowsPC - TPU'), 
             ('#fff3e0', 'Pi-5 - Hailo'), ('#fce4ec', 'Hub - Coord')]
for i, (color, label) in enumerate(leg_items):
    lrect = FancyBboxPatch((8.35, 1.55 - i*0.35), 0.25, 0.2, facecolor=color, edgecolor='#999')
    ax.add_patch(lrect)
    ax.text(8.7, 1.57 - i*0.35, label, fontsize=7, va='center')

plt.tight_layout()
fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig7_infrastructure.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig7_infrastructure.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig7_infrastructure.png and .pdf (final publication version)")
plt.close()
