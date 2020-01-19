name=notionpy
token="<get your notion token from dev tools>"
port=8888

build:
	docker build --rm -t $(name) .

run:
	docker run -p $(port):$(port) -it $(name)