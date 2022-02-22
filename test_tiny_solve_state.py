import unittest

from tiny_solve_state import TinySolveState


class TestTinySolveStateMethods(unittest.TestCase):
    def test_get_submission_hints(self):
        solve_state = TinySolveState()
        result = solve_state.get_submission_hints('aa', 'ab')
        self.assertEqual(result, 'g-')

    def test_get_hint_pattern_to_frequency_map(self):
        solve_state = TinySolveState()
        result = solve_state.get_hint_pattern_to_frequency_map('ab')
        self.assertEqual(result, {'-g': 1, 'g-': 1, 'gg': 1, 'yy': 1})

    def test_get_expected_score(self):
        solve_state = TinySolveState()
        score = solve_state.get_expected_score('ab')
        self.assertAlmostEqual(score, 2)

    def test_get_sorted_word_to_expected_score(self):
        solve_state = TinySolveState()
        self.assertAlmostEqual(solve_state.get_sorted_word_to_expected_score(), [['aa', 2], ['ab', 2], ['ba', 2], ['bb', 2]])

if __name__ == '__main__':
    unittest.main()
