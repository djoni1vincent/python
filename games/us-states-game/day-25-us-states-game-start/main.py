import turtle
import pandas as pd
from guessed_turtle import Guessed

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
s_turtle = turtle.Turtle(visible=False)
s_turtle.penup()
s_turtle.goto(0, 300)

data = pd.read_csv("50_states.csv")

states = [state for state in data["state"]]
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state",
                                    prompt="What's another state's name?")

    if answer_state is None:
        missing_states = [state for state in states if state not in guessed_states]

        with open("states_to_remember.txt", 'w') as file:
            for state in missing_states:
                file.write(f"{state}\n")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        guessed = Guessed(state_data.x.item(), state_data.y.item(), answer_state)
        s_turtle.clear()
        s_turtle.write(f"Guessed states: {len(guessed_states)}/50")

turtle.mainloop()
