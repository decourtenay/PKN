import random

legal_choices = ["p","k","n"]
yes_choices = ["t","T","y","Y","tak","yes"]
no_choices = ["n","N","nie","no"]
legal_cont_choices = yes_choices + no_choices


def get_player_choice():
    player_choice = input("Co wybierasz: papier (p), kamień (k) czy nożyce (n)? ")
    return player_choice


def continue_after_error():
    cont_answer = input("Nie zrozumiałem. Czy chcesz spróbować jeszcze raz? ")
    if cont_answer not in legal_cont_choices:
        print("Niestety, nie rozumiem. Do widzenia! ")
        exit()
    elif cont_answer in no_choices:
        print("OK! Do widzenia! ")
        exit()
    else:
        player_choice = get_player_choice()
    return player_choice


def get_verified_player_choice():
    player_choice = get_player_choice()
    while player_choice not in legal_choices:
        player_choice = continue_after_error()
    if player_choice == "p":
        player_choice = "PAPIER"
    elif player_choice == "k":
        player_choice = "KAMIEŃ"
    elif player_choice == "n":
        player_choice = "NOŻYCE"
    return player_choice


def get_computer_choice():
    computer_choice_num = random.randint(1,3)
    if computer_choice_num == 1:
        computer_choice = "PAPIER"
    elif computer_choice_num == 2:
        computer_choice = "KAMIEŃ"
    else:
        computer_choice = "NOŻYCE"
    return computer_choice


def compare_choices():
    player_choice = get_verified_player_choice()
    computer_choice = get_computer_choice()
    if player_choice == computer_choice:
        print(f"I ty i komputer wybraliście {player_choice}")
        return 0
    else:
        print(f"Ty wybrałeś {player_choice}, a komputer wybrał {computer_choice}")
        if player_choice == "PAPIER":
            if computer_choice == "KAMIEŃ":
                return 1
            elif computer_choice == "NOŻYCE":
                return -1
        elif player_choice == "KAMIEŃ":
            if computer_choice == "NOŻYCE":
                return 1
            elif computer_choice == "PAPIER":
                return -1
        elif player_choice == "NOŻYCE":
            if computer_choice == "PAPIER":
                return 1
            elif computer_choice == "KAMIEŃ":
                return -1


def update_score(result, computer_score, player_score):
    if result > 0:
        player_score = player_score + result
        print("Wygrałeś!")
    elif result < 0:
        computer_score = computer_score - result
        print("Komputer wygrał!")
    else:
        print("Remis!")
    print(f"Obecny wynik to ty {player_score}, komputer {computer_score}")
    return computer_score, player_score


player_score = 0
computer_score = 0
result = compare_choices()
computer_score, player_score = update_score(result, computer_score, player_score)
while input("Czy chcesz kontynuować? ") in yes_choices:
    result = compare_choices()
    computer_score, player_score = update_score(result, computer_score, player_score)
else:
    print(f"OK! Do widzenia!")













