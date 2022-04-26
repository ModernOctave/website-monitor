import requests
from bs4 import BeautifulSoup
from utils import *
import json

class moniter:

    def __init__(self, url, name) -> None:
        self.url = url
        self.name = name
        self.dirname = os.path.dirname(__file__)

    def get_text(self) -> str:
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, "lxml")
        return soup.get_text()

    def is_changed(self, text) -> bool:
        try:
            with open(relpath("prev_texts.json"), "r") as f:
                try:
                    prev_texts = json.load(f)
                except:
                    prev_texts = {}
                try:
                    old_text = prev_texts[self.name]
                except:
                    old_text = ""
        except FileNotFoundError:
            old_text = ""
        
        if text != old_text:
            print("Changed!")
                
            try:
                with open(relpath("prev_texts.json"), "w") as f:
                    prev_texts[self.name] = text
                    f.write(json.dumps(prev_texts))
            except:
                raise Exception("Could not write to prev_texts.json!")
            return True
        else:
            return False

    def check_for_update(self) -> None:
        text = self.get_text()
        if self.is_changed(text):
            html_msg = f"""\
                <html>
                    <body>
                        <p>Go to the <a href="{self.url}">page</a>.</p>
                    </body>
                </html>
            """
            send_email(f"{self.name} has changed!", html_msg)

if __name__ == '__main__':
    with open(relpath("jobs.json"), "r") as f:
        jobs = json.load(f)
    for job in jobs:
        moniter(job["url"], job["name"]).check_for_update()