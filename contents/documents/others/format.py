ButtonClick = "../../code/view/ButtonClick.py"


with open(ButtonClick, "r", encoding="utf-8") as file:
    contents = file.read()

contents = contents.replace("from modules", "\n\n\n\nfrom modules")
contents = contents.replace("elif", "\n\n\n\n    elif")

with open(ButtonClick, "w", encoding="utf-8") as file:
    file.write(contents)
