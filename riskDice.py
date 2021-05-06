import random

# ARMIES AVAILABLE, DICE ALLOWED, DICE CHOICE 
def dice_number(x,y):
    z = [] # Attack options list, D-fence always defends with maximum dice available.
    if x >= 4:
        xd = 3
    else:
        xd = x - 1
    if y >= 3:
        yd = 3
    else:
        yd = y  
    for i in range(1, xd + 1):
        z.append(str(i))

    while z != []:
        print(f"Attack can roll up to {xd} die/dice, D-fence will roll {yd} die/dice.")
        selection = input(f"Select the number of dice you want to use (Options:{z}). To retreat enter \"R\": ")
        while selection not in z and selection != "r":
            selection = input(f"Select the number of dice you want to use (Options:{z}). To retreat enter \"R\": ")
        if selection in z:
            dice_number = int(selection), yd
            print(f"Attack rolls {dice_number[0]} dice, Defence rolls {dice_number[0]} dice. Results:")
            return dice_number
            break
        elif selection.lower() == "r":
            print("You retreated. Chicken!")
            break
        
# ROLL THE DICE

def dice_rolls(dice):
    xd, yd = dice
    a_rolls = 0
    a_score = []
    while a_rolls < xd:
        a_score.append(random.randint(1,6))
        a_rolls += 1
        a_score.sort(reverse = True)
    print(f"ATTACK ROLLS: {a_score}")

    d_rolls = 0
    d_score = []
    while d_rolls < yd:
        d_score.append(random.randint(1,6))
        d_rolls += 1
        d_score.sort(reverse = True)
    print(f"D-FENCE ROLLS: {d_score}")

    rolls = (a_score, d_score)
    return rolls


# COMPARE RESULTS AND ELIMINATE ARMIES 

def blood_bath(rolls):    
    a_score, d_score = rolls
    a_losses, d_losses = 0, 0
    if a_score[0] > d_score[0]:
        d_losses += 1
    else: 
        a_losses += 1
    if len(a_score) >=2 and len(d_score) >= 2:
        if a_score[1] > d_score[1]:
            d_losses += 1
        else: 
            a_losses += 1
    if len(a_score) == 3 and len(d_score) == 3:
        if a_score[2] > d_score[2]:
            d_losses += 1
        else: 
            a_losses += 1
    losses = a_losses, d_losses
    print(f"LOSSES: Attack {losses[0]} casualties, D-fence {losses[1]} casualties.")
    return losses


# MAIN TURN (ATTACK, RECALCULATE ARMIES, OUTCOME)

def turn(armies): # AS ARGUMENT PASS A TUPLE CONTAINING 2 INT
    x, y = armies
    print(f"Armies: Attack => {x}, D-fence => {y}.")
    violence = ""
    while violence.lower() != "y" or violence.lower() != "n":
        violence = input("Do you want to attack? Press \"Y\" for yes or \"N\" for no: ")
        if violence.lower() == "y":
            while x > 1 and y > 0:
                print(f"Armies: Attack => {x}, D-fence => {y}.")
                dice = dice_number(x,y)
                if dice == None:
                    break
                else:
                    rolls = dice_rolls(dice)
                    losses = blood_bath(rolls)
                    a_losses, d_losses = losses
                    x = x - a_losses
                    y = y - d_losses
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

turn((7,2))







