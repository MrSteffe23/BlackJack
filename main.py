# --------------------- Our Blackjack House Rules ---------------------

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_computer(cards):
    score = calculate_score(cards)
    while score < 17:
        cards.append(random.choice(cards))
        score = calculate_score(cards)
    return cards, score


def verify_score(my_cards, computers_cards):
    my_score = calculate_score(my_cards)
    (computers_cards, computers_score) = calculate_computer(computers_cards)
    print(f"   Your final hand: {my_cards}, final score {my_score}")
    print(
        f"   Computer\'s final hand: {computers_cards}, final score: {computers_score}"
    )
    if my_score > 21:
        print("You went over. You lose :(\n\n")
    elif computers_score > 21:
        print("Opponent went over. You win. :)\n\n")
    elif my_score == computers_score:
        print("It's a draw!\n\n")
    elif my_score > computers_score:
        print("You win! :)\n\n")
    else:
        print("You lost! :(\n\n")


def calculate_score(cards):
    number_11 = cards.count(11)
    all_sum = sum(cards)
    sum_without_11 = all_sum - number_11 * 11
    sum_with_11_eq_1 = sum_without_11 + number_11
    if sum_with_11_eq_1 >= 21:
        return sum_with_11_eq_1
    final_sum = sum_with_11_eq_1
    for i in range(0, number_11):
        final_sum = final_sum - 1 + 11
        if final_sum > 21:
            return final_sum - 11 + 1
        elif final_sum == 21:
            return final_sum
    return final_sum


while True:
    black_jack = input(
        "Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if black_jack == 'y':
        print(logo)
        my_cards = [random.choice(cards), random.choice(cards)]
        computers_cards = [random.choice(cards), random.choice(cards)]
        while True:
            my_score = calculate_score(my_cards)
            print(f'   Your cards: {my_cards}, current score: {my_score}')
            print(f'   Computer\'s first card: {computers_cards[0]}')
            if len(my_cards) == 2 and sum(my_cards) == 21:
                print(f"BlackJack! :)))))))")
                break
            if my_score > 21:
                (computers_cards,
                 computers_score) = calculate_computer(computers_cards)
                print(
                    f"   Your final hand: {my_cards}, final score {my_score}")
                print(
                    f"   Computer\'s final hand: {computers_cards}, final score: {computers_score}"
                )
                print("You went over. You lose :(\n\n")
                break
            ask = input("Type 'y' to get another card, type 'n' to pass: ")
            if ask != 'y':
                verify_score(my_cards, computers_cards)
                break
            else:
                my_cards.append(random.choice(cards))
    else:
        break
