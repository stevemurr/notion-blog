import argparse
import falcon
import waitress
import notion_api


def parse_args():
    args = argparse.ArgumentParser()

    args.add_argument("--port", default=8888)

    return args.parse_args()


class NotionResource(object):
    
    def on_post(self, req, res):
        payload = req.media
        token, url, valid_types = payload["token"], payload["url"], payload["valid_types"]
        notion = notion_api.NotionAPI(token)
        table = notion.get_table(url)
        
        pages = []
        for row in table:
            rrow = {"id": row.id, "title": row.title, "content": {}} 
            if row.page_type not in valid_types:
                continue
            rrow["content"] = notion.process_page(row)
            pages.append(rrow)

        res.status_code = falcon.HTTP_200
        res.content_type = "application/json"
        res.media = pages


if __name__ == "__main__":
    api = falcon.API()
    notion_resource = NotionResource()
    api.add_route("/api/table", notion_resource)
    waitress.serve(api, host="0.0.0.0", port=args.port)