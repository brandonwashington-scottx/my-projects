print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old")

if age >= 18:
    print("You are old enough to play")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")

        left_or_right = input("First key decision.... Left or Right(left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Cool beans, you follow the road and reach a burning tree... "
                        "Do you walk left or walk right (left/right)? ")

            if ans == "right":
                ans = input("You are chased by a wild pack of wolves until you run out of breath and collapse due to fatigue GAME OVER!! ")

            elif ans == "left":
                ans = input("You follow a path that leads you to the forbidden fortune!...Congrats on finding the forbidden fortune ... YOU WIN!! ")

        if left_or_right == "right":
            ans = input("You fall down a tree trap and lose all of your health... GAME OVER!!")

    else:
        print("Cya...")
elif age >= 14:
    print("you can play with supervision")
else:
    print("You are not old enough to play...")




