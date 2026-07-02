import pandas as pd

data = pd.read_csv("data_squirls.csv")

gray = 0
cinnamon = 0
black = 0

for color in data["Primary Fur Color"]:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1

colors_dict = {
    "gray": [gray],
    "cinnamon": [cinnamon],
    "black": [black],
}

colors = pd.DataFrame(colors_dict)
colors.to_csv("squirel_colors.csv", index=False)

print(colors)
