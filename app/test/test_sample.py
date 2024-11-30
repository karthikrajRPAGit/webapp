# content of test_sample.py
import requests
def func():
    resp=requests.get("https://appaccount2306.azurewebsites.net/")
    print(resp.text)
    if "Hello World" in resp.text:
        return True
    else:
        return False


def test_answer():
    assert func() == True