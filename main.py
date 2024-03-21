from turtle import Turtle, Screen
from text import Text
import pandas as pd

FONT = ("Courier", 8, "normal")
IMAGE = 'blank_states_img.gif'

def main():
    screen = Screen()
    screen.clear()
    screen.title("U.S States Game")
    screen.addshape(IMAGE)
    Turtle().shape(IMAGE)

    data = pd.read_csv('50_states.csv')

    states = data['state'].to_list()

    while len(states) > 0:
        answer = screen.textinput(title=f"{len(states)} remaining", prompt="What's another state's name?").title()
        if answer in states:
            text = Text()
            text.update_text(x=data['x'][data['state'] == answer].iloc[0], y=data['y'][data['state'] == answer].iloc[0], state=answer)
            states.remove(answer)

    game_over_text = Text()
    game_over_text.game_over()

    screen.listen()
    screen.onkey(main, "r")

    screen.exitonclick()


if __name__ == "__main__":
    main()