FROM python:3.9-slim
COPY MainScores.py /MainScores.py
COPY Utils.py /Utils.py
COPY Scores.txt /Scores.txt
RUN pip install flask
CMD ["python", "MainScores.py"]

