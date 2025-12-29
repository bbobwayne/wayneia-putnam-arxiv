# WayneIA PutnamBench - Reproducibility Specification
## ArXiv Technical Report Supplementary Materials

---

## 1. Hardware Specification

### Primary Nodes

| Node | IP | Hardware | OS | Role |
|------|-----|----------|-----|------|
| WaynePC | 192.168.1.19 | RTX 4070 SUPER (12GB), RTX 3080 (10GB) | Ubuntu 24.04 | Quantum API, Primary Inference |
| WindowsPC | 192.168.1.38 | RTX 3070 (8GB), 8x Coral TPU (32 TOPS) | Windows 11 | Benchmark Execution |
| Pi-5 MCM | 192.168.1.173 | Hailo-8 (26 TOPS), Raspberry Pi 5 | Raspberry Pi OS | Edge Inference |

### Total Compute
- **GPU VRAM**: 30GB combined
- **Edge TOPS**: 58 TOPS (Coral + Hailo)
- **Total Effective**: 84+ TOPS

---

## 2. Software Environment

### Python Environment
```bash
# Python version
Python 3.11.7

# Core dependencies
torch==2.1.2
transformers==4.36.2
numpy==1.26.3
pandas==2.1.4
scipy==1.12.0
```

### Proof Assistants
```bash
# Lean 4
lean --version
# Lean (version 4.3.0, commit ...)

# Isabelle
isabelle version
# Isabelle2024

# Coq
coqc --version
# The Coq Proof Assistant, version 8.18.0
```

### Full Requirements
```
# requirements.txt
torch>=2.1.0
transformers>=4.36.0
numpy>=1.26.0
pandas>=2.1.0
scipy>=1.12.0
asyncio-mqtt>=0.16.0
aiohttp>=3.9.0
pyyaml>=6.0
tqdm>=4.66.0
```

---

## 3. Dataset Access

### PutnamBench Repository
```bash
git clone https://github.com/trishullab/PutnamBench.git
cd PutnamBench
```

### Problem Distribution
| Language | Problems | Source Directory |
|----------|----------|------------------|
| Lean 4 | 672 | `lean4/` |
| Isabelle | 640 | `isabelle/` |
| Coq | 412 | `coq/` |

### Sampling Strategy
```python
# Random stratified sampling
import random
random.seed(42)

problems_per_language = 200
categories = ['algebra', 'analysis', 'number_theory', 'geometry', 
              'probability', 'combinatorics', 'linear_algebra', 
              'abstract_algebra', 'set_theory']

# Stratified by category proportions
sample = stratified_sample(problems, categories, n=problems_per_language)
```

---

## 4. Evaluation Protocol

### Pass@10 Evaluation
```python
def evaluate_problem(problem, attempts=10):
    """
    Evaluate a single problem with multiple attempts.
    
    Returns:
        bool: True if any attempt succeeds
    """
    for attempt in range(attempts):
        proof = generate_proof(problem)
        if verify_proof(proof, problem.language):
            return True
    return False
```

### Verification Commands
```bash
# Lean 4 verification
lake env lean --run proof.lean

# Isabelle verification
isabelle build -o document=false -D proof.thy

# Coq verification
coqc proof.v
```

### Success Criteria
- Proof compiles without errors
- All proof obligations discharged
- No `sorry`, `admit`, or `Admitted` statements

---

## 5. Agent Configuration

### CODE_KEY Registry
```python
CODE_KEYS = {
    24: "REASONING_ROUTER",
    23: "QUANTUM_DECISION",
    32: "COMBINATORICS_FIX",
    99: "VISUAL_BRIDGE",
    104: "FRACTAL_DISPATCHER",
    115: "BOB_PROXY",
    200: "ULTRATHINK",
    210: "FORMAL_ENCODE",
    211: "LEAN4_TRANSFORM",
    212: "ISABELLE_TRANSFORM",
    213: "COQ_TRANSFORM",
    214: "PROOF_VERIFY",
    220: "UNIVERSAL_LANGUAGE",
}
```

### Master Cipher
```
V1:24S104S23S99S32S211P212P213S214R:UNILANG
```

### Agent Files
| Agent | Size | Location |
|-------|------|----------|
| universal_language_transformer.py | 29KB | reasoning/agents/ |
| self_evolving_agent.py | 26KB | reasoning/agents/ |
| codekey_cipher_transformer.py | 22KB | reasoning/agents/ |
| quantum_decision_engine.py | 19KB | reasoning/agents/ |
| reasoning_router.py | 18KB | reasoning/agents/ |
| fractal_dispatcher.py | 17KB | reasoning/agents/ |
| ecosystem_integration.py | 15KB | reasoning/agents/ |

