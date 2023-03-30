from flask import Flask
from Utils import scores_file_name, bad_return_code
import os

app = Flask(__name__)


@app.route('/')
def score_server():
    file_path = scores_file_name()
    if os.path.exists(file_path):
        with open(file_path, 'r+') as f:
            score_value = f.read()
        html = """
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is: <div id="score">{}</div></h1>
                </body>
            </html>
        """.format(score_value)
    else:
        error_number = bad_return_code()
        html = """
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>Error<div id="score" style="color:red">{}</div></h1>
                </body>
            </html>
        """.format(error_number)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0')

