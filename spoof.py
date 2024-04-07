import random

num_dealers = 5

print("Welcome to Spoof! Each round every player will hold 1, 2 or 3 coins. Try to guess how many coins there are in total - \nbut there are no repeating guesses allowed! The winner gets to leave.")
while num_dealers > 1:
    dealers_hands = [random.randint(1, 3) for i in range(0, num_dealers)]
    player_hand = int(input("\nPick a number from 1 to 3: "))
    while player_hand > 3 or player_hand < 1:
      player_hand = int(input("Pick a number from 1 to 3: "))
    target = player_hand + sum(dealers_hands)
    guesses = []
    players = 1 + len(dealers_hands)
    counter = 1
    for pick in dealers_hands:
        max_guess = pick + 3 * num_dealers
        guess = random.randint(pick + num_dealers, max_guess)
        while guess in guesses:
            guess = random.randint(pick + num_dealers, max_guess)
        guesses.append(guess)
        print("\nPlayer " + str(counter) + ": I guess there are " + str(guess) + " coins in total.")
        counter += 1
    print("Your minimum recommended guess is: " + str(player_hand + num_dealers))
    print("Your maximum recommended guess is: " + str(player_hand + 3 * num_dealers))
    player_guess = int(input("\nPick a number that nobody has guessed yet: "))
    while player_guess in guesses:
        player_guess = int(input("Pick a number that nobody has guessed yet: "))
    guesses.append(player_guess)
    if guesses[-1] == target:
        num_dealers = 0
        print("You win!")
    elif target in guesses:
        num_dealers -= 1
        print("Somebody else guessed it.")
        if num_dealers == 1:
          print("You lose!")
    else:
        print("Nobody guessed it.")
