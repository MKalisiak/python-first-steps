import unittest
import unittest.mock
import exercises as exercise
import io

class TestExercises(unittest.TestCase):

    def test_describe_list(self):
        result = exercise.describe_list(['test', (1, 5.5, 'foo'), 'bar', 2])
        expected = [(0, 'test'), (1, (1, 5.5, 'foo')), (2, 'bar'), (3, 2)]
        self.assertEqual(result, expected)

    def test_print_christmas_tree(self):
        expected = '  *  \n *** \n*****\n  *  \n *** \n*****\n  *  \n *** \n*****\n'
        self.assert_stdout(exercise.print_christmas_tree, {'width': 5}, expected)

    def test_print_christmas_tree_with_args(self):
        expected = '    o    \n   ooo   \n  ooooo  \n ooooooo \nooooooooo\n'
        self.assert_stdout(exercise.print_christmas_tree, {'width': 9, 'height': 1, 'character': 'o'}, expected)

    def test_remove_duplicates_loop(self):
        result = exercise.remove_duplicates_loop([1, 2, 3, 1, 5, 3, 2, 7])
        result.sort()
        expected = [1, 2, 3, 5, 7]
        self.assertEqual(result, expected)

    def test_remove_duplicates_set(self):
        result = exercise.remove_duplicates_set([1, 2, 3, 1, 5, 3, 2, 7])
        result.sort()
        expected = [1, 2, 3, 5, 7]
        self.assertEqual(result, expected)

    def test_flatten_dicts(self):
        a = {'a': 1, 'b': 2}
        b = {'b': 3, 'c': 3}
        c = {'d': 6, 'a': 7}
        result = exercise.flatten_dicts([a, b, c])
        expected = {'a': 8, 'b': 5, 'c': 3, 'd': 6}
        self.assertEqual(result, expected)

    def test_primes(self):
        result = exercise.primes(7)
        expected = [2, 3, 5, 7]
        self.assertEqual(result, expected)

        result = exercise.primes(100)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(result, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, function_to_call, kwargs, expected, mock_stdout):
        function_to_call(**kwargs)
        self.assertEqual(mock_stdout.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()