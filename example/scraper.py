import csv
from contextlib import contextmanager

import requests

from roboparse import Parser, BaseRouter


class HabrRouter(BaseRouter):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @contextmanager
    def login(self):
        """
        Implement there login functionality
        """

    def get_news(self):
        """
        Create router response and return it
        """
        response = self.create_router_response(
            path="https://habr.com/ru/",  # Path is just meta data. It uses for nothing
            linter={
                "type": "LIST",
                "tag": "li",
                "attrs": {"class": "content-list__item"},
                "children": {
                    "type": "ELEMENT",
                    "tag": "h2",
                    "attrs": {"class": "post__title"},
                    "children": {
                        "type": "ELEMENT",
                        "tag": "a",
                        "attrs": {"class": "post__title_link"}
                    }
                }
            }
        )
        return response


def write_csv(data):
    with open("news.csv", "a+") as f:
        writer = csv.writer(f)
        writer.writerow(("Title", "Link"))

        for item in data:
            writer.writerow(
                (item.text.strip(), item.get("href"))
            )


def scrape_news():
    parser = Parser()
    router = HabrRouter(username="someUserName", password="somePassWord")

    with requests.Session() as session:
        html = session.get("https://habr.com/ru/", headers={
            "accept": "*/*",
            "user-agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/86.0.4240.111 Safari/537.36"
            )
        })
        print(html.text)
        data = parser.load(html.content, router.get_news())
        data = [element for element in data if element is not None]  # Removing unnecessary elements
        write_csv(data)


if __name__ == '__main__':
    scrape_news()
