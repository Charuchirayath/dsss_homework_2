import unittest
from math_quiz import integer_generator, operator_generator, problem_generator


class TestMathGame(unittest.TestCase):
    
    # Test for integer_generator
    def test_integer_generator(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = integer_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    # Test for operator_generator
    def test_operator_generator(self):
        for _ in range(1000):
            oper = operator_generator()
            self.assertIn(oper, ['+', '-', '*'])
        pass

    def test_problem_generator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 3, '-', '4 - 3', 1),
                (7, 3, '*', '7 * 3', 21),
            ]

            for num1, num2, oper, expected_problem, expected_answer in test_cases:
                prob, ans = problem_generator(num1, num2, oper)
                self.assertEqual(prob, expected_problem)  
                self.assertEqual(ans, expected_answer)     
            pass

if __name__ == "__main__":
    unittest.main()