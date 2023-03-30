from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(app_url):
    driver = webdriver.Chrome()
    driver.get(app_url)

    score_element = driver.find_element(By.ID, "score")
    score_text = score_element.text

    score = int(score_text)
    if score >= 1 and score <= 1000:
        return True
    else:
        return False


def main_function():
    try:
        test_scores_service('http://127.0.0.1:5000/')
        if test_scores_service('http://127.0.0.1:5000/'):
            return 0
        else:
            return -1

    except Exception:
        return -1


print(main_function())
