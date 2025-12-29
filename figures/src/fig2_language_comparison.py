"""
Figure 2: Multi-Language Performance Comparison
WayneIA ArXiv Paper
Isabelle 6.5% | Lean 4 4.5% | Coq 4.0%
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

languages = ['Isabelle', 'Lean 4', 'Coq']
rates = [6.5, 4.5, 4.0]
solved = [13, 9, 8]
colors = ['#2ecc71', '#3498db', '#e67e22']

fig, ax = plt.subplots(figsize=(6, 4))

x = np.arange(len(languages))
width = 0.6

bars = ax.bar(x, rates, width, color=colors, edgecolor='white', linewidth=1.5)

for bar, rate, sol in zip(bars, rates, solved):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{rate}%\n({sol}/200)', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylabel('Solve Rate (%)', fontweight='bold')
ax.set_xlabel('Proof Assistant', fontweight='bold')
ax.set_title('WayneIA Multi-Language Performance on PutnamBench', fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(languages)
ax.set_ylim(0, 8.5)

ax.axhline(y=5.0, color='#0066cc', linestyle='--', alpha=0.5, linewidth=1, label='Combined (5.0%)')
ax.legend(loc='upper right')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig2_language_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig2_language_comparison.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig2_language_comparison.png and .pdf")
plt.close()
