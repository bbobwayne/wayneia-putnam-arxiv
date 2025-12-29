"""
Figure 3: Category Performance Radar
WayneIA ArXiv Paper
9 mathematical categories
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

categories = ['Probability', 'Number\nTheory', 'Analysis', 'Geometry', 
              'Algebra', 'Linear\nAlgebra', 'Abstract\nAlgebra', 
              'Combinatorics', 'Set\nTheory']
rates = [10.0, 8.96, 6.45, 5.45, 4.21, 0.0, 0.0, 0.0, 0.0]

N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
rates_plot = rates + [rates[0]]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

ax.fill(angles, rates_plot, color='#0066cc', alpha=0.25)
ax.plot(angles, rates_plot, color='#0066cc', linewidth=2, marker='o', markersize=6)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=9)
ax.set_ylim(0, 12)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2%', '4%', '6%', '8%', '10%'], size=8)

ax.set_title('WayneIA Performance by Mathematical Category', fontweight='bold', pad=20, size=14)

for angle, rate, cat in zip(angles[:-1], rates, categories):
    if rate > 0:
        ax.annotate(f'{rate}%', xy=(angle, rate), xytext=(angle, rate + 1.5),
                    ha='center', fontsize=8, fontweight='bold', color='#0066cc')

plt.tight_layout()

fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig3_category_radar.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig3_category_radar.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig3_category_radar.png and .pdf")
plt.close()
