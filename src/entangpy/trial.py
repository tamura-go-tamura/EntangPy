import random
from typing import Dict, Any, Optional

class Trial:
    def __init__(self, trial_id: int):
        self.trial_id = trial_id
        self._params: Dict[str, Any] = {}
        self._value: Optional[float] = None
        
    def suggest_float(self, name: str, low: float, high: float) -> float:
        """
        Suggest a value for the floating point parameter.
        For now, this just uses random sampling (uniform).
        """
        if name in self._params:
            return self._params[name]
        
        # Simple random sampling (placeholder for quantum-inspired sampler)
        val = random.uniform(low, high)
        self._params[name] = val
        return val

    def report(self, value: float):
        """Report the objective value of the trial."""
        self._value = value

    @property
    def params(self) -> Dict[str, Any]:
        return self._params

    @property
    def value(self) -> Optional[float]:
        return self._value

    def __repr__(self):
        return f"Trial(trial_id={self.trial_id}, state=COMPLETE, value={self.value}, params={self.params})"
