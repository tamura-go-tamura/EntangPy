# EntangPy: Quantum-inspired Optimization Library for Everyone

![EntangPy](https://raw.githubusercontent.com/tamura-go-tamura/EntangPy/main/docs/logo.png)

> **Unlock the power of quantum mechanics with simple Python code.**

`EntangPy` is a library that allows you to use quantum-inspired optimization algorithms (like quantum tunneling and superposition) as easily as calling a function. Designed for data scientists and engineers who want to explore beyond classical optimization without needing a PhD in physics.

## Features

- **Quantum-Inspired Algorithms**: Includes solvers based on Simulated Bifurcation, Quantum Monte Carlo, and more.
- **Simple API**: Just define your objective function and run. Similar to Optuna.
- **Classical Backend**: Runs on your CPU/GPU. No quantum computer required.

## Installation

```bash
pip install entangpy
```

## Quick Start

```python
import entangpy

def objective(trial):
    x = trial.suggest_float("x", -10, 10)
    return (x - 2) ** 2

study = entangpy.create_study()
study.optimize(objective, n_trials=100)

print(study.best_params)  # {'x': 2.0}
```

## Contributing

Pull requests are welcome!

## License

MIT License
