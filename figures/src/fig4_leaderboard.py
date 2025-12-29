"""
Figure 4: PutnamBench Leaderboard Position
WayneIA ArXiv Paper - CRITICAL FIGURE
Shows 3025% improvement over GPT-4o baseline
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 9,
    'axes.titlesize': 14,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

systems = ['GPT-4o\n(Baseline)', 'Goedel-Prover', 'Special-Prover', 'WayneIA\n(This Work)', 'DeepSeek-V2\n(SOTA)']
rates = [0.16, 1.09, 1.22, 5.0, 7.29]

colors = ['#bdc3c7', '#95a5a6', '#95a5a6', '#0066cc', '#9b59b6']

fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.barh(systems, rates, color=colors, edgecolor='white', linewidth=1.5)

for i, (bar, rate) in enumerate(zip(bars, rates)):
    if i == 3:
        ax.text(rate + 0.15, bar.get_y() + bar.get_height()/2, 
                f'{rate}%', va='center', ha='left', fontweight='bold', fontsize=11, color='#0066cc')
    elif i == 4:
        ax.text(rate + 0.15, bar.get_y() + bar.get_height()/2, 
                f'{rate}%', va='center', ha='left', fontsize=10, color='#9b59b6')
    else:
        ax.text(rate + 0.15, bar.get_y() + bar.get_height()/2, 
                f'{rate}%', va='center', ha='left', fontsize=10)

improvement = ((5.0 - 0.16) / 0.16) * 100
ax.annotate(f'+{improvement:.0f}%\nvs baseline', 
            xy=(5.0, 3), xytext=(6.5, 2.2),
            fontsize=10, fontweight='bold', color='#0066cc',
            arrowprops=dict(arrowstyle='->', color='#0066cc', lw=1.5),
            ha='center')

ax.axvline(x=5.0, color='#0066cc', linestyle='--', alpha=0.3, linewidth=1)

ax.set_xlabel('Solve Rate (%)', fontweight='bold')
ax.set_title('PutnamBench Leaderboard: WayneIA vs. State-of-the-Art', fontweight='bold', pad=15)
ax.set_xlim(0, 8.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig4_leaderboard.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig4_leaderboard.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig4_leaderboard.png and .pdf")
plt.close()
