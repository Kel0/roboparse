# roboparse

Simple utility which helps to organize code of your scraper.

# Example
Go to the `example` directory.

## Installation
* **Via pip**
```shell
pip install roboparse
```

* **Via git** 
```shell
git clone https://github.com/Toffooo/roboparse.git
cd roboparse
pip install -e .
```

## Routers
You have 2 options when you create routers.
1. Make one and big router for all features that you need
2. Divide it to small parts

* **Big router**
```python
from roboparse import BaseRouter
from roboparse.schemas import RouterResponse


class BlogSiteRouter(BaseRouter):
    def get_posts(self) -> RouterResponse:    
        response = self.create_router_response(
            path="<site_url>",  # Path is just meta data. It uses for nothing
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
    
    def get_main(self) -> RouterResponse:
        response = self.create_router_response_from_json(
            path="json_file.json"
        )
        return response

    def _fb_exclude_none_blocks(self, data):
        return [element for element in data if element is not None]
```
* **Small router**
```python
from roboparse import BaseRouter
from roboparse.schemas import RouterResponse


class BlogFilters:
    def _fb_exclude_none_blocks(self, data):
        return [element for element in data if element is not None]


class BlogMainRouter(BaseRouter, BlogFilters):
    def get(self) -> RouterResponse:
        response = self.create_router_response_from_json(
            path="json_file.json"
        )
        return response


class BlogPostRouter(BaseRouter, BlogFilters):
    def get(self) -> RouterResponse:    
        response = self.create_router_response(
            path="<site_url>",  # Path is just meta data. It uses for nothing
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

Explanation:
1. `create_router_response` - Every method of router should return router response as following, this responses will be provided to parser, and handled by it \
   a) `path` - Meta about url of page \
   b) `linter` - You have to provide there hierarchy of html elements
2. `create_router_responsefrom_json` - Same as `create_router_response`, provide json file's path and load your linter's schema from it. Json structure should be same
3. `_fb prefix` - You can register filters for your router. In this example, I've declared the filter by adding to method name `_fb` prefix.
This will register your method in the class as filter. My filter just removes None elements from list and returning handled data.
   
See code example at `example/scraper.py`
