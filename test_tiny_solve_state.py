import unittest

from tiny_solve_state import TinySolveState


class TestTinySolveStateMethods(unittest.TestCase):
    def test_get_submission_hints(self):
        solve_state = TinySolveState()
        result = solve_state.get_submission_hints('ab', 'bc')
        self.assertEqual(result, '-y')

    def test_get_hint_pattern_to_frequency_map(self):
        solve_state = TinySolveState()
        result = solve_state.get_hint_pattern_to_frequency_map('ab')
        self.assertEqual(result, {'g-': 2, 'gg': 1, 'yy': 1, '-g': 2, '-y': 1, 'y-': 1, '--': 1})

    def test_get_expected_score(self):
        solve_state = TinySolveState()
        score = solve_state.get_expected_score('ab')
        self.assertAlmostEqual(score, 2.72548055)

if __name__ == '__main__':
    unittest.main()
