import unittest
import entangpy

class TestCore(unittest.TestCase):

    def test_optimization(self):
        def objective(trial):
            x = trial.suggest_float("x", -10, 10)
            return (x - 2) ** 2

        study = entangpy.create_study()
        study.optimize(objective, n_trials=10)
        
        self.assertEqual(len(study.trials), 10)
        self.assertIsNotNone(study.best_params.get("x"))
        self.assertLess(study.best_value, 100) # Should be better than random worst case

    def test_constraints(self):
        def objective(trial):
            x = trial.suggest_float("x", 0, 1)
            self.assertTrue(0 <= x <= 1)
            return x

        study = entangpy.create_study()
        study.optimize(objective, n_trials=5)

if __name__ == '__main__':
    unittest.main()
