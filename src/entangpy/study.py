from typing import Callable, Optional, Dict, Any, List
from .trial import Trial

class Study:
    def __init__(self, study_name: Optional[str] = None):
        self.study_name = study_name or "no-name-study"
        self.trials: List[Trial] = []

    def optimize(self, func: Callable[[Trial], float], n_trials: int = 100):
        for i in range(n_trials):
            trial = Trial(trial_id=i)
            try:
                value = func(trial)
                trial.report(value)
                self.trials.append(trial)
            except Exception as e:
                print(f"Trial {i} failed: {e}")
                # In a real library, we'd handle this better (e.g., mark as FAIL)
                continue

    @property
    def best_trial(self) -> Optional[Trial]:
        if not self.trials:
            return None
        # Minimal value optimization by default
        return min(self.trials, key=lambda t: t.value if t.value is not None else float('inf'))

    @property
    def best_params(self) -> Dict[str, Any]:
        if not self.best_trial:
            return {}
        return self.best_trial.params

    @property
    def best_value(self) -> Optional[float]:
        if not self.best_trial:
            return None
        return self.best_trial.value

def create_study(study_name: Optional[str] = None) -> Study:
    return Study(study_name=study_name)
