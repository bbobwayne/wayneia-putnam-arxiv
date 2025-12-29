"""
Figure 6: Cross-Domain Benchmark Performance
WayneIA ArXiv Paper - Multi-benchmark radar
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

benchmarks = ['PutnamBench', 'SWE-bench\nLite', 'BFCL', 'AgentBench', 'MLPerf\nEdge']
wayneia_scores = [68.6, 55.5, 77.0, 77.5, 95.2]
sota_scores = [100, 100, 100, 100, 100]

N = len(benchmarks)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

wayneia_plot = wayneia_scores + [wayneia_scores[0]]
sota_plot = sota_scores + [sota_scores[0]]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.fill(angles, sota_plot, color='#e0e0e0', alpha=0.3, label='SOTA (100%)')
ax.plot(angles, sota_plot, color='#999999', linewidth=1.5, linestyle='--')

ax.fill(angles, wayneia_plot, color='#0066cc', alpha=0.3, label='WayneIA')
ax.plot(angles, wayneia_plot, color='#0066cc', linewidth=2.5, marker='o', markersize=8)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(benchmarks, size=10)
ax.set_ylim(0, 110)
ax.set_yticks([25, 50, 75, 100])
ax.set_yticklabels(['25%', '50%', '75%', '100%'], size=8)

for angle, score, bench in zip(angles[:-1], wayneia_scores, benchmarks):
    ax.annotate(f'{score:.1f}%', xy=(angle, score), xytext=(angle, score + 12),
                ha='center', fontsize=9, fontweight='bold', color='#0066cc')

ax.set_title('WayneIA Cross-Domain Benchmark Performance\n(Normalized to SOTA)', 
             fontweight='bold', pad=20, size=14)
ax.legend(loc='lower right', bbox_to_anchor=(1.15, -0.05))

plt.tight_layout()

fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig6_crossdomain.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig6_crossdomain.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig6_crossdomain.png and .pdf")
plt.close()
