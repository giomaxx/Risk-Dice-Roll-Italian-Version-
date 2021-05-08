import random

# AVAILABLE ARMIES, ALLOWED DICE, DICE CHOICE

def dice_number(x, y: int) -> tuple:
    # z = Attack options list, D-fence always defends with maximum dice available.
    if x >= 4:
        option_dice = 3
        z = [str(i) for i in range(1, 4)]
    else:
        option_dice = x - 1
        z = [str(i) for i in range(1, x)]
    if y >= 3:
        d_dice = 3
    else:
        d_dice = y

    while z != []:
        print(
            f"Attack can roll up to {option_dice} die/dice, D-fence will roll {d_dice} die/dice.")
        selection = input(
            f"Select the number of dice you want to use (Options:{z}). To retreat enter \"R\": ")
        while selection not in z and selection != "r":
            selection = input(
                f"Select the number of dice you want to use (Options:{z}). To retreat enter \"R\": ")
        if selection in z:
            print(f"Attack rolls {int(selection)} dice, Defence rolls {d_dice} dice. Results:")
            return (int(selection), d_dice)
            break
        elif selection.lower() == "r":
            print("You retreated. Chicken!")
            break


# ROLL THE DICE

def dice_rolls(dice: tuple) -> tuple:
    a_dice, d_dice = dice
    a_rolls = 0
    a_score = []
    while a_rolls < dice[0]:
        a_score.append(random.randint(1, 6))
        a_rolls += 1
    a_score.sort(reverse=True)
    print(f"ATTACK ROLLS: {a_score}")

    d_rolls = 0
    d_score = []
    while d_rolls < dice[1]:
        d_score.append(random.randint(1, 6))
        d_rolls += 1
    d_score.sort(reverse=True)
    print(f"D-FENCE ROLLS: {d_score}")
    print(a_score, d_score)
    return (a_score, d_score)


# COMPARE RESULTS AND ELIMINATE ARMIES

def blood_bath(rolls: tuple) -> tuple:
    a_losses, d_losses = 0, 0
    if rolls[0][0] > rolls[1][0]:
        d_losses += 1
    else:
        a_losses += 1
    if len(rolls[0]) >= 2 and len(rolls[1]) >= 2:
        if rolls[0][1] > rolls[1][1]:
            d_losses += 1
        else:
            a_losses += 1
    if len(rolls[0]) == 3 and len(rolls[1]) == 3:
        if rolls[0][2] > rolls[1][2]:
            d_losses += 1
        else:
            a_losses += 1
    losses = a_losses, d_losses
    print(f"LOSSES: Attack {losses[0]} casualties, D-fence {losses[1]} casualties.")
    return losses


# MAIN TURN (ATTACK, RECALCULATE ARMIES, OUTCOME)

def turn(armies: tuple):  
    x, y = armies
    print(f"Armies: Attack => {x}, D-fence => {y}.")
    violence = ""
    while violence.lower() != "y" or violence.lower() != "n":
        violence = input(
            "Do you want to attack? Press \"Y\" for yes or \"N\" for no: ")
        if violence.lower() == "y":
            while x > 1 and y > 0:
                print(f"Armies: Attack => {x}, D-fence => {y}.")
                dice = dice_number(x, y)
                if dice == None:
                    break
                else:
                    rolls = dice_rolls(dice)
                    losses = blood_bath(rolls)
                    x = x - losses[0]
                    y = y - losses[1]
            if x == 1:
                print(f"Remaining armies: Attack => {x}, D-fence => {y}.")
                print("You were defeated!")
                break
            elif y == 0:
                print(f"Remaining armies: Attack => {x}, D-fence => {y}.")
                print("Congratulations, you conquered the territory!")
                break

        elif violence.lower() == "n":
            print("You surrendered. Chicken!")
            break

turn((7, 4))







