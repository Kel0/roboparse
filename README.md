# roboparse

Simple utility which helps to organize code of your scraper.

# Example
Go to the `example` directory.

## Installation
* **Via pip**
```shell
pip install roboparser
```

* **Via git** 
```shell
git clone https://github.com/Toffooo/roboparse.git
cd roboparse
pip install -e .
```

## Usage
* **Structure of project**

You can create `router` for whole web service if you have a small scraper.
Or you can divide it to small routers.
  
routers.py
```python
from roboparse import BaseRouter


class HabrRouterNews(BaseRouter):  # Small router for every feature
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def filter_data(self, data):
        """Filter/sort your data"""
        
    def get(self):
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


class HabrRouter(BaseRouter):  # One router for whole web service
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

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
```

main.py
```python
import requests
from roboparse import Parser

from .routers import HabrRouter, HabrRouterNews

parser: Parser = Parser()


def scrape_news1():
    router = HabrRouterNews(username="username", password="password")
    
    with requests.Session() as session:
        html = session.get("url")
        data = parser.load(html, router.get())
        sorted_data = router.filter_data(data)
        print(sorted_data)

        
def scrape_news2():
    router = HabrRouter(username="username", password="password")
    
    with requests.Session() as session:
        html = session.get("url")
        data = parser.load(html, router.get_news())
        print(data)
```
