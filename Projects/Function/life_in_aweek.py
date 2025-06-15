# TODO: Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
       #It will take your current age as the input and output a message with our time left in this format:
def life_in_weeks(expected_year_to_live,current_age):
    week_in_year= 52
    year_left = expected_year_to_live - current_age
    week_left = year_left *week_in_year
    print(f"You have {week_left} weeks left.")



life_in_weeks(90,39)