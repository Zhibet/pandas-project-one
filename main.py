import pandas as pd

df = pd.read_csv('50_states.csv')
states = df['state']

with open('collected.txt') as file:
    content = file.read()
    print(content)

collected_states = []

def entered_letter():
    user_letter = str(input('Enter A Letter: '))
    return user_letter.lower()

def logic():
    chosen_letter = entered_letter()
    for state in states:
        if state[0].lower() == chosen_letter:
            collected_states.append(state)

    with open('collected.txt', mode='a') as file:
        amount_of_matches = len(collected_states)
        string_amount = f"'\n'{amount_of_matches}, {collected_states}"
        print(string_amount)
        file.write(string_amount)

def game():
    game_on = True
    while game_on:
        question = str(input('Do you want to play a game "yes" or "no" ?: ')).lower()
        if question == 'yes':
            logic()
        else:
            game_on = False

# Start the game
game()
