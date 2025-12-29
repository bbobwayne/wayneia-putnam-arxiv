"""
WayneIA ArXiv Paper - Figure Generation Configuration
December 29, 2025 | Position_2 OpusPlan

Hybrid Figure Generation Workflow Configuration
Ready to receive Claude Desktop research specifications
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

WAYNEIA_COLORS = {
    'primary': '#0066cc',
    'success': '#2ecc71',
    'warning': '#f39c12', 
    'error': '#e74c3c',
    'neutral': '#95a5a6',
    'isabelle': '#2ecc71',
    'lean4': '#3498db',
    'coq': '#e67e22',
    'wayneia': '#0066cc',
    'sota': '#9b59b6',
    'baseline': '#bdc3c7',
}

FIGURE_CONFIG = {
    'dpi': 300,
    'format': ['png', 'pdf'],
    'font_family': 'sans-serif',
    'font_size': {
        'title': 14,
        'axis_label': 11,
        'tick': 9,
        'annotation': 10,
        'legend': 9,
    },
    'figsize': {
        'standard': (6, 4),
        'wide': (8, 4),
        'square': (6, 6),
        'tall': (6, 8),
        'architecture': (8, 6),
        'timeline': (8, 3),
        'infrastructure': (8, 5),
    }
}

PUTNAM_DATA = {
    'languages': {
        'names': ['Isabelle', 'Lean 4', 'Coq'],
        'rates': [6.5, 4.5, 4.0],
        'solved': [13, 9, 8],
        'total': [200, 200, 200],
        'colors': ['#2ecc71', '#3498db', '#e67e22'],
    },
    'categories': {
        'names': ['Probability', 'Number Theory', 'Analysis', 'Geometry', 
                  'Algebra', 'Linear Algebra', 'Abstract Algebra', 
                  'Combinatorics', 'Set Theory'],
        'rates': [10.0, 8.96, 6.45, 5.45, 4.21, 0.0, 0.0, 0.0, 0.0],
        'total': [10, 67, 186, 55, 190, 41, 27, 20, 4],
        'solved': [1, 6, 12, 3, 8, 0, 0, 0, 0],
    },
    'leaderboard': {
        'systems': ['GPT-4o', 'Goedel-Prover', 'Special-Prover', 'WayneIA', 'DeepSeek-V2'],
        'rates': [0.16, 1.09, 1.22, 5.0, 7.29],
        'labels': ['Baseline', '', '', 'THIS WORK', 'SOTA'],
    },
    'ablation': {
        'components': ['Baseline', '+Reasoning Router', '+Fractal Dispatcher', 
                       '+Self-Evolving', '+Universal Language'],
        'cumulative': [0.67, 1.83, 2.67, 3.33, 5.0],
        'contribution': [0.67, 1.16, 0.84, 0.66, 1.67],
    },
    'crossdomain': {
        'benchmarks': ['PutnamBench', 'SWE-bench', 'BFCL', 'AgentBench', 'MLPerf'],
        'scores': [5.0, 42.33, 69.28, 46.5, 95.2],
        'sota': [7.29, 76.2, 90.0, 60.0, 100.0],
        'normalized': [68.6, 55.5, 77.0, 77.5, 95.2],
    },
    'infrastructure': {
        'nodes': [
            {'name': 'WaynePC', 'ip': '192.168.1.19', 'hw': 'RTX 4070S + RTX 3080', 'role': 'Quantum API'},
            {'name': 'WindowsPC', 'ip': '192.168.1.38', 'hw': 'RTX 3070 + 8x Coral TPU', 'role': 'Benchmark Exec'},
            {'name': 'Pi-5 MCM', 'ip': '192.168.1.173', 'hw': 'Hailo-8 (26 TOPS)', 'role': 'Edge Inference'},
        ],
        'total_tops': 84,
        'compression': 99.2,
        'handoff_ms': 50,
    },
}

OUTPUT_DIR = 'C:/WayneIA/arxiv-putnam/figures'

def setup_style():
    """Configure matplotlib style for publication figures."""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams.update({
        'font.family': FIGURE_CONFIG['font_family'],
        'font.size': FIGURE_CONFIG['font_size']['tick'],
        'axes.titlesize': FIGURE_CONFIG['font_size']['title'],
        'axes.labelsize': FIGURE_CONFIG['font_size']['axis_label'],
        'xtick.labelsize': FIGURE_CONFIG['font_size']['tick'],
        'ytick.labelsize': FIGURE_CONFIG['font_size']['tick'],
        'legend.fontsize': FIGURE_CONFIG['font_size']['legend'],
        'figure.dpi': FIGURE_CONFIG['dpi'],
        'savefig.dpi': FIGURE_CONFIG['dpi'],
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
    })

def save_figure(fig, name, formats=['png', 'pdf']):
    """Save figure in multiple formats."""
    for fmt in formats:
        path = f"{OUTPUT_DIR}/{fmt}/{name}.{fmt}"
        fig.savefig(path, format=fmt, dpi=FIGURE_CONFIG['dpi'], bbox_inches='tight')
        print(f"Saved: {path}")

if __name__ == '__main__':
    setup_style()
    print("Figure configuration loaded successfully")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"DPI: {FIGURE_CONFIG['dpi']}")
    print(f"Colors: {len(WAYNEIA_COLORS)} defined")
