cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
cards2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def check_straight(card1, card2, card3):
    card1 = int(card1)
    card2 = int(card2)
    card3 = int(card3)
    if card1 < card2 < card3:
        return card3
    else:
        return 0


def check_3ofa_kind(card1, card2, card3):
    card1 = int(card1)
    card2 = int(card2)
    card3 = int(card3)
    if card1 == card2 == card3:
        return card3
    else:
        return 0


def check_royal_flush(card1, card2, card3):
    card1 = int(card1)
    card2 = int(card2)
    card3 = int(card3)
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


def play_cards(left1, left2, left3, right1, right2, right3):
    left1 = int(left1)
    left2 = int(left2)
    left3 = int(left3)
    right1 = int(right1)
    right2 = int(right2)
    right3 = int(right3)
    left = [left1, left2, left3]
    right = [right1, right2, right3]
    if left < right:
        if right1 < right2 < right3:
            return 1
        elif right1 == right2 == right3:
            return 1
        elif right == check_straight(right1, right2, right3) and left == check_3ofa_kind(left1, left2, left3):
            return 1
        elif right == check_royal_flush(right1, right2, right3) and left != check_royal_flush(left1, left2, left3):
            return 1
    elif left == right:
        return 0
    elif left > right:
        if left1 < left2 < left3:
            return -1
        elif left1 == left2 == left3:
            return -1
        elif left == check_straight(left1, left2, left3) and right == check_3ofa_kind(right1, right2, right3):
            return -1
        elif left == check_royal_flush(left1, left2, left3) and right != check_royal_flush(right1, right2, right3):
            return -1
