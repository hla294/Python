import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A States Game !")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What is another state's name?").title()
    print(answer_state)

    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        #if they got it right:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
            #Create a turtle to write the name of the state at the state's corx and cory

screen.exitonclick()
