import turtle
import pandas
from state_names import StateName

screen = turtle.Screen()
screen.setup(width=770, height=770)
screen.title("United States: Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

stating = StateName()

states_data = pandas.read_csv("50_states.csv")
state_name = states_data["state"].tolist()
state_dict = states_data.to_dict()

state_list = []

more_states = 0
while more_states < 50:
    user_answer = screen.textinput(f"{more_states}/50 States", "Enter a State name: ").title()

    if user_answer not in state_list:           # check first
        if user_answer in state_name:
            for i, name in state_dict["state"].items():
                if name == user_answer:
                    state_x = state_dict["x"][i]
                    state_y = state_dict["y"][i]
            stating.place_state(state_x, state_y)
            stating.write_state(user_answer)
            state_list.append(user_answer)      # then record it
            more_states += 1
    else:
        continue
    if more_states == 50:
        stating.game_over()



screen.exitonclick()