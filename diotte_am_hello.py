# Amare Diotte
# 2024-RTT-107
# GLAB-340.1.1

# constant
AMARE_AGE = 37

# function containing hello world message
def greeting():
    # inputs saved to variables
    user_name = input("What's your name? ")
    user_age = int(input("How old are you? "))
    # conditionals
    if user_age == AMARE_AGE:
        print("Wow, " + user_name + ", we're the same age!")
    elif user_age > AMARE_AGE:
        print("Hi, " + user_name + ", you are " + str(user_age - AMARE_AGE) + " years older than me")
    else:
        print("Hi, " + user_name + ", you are " + str(AMARE_AGE - user_age) + " years younger than me")


greeting()