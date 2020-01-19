import argparse
from notion.client import NotionClient
from pprint import pprint


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument("--valid-types", default=["Blog"])
    args.add_argument("--token", default="")
    return args.parse_args()


class NotionAPI(object):
    TEXT_TYPES = ["header", "sub_header", "sub_sub_header", "text", "callout", "code"]
    EMPTY_TYPES = ["divider", "table_of_contents", "column_list"]
    SOURCE_TYPES = ["video", "image", "file", "audio", "pdf"]
    BOOKMARK_TYPES = ["bookmark"]

    def __init__(self, token):
        self.token = token
        self.client = NotionClient(token_v2=token)


    def get_table(self, url):
        return self.client.get_collection_view(url).default_query().execute()


    def process_page(self, row):
        page = []
        for child in row.children:
            
            content, e_type = "", child.type

            if e_type in self.SOURCE_TYPES:
                content = child.source
            elif e_type in self.TEXT_TYPES:
                content = child.title.strip()
            elif e_type in self.BOOKMARK_TYPES:
                content = {
                    "link": child.link, 
                    "title":child.title, 
                    "description":child.description
                }
            elif e_type in self.EMPTY_TYPES: 
                pass

            page.append({"type": e_type, "content": content})
        return page



if __name__ == "__main__":
    args = parse_args()
    token, url = args.token, args.url

    notion = NotionAPI(token)
    table = notion.get_table(url)

    pages = []
    for row in table:
        if row.page_type not in args.valid_types:
            continue
        pages.aappend(notion.process_page(row))

    for page in pages:
        pprint(page)