import unittest

from tiny_solve_state import TinySolveState


class TestTinySolveStateMethods(unittest.TestCase):
    def test_get_submission_hints(self):
        solve_state = TinySolveState()
        result = solve_state.get_submission_hints('aabbc', 'edcba')
        self.assertEqual(result, 'y--gy')

    def test_get_hint_pattern_to_frequency_map(self):
        solve_state = TinySolveState()
        result = solve_state.get_hint_pattern_to_frequency_map('aback')
        self.assertEqual(result, {'ggggg': 1, 'yy-y-': 1, 'yyyy-': 1, 'y----': 8, 'yy---': 6, '---y-': 1, 'y-y-y': 1, 'y-yy-': 1, 'y---y': 1, '--ggg': 1, '-----': 1, 'y--yy': 1, 'y--y-': 1})

    def test_get_expected_score(self):
        solve_state = TinySolveState()
        score = solve_state.get_expected_score('aback')
        self.assertAlmostEqual(score, 3.06346518)

if __name__ == '__main__':
    unittest.main()
