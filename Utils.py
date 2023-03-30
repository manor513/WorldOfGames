import time
import os


def scores_file_name():
    scores_file_path = 'C:/Users/manor/Desktop/Python/WorldOfGames/Scores.txt'
    return scores_file_path


def bad_return_code():
    bad_return_number = '400'
    return bad_return_number


def screen_cleaner():
    time.sleep(0.7)
    os.system("cls" if os.name == "nt" else "clear")



