import unittest
import PokerSpadesGame


class MyTestCase(unittest.TestCase):
    def test_check_straight(self):
        self.assertEqual(PokerSpadesGame.check_straight(2, 3, 4), 4)  # add assertion here

    def test_check_straight2(self):
        self.assertEqual(PokerSpadesGame.check_straight(2, 14, 6), 0)

    def test_3ofakind(self):
        self.assertEqual(PokerSpadesGame.check_3ofa_kind(13, 13, 13), 13)

    def test_3ofakind2(self):
        self.assertEqual(PokerSpadesGame.check_3ofa_kind(7, 10, 8), 0)

    def test_royal_flush(self):
        self.assertEqual(PokerSpadesGame.check_royal_flush(12, 13, 14), 14)

    def test_royal_flush2(self):
        self.assertEqual(PokerSpadesGame.check_royal_flush(2, 11, 5), 0)

    def test_royal_flush3(self):
        self.assertEqual(PokerSpadesGame.check_royal_flush(6, 7, 8), 0)

    def test_play_cards(self):
        self.assertEqual(PokerSpadesGame.play_cards(9, 9, 9, 10, 10, 10), 1)

    def test_play_cards2(self):
        self.assertEqual(PokerSpadesGame.play_cards(12, 12, 12, 12, 12, 12), 0)

    def test_play_cards3(self):
        self.assertEqual(PokerSpadesGame.play_cards(4, 5, 6, 2, 2, 2), -1)

    def test_play_cards4(self):
        self.assertEqual(PokerSpadesGame.play_cards(6, 7, 8, 9, 10, 11), 1)

    def test_play_cards5(self):
        self.assertEqual(PokerSpadesGame.play_cards(11, 12, 13, 11, 12, 13), 0)

    def test_play_cards6(self):
        self.assertEqual(PokerSpadesGame.play_cards(12, 13, 14, 6, 7, 2), -1)


if __name__ == '__main__':
    unittest.main()
