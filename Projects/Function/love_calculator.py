# TODO: Love Calculator
# 💪 This is a difficult challenge! 💪
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.


def calculate_love_score(name1, name2):
    # varibale
    T = R = U = E = 0
    L = O = V = 0

    combined_name = name1 + name2
    lower_case_name =combined_name.lower()
    for char in lower_case_name:
        if char == "t" :
            T += 1
        elif char == "r" :
            R += 1
        elif char == "u":
            U += 1
        elif char == "e":
            E += 1
        elif char == "l":
            L += 1
        elif char == "o":
            O += 1
        elif char == "v":
            V += 1
        # elif char =="E" or char=="e":
        #     E +=1
    true_count = T + R + U + E
    love_count = L + O + V + E
    print(f"T occurs {T} times")
    print(f"R occurs {R} times")
    print(f"U occurs {U} times")
    print(f"E occurs {E} times")

    print(f"Total= {true_count}")

    print(f"L occurs {L} times")
    print(f"O occurs {O} times")
    print(f"V occurs {V} times")
    print(f"E occurs {E} times")

    print(f"Total= {love_count}")
    print(f"Love Score = {true_count}{love_count}")


# Call your function with hard coded values
calculate_love_score("Belete", "Tekalign")



#Solutions:

# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
#
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
#
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
#
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")