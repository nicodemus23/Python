import random

events = [
    ("the start of the Revolutionary War", 1775),
    ("the United States Constitution signed", 1783),
    ("President Lincoln assassinated", 1865),
    ("Theodore Roosevelt's first day in office as President of the United States", 1901),
    ("the beginning of World War II", 1939),
    ("the first personal computer introduced", 1975),
    ("the Berlin Wall taken down", 1989),
    ("the first moon landing", 1969),
    ("the signing of the Declaration of Independence", 1776),
    ("the end of World War I", 1918)
]

random.shuffle(events)

score = 0

for event, year in events:
    question = f"In what year did {event} occur? "
    
    try:
        guess = int(input(question))
        
        if guess == year:
            print("Exactly right! 10 points!")
            score += 10
        elif abs(guess - year) <= 5:
            score += 5
            print(f"Close! The correct answer is {year}. You earn 5 points.")
        elif abs(guess - year) <= 10:
            score += 2
            print(f"The correct answer is {year}. You earn 2 points.")
        elif abs(guess - year) <= 20:
            score += 1
            print(f"The correct answer is {year}. You earn 1 point.")
        else:
            print(f"The correct answer is {year}. You don't earn any points.")
            
        print(f"Your score is {score} points.")
        
    except ValueError:
        print("You must enter a valid year(int).")
        break
    
print(f"\nYour final score is {score} points out of {len(events) * 10}.")

if score >= len(events) * 8:
    print("Yeah, boyeeee!! You know your history.")
elif score >= len(events) * 6:
    print("Nice! You have a solid understanding of historical events.")
elif score >= len(events) * 4:
    print("Not bad!.")
else:
    print("History ain't your thang, eh?")

