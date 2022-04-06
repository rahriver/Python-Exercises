from pyfiglet import Figlet
from termcolor import colored

# get input -> what text?
# get input -> what color?
# print the text with color
# have a default color in the function (default parameter)


def ascii_art(texts, selected_color='magenta'):
    f = Figlet(font='slant')
    print(colored(f.renderText(texts), color=selected_color))


def colored_text():
    colors = ('red', 'blue', 'cyan', 'green', 'yellow', 'white', 'magenta')
    while True:
        text = input('What text do you want to show?(q to quit): ')
        if text != '':
            if text == 'q':
                print("Have a great day!")
                break
            color = input('What color?: ').lower()
            if color == 'q':
                print("Have a great day!")
                break
            elif color not in colors:
                color = 'magenta'
            ascii_art(text, color)
        else:
            print("Enter a value!")


colored_text()
