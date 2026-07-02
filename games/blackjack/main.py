import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card():
    return random.choice(cards)

def toose(cards):
    score = sum(cards)
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score


u_cards = [random_card(), random_card()]
c_cards = [random_card()]

start_cards = (random.choices(cards, k=2))

current_score = toose(u_cards)
computer_score = toose(c_cards)
print(art.logo)

ask_to_play = input("Start playing?\n y, n:")

if ask_to_play == "y":
    print(f"your cards: {u_cards}, current score: {current_score}")
    print(f"Computer's first card: {c_cards}")

    while current_score <= 21:
        continue_play = input(f"Type 'y' to get another card, type 'n' to pass: ")

        if continue_play == "y":
            u_cards.append(random_card())
            current_score = toose(u_cards)

            print(f"your cards: {u_cards}, current score: {current_score}")
            print(f"Computer's cards: {c_cards}")

            if current_score > 21:
                print("You went over, GIVE ME MY MONEY, BEACH")
                break


        if continue_play == "n":
            while computer_score <= 16:
                c_cards.append(random_card())
                computer_score = toose(c_cards)

            print(f"your final cards: {u_cards}, final score: {current_score}")
            print(f"Computer's final cards: {c_cards}, final score: {computer_score}")
            break

    if computer_score > 21:
        print("You win! 😁")
    if current_score < computer_score and computer_score <= 21:
        print("You lose 😮‍")
    elif current_score > computer_score and current_score <= 21:
        print("You win! 😁")
    else:
      print("Tie")
