import random
rounds = 1

die1 =  random.randint(1, 6)
die2 =  random.randint(1, 6)
die3 =  random.randint(1, 6)
dice = [die1, die2, die3]

while rounds <= 6:
    print("Round " + str(rounds))
    print("Sum of numbers on die = " + str(dice[0] + dice[1] + dice[2]))
    
    if rounds%2 == 0:
        look_at = input("Choose a die to look at: ")
        print("Die " + str(look_at[0]) + " = " + str(dice[int(look_at[0]) - 1]))
        
    answer = input("Choose which dice to keep of 1, 2, and 3 \nFor example, to keep dice 1 and 3, answer 1 3 or 13: ")
    answer = [int(a) for a in list(answer.strip())]
    temp = [None, None, None]
    while len(answer) > 0:
        temp[answer[0] - 1] = dice[answer[0] - 1]
        answer = answer[1:]
    for i in range(len(dice)):
        if temp[i] == None:
            temp[i] = random.randint(1, 6)
    dice = temp
    rounds += 1

if dice[0] == dice[1] == dice[2] == 6:
    print("You win!")
else:
    print("You lose :(")
    print(dice)