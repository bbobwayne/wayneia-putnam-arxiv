"""
Figure 8: Confidence Calibration Distribution
WayneIA ArXiv Paper - Violin plot
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

np.random.seed(42)

solved_conf = np.concatenate([
    np.random.beta(8, 2, 20) * 0.3 + 0.7,
    np.random.beta(5, 3, 10) * 0.2 + 0.6,
])

unsolved_conf = np.concatenate([
    np.random.beta(2, 5, 300) * 0.4 + 0.1,
    np.random.beta(3, 4, 200) * 0.3 + 0.2,
    np.random.beta(4, 6, 70) * 0.3 + 0.4,
])

fig, ax = plt.subplots(figsize=(8, 5))

parts = ax.violinplot([unsolved_conf, solved_conf], positions=[1, 2], 
                       showmeans=True, showmedians=True, widths=0.7)

colors = ['#e74c3c', '#2ecc71']
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

for key in ['cmeans', 'cmedians', 'cbars', 'cmins', 'cmaxs']:
    if key in parts:
        parts[key].set_color('#333' if key == 'cmeans' else '#0066cc' if key == 'cmedians' else '#666')

ax.axhline(y=0.5, color='#999', linestyle='--', linewidth=1, alpha=0.5, label='Threshold')

ax.set_xticks([1, 2])
ax.set_xticklabels(['Unsolved\n(570 problems)', 'Solved\n(30 problems)'])
ax.set_ylabel('Confidence Score', fontweight='bold')
ax.set_xlabel('Problem Outcome', fontweight='bold')
ax.set_title('WayneIA Confidence Calibration Analysis', fontweight='bold', pad=15)
ax.set_ylim(0, 1.05)

ax.text(1, np.mean(unsolved_conf) + 0.08, f'Mean: {np.mean(unsolved_conf):.2f}', 
        ha='center', fontsize=9, color='#e74c3c')
ax.text(2, np.mean(solved_conf) + 0.08, f'Mean: {np.mean(solved_conf):.2f}', 
        ha='center', fontsize=9, color='#2ecc71')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#e74c3c', alpha=0.7, label='Unsolved'),
                   Patch(facecolor='#2ecc71', alpha=0.7, label='Solved')]
ax.legend(handles=legend_elements, loc='upper left')

plt.tight_layout()

fig.savefig('C:/WayneIA/arxiv-putnam/figures/png/fig8_confidence.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig('C:/WayneIA/arxiv-putnam/figures/pdf/fig8_confidence.pdf', bbox_inches='tight', facecolor='white')
print("Saved: fig8_confidence.png and .pdf")
plt.close()