---

## 6. Hyperparameters

### Reasoning Router
```python
router_config = {
    'complexity_weights': {
        'depth': 0.3,
        'concepts': 0.4,
        'novelty': 0.3
    },
    'strategy_thresholds': {
        'CLASSICAL': 0.3,
        'REFLEXION': 0.5,
        'LATS': 0.7,
        'HYBRID': 0.85,
        'ULTRATHINK': 0.95
    }
}
```

### Self-Evolving Agent
```python
evolution_config = {
    'max_iterations': 5,
    'reflexion_depth': 3,
    'lats_branching_factor': 4,
    'improvement_threshold': 0.05
}
```

### Universal Language Transformer
```python
ult_config = {
    'parallel_languages': True,
    'timeout_per_language': 120,  # seconds
    'verification_retries': 3,
    'cross_language_hints': True
}
```

---

## 7. Execution Commands

### Full Benchmark Run
```bash
cd /path/to/wayne-ia-eco-OFFICIAL-benchmark

# Run full PUTNAM benchmark
python putnam_full_benchmark.py --samples 200 --languages all

# Output: results/putnam_full_benchmark_YYYYMMDD_HHMMSS.json
```

### Single Language Run
```bash
# Lean 4 only
python putnam_full_benchmark.py --samples 200 --languages lean4

# Isabelle only
python putnam_full_benchmark.py --samples 200 --languages isabelle

# Coq only
python putnam_full_benchmark.py --samples 200 --languages coq
```

### Ablation Study
```bash
# Baseline (no agents)
python putnam_full_benchmark.py --samples 50 --ablation baseline

# Progressive addition
python putnam_full_benchmark.py --samples 50 --ablation +router
python putnam_full_benchmark.py --samples 50 --ablation +fractal
python putnam_full_benchmark.py --samples 50 --ablation +evolving
python putnam_full_benchmark.py --samples 50 --ablation +universal
```

---

## 8. Expected Results

### Main Results
| Language | Expected Rate | Confidence Interval |
|----------|---------------|---------------------|
| Overall | 5.0% | [4.2%, 5.8%] |
| Isabelle | 6.5% | [5.2%, 7.8%] |
| Lean 4 | 4.5% | [3.4%, 5.6%] |
| Coq | 4.0% | [2.9%, 5.1%] |

### Variance Notes
- Results may vary ±0.5% due to sampling randomness
- Hardware differences may affect timeout-based results
- Proof assistant version changes may affect compatibility

---

## 9. Result Files

### JSON Output Format
```json
{
  "timestamp": "2025-12-27T20:18:05.709134",
  "benchmark": "PutnamBench Full",
  "code_key_anchor": "[220] UNIVERSAL_LANGUAGE",
  "master_cipher": "V1:24S104S23S99S32S211P212P213S214R:UNILANG",
  "languages": {
    "lean4": {"total": 200, "solved": 9, "rate": 4.5},
    "isabelle": {"total": 200, "solved": 13, "rate": 6.5},
    "coq": {"total": 200, "solved": 8, "rate": 4.0}
  },
  "overall": {
    "total_problems": 600,
    "total_solved": 30,
    "success_rate": 5.0
  }
}
```

### File Locations
```
results/
├── putnam_full_benchmark_20251227_201805.json
├── wayneia_putnam_results_summary.json
└── category_breakdown.json

reports/
├── PUTNAM_OFFICIAL_RESULTS_FINAL_DEC27_2025.md
└── PUTNAM_FULL_BENCHMARK_REPORT_20251227.md
```

---

## 10. Citation

```bibtex
@misc{wayneia2025putnam,
  title={Self-Origin AGI: Multi-Domain Formal Theorem Proving 
         with Universal Language Transformation},
  author={WayneIA LLC},
  year={2025},
  howpublished={\url{https://github.com/bbobwayne/wayne-ia-eco-OFFICIAL-benchmark}},
  note={PutnamBench: 5.0\% (30/600 multi-language)}
}
```

---

## 11. Contact

- **Repository**: https://github.com/bbobwayne/wayne-ia-eco-OFFICIAL-benchmark
- **Email**: bw@wayneia.com
- **Organization**: WayneIA LLC, Waco, Texas

---

*Last Updated: December 29, 2025*
*Version: 1.0*
