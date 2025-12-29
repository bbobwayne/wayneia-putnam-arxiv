"""
Figure 5: CODE_KEY Ablation Study
WayneIA ArXiv Paper
Component contribution waterfall
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 9,
    'axes.titlesize': 14,
    'axes.labelsize': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

components = ['Baseline', '+Reasoning\nRouter', '+Fractal\nDispatcher', 
              '+Self-Evolving', '+Universal\nLanguage']
cumulative = [0.67, 1.83, 2.67, 3.33, 5.0]
contribution = [0.67, 1.16, 0.84, 0.66, 1.67]

colors = ['#bdc3c7', '#3498db', '#2ecc71', '#f39c12', '#0066cc']

fig, ax = plt.subplots(figsize=(8, 5))

x = np.arange(len(components))
bottom = [0] + cumulative[:-1]

bars = ax.bar(x, contribution, bottom=bottom, color=colors, edgecolor='white', linewidth=1.5)

for i, (bar, cum, contrib) in enumerate(zip(bars, cumulative, contribution)):
    ax.text(bar.get_x() + bar.get_width()/2, cum + 0.15,
            f'{cum}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    if contrib > 0.5:
        ax.text(bar.get_x() + bar.get_width()/2, bottom[i] + contrib/2,
                f'+{contrib}%', ha='center', va='center', fontsize=9, color='white', fontweight='bold')

ax.set_ylabel('Cumulative Solve Rate (%)', fontweight='bold')
ax.set_xlabel('System Configuration', fontweight='bold')
ax.set_title('CODE_KEY Component Ablation Study', fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(components)
ax.set_ylim(0, 6)

ax.axhline(y=5.0, color='#0066cc', linestyle='--', alpha=0.3, linewidth=1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig5_ablation.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig5_ablation.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig5_ablation.png and .pdf")
plt.close()
