import unittest
from rock_paper import determine_winner, play_again  # Import the refactored functions

class TestRockPaperScissors(unittest.TestCase):
    def test_determine_winner(self):
        # Test for ties
        self.assertEqual(determine_winner("rock", "rock"), "Tie")
        self.assertEqual(determine_winner("paper", "paper"), "Tie")
        self.assertEqual(determine_winner("scissors", "scissors"), "Tie")

        # Test for player wins
        self.assertEqual(determine_winner("rock", "scissors"), "Win")
        self.assertEqual(determine_winner("scissors", "paper"), "Win")
        self.assertEqual(determine_winner("paper", "rock"), "Win")

        # Test for player loses
        self.assertEqual(determine_winner("rock", "paper"), "Lose")
        self.assertEqual(determine_winner("scissors", "rock"), "Lose")
        self.assertEqual(determine_winner("paper", "scissors"), "Lose")

    def test_play_again(self):
        # Test for continuing the game
        self.assertTrue(play_again("yes"))
        # Test for exiting the game
        self.assertFalse(play_again("no"))

if __name__ == "__main__":
    unittest.main()
