from notion.client import NotionClient


HUGO_TEMPLATE = """
---
title: "{title}"
date: {date}
link: "{link}"
---
{content}
"""


def get_table(client, url):
    cv = client.get_collection_view(url)
    result = cv.default_query().execute()
    return result


def table_to_markdown(table):
    last = ""
    idx = 0
    for row in table:
        content = ""
        for child in row.children:
            print(child.type)
            if child.type == "video":
                content += "{{{{< youtube id=\"{0}\" >}}}}<br>".format(child.source[-11:])
            elif child.type == "text":
                content += "{0}<br>\n".format(child.title)
            elif child.type == "header":
                content += "# {0}<br>".format(child.title)
            elif child.type == "embed":
                content += "{0}<br>".format(child.source)
            elif child.type == "bookmark":
                content += "<br>{{{{< customfig target=\"{link}\" class=\"notion-bookmark\" caption=\"{caption}\" title=\"{title}\" link=\"{link}\" src=\"{image}\" >}}}}".format(image=child.bookmark_cover, link=child.link, title=child.title, caption=child.description)
            elif child.type == "numbered_list":
                if last != "numbered_list":
                    idx = 0
                idx += 1
                text = child.title
                content += "{idx}. {text}<br>".format(idx=idx, text=text)
            else:
                pass
            last = child.type
        link = "{0}".format(row.url)
        yield (row.title, row.createdat, content, row.published, link)



if __name__ == "__main__":
    token = "d6b7981052765938534745a195e86076adfeea28135e224a54bfb72727c62da436473fe91e375e2659842a60da1afdd6707447c2b10a0173b97706c2468263a3b52e89e6cec9b7a809f23d9a61f9"
    client = NotionClient(token_v2=token)
    url = "https://www.notion.so/9bed5bc24bf546b59f371f6e9df3f233?v=832d68e629bb4fbb8c5c19e4c6dbfcc5"
     
    table = get_table(client, url)
    table = table_to_markdown(table)
    for row in table:
        published = row[3]
        if not published:
            continue
        title = row[0].replace("/", "-")
        date = row[1]
        content = row[2]
        url = row[4]
        with open("./bitwig-resources/content/posts/{name}.md".format(name=title), "w") as f:
            f.write(HUGO_TEMPLATE.format(title=title, date=date, content=content, link=url))


    
            

