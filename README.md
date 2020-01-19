# Notion something

This is a basic ass library for turning a notion table into a simple json structure. 


# Usage  

`make build run`  

# Example  

```json
POST http://localhost:8888/api/table

{
	"token": "<token from dev tools while logged into notion on>",
	"url": "<notion url to table>",
	"valid_types": ["Blog", "Music"]
}

```

The return structure is the notion id, title of the notion page and a content array containing objects with a type field denoting the notion type (mapping name determined by the notion python library) and the content of that block as a plain string.

```json
[
    {
        "id": "cf0ca612-ff3b-4f40-8f51-f2a5efb913b9",
        "title": "Bureaucracy isn't a bad word",
        "content": []
    },
    {
        "id": "1c031997-53db-4e0b-9ee3-c6b53ffdd46d",
        "title": "Spice/XPRA/Xephyr",
        "content": [
            {
                "type": "table_of_contents",
                "content": ""
            },
            {
                "type": "header",
                "content": "Xephyr"
            },

```