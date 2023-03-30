import Utils
import os


def add_score():
    file_path = Utils.scores_file_name()
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            number = int(file.read())
    else:
        with open(file_path, 'w') as file:
            file.write("0")
        number = 0

    number += 1
    with open(file_path, 'w') as file:
        file.write(str(number))



