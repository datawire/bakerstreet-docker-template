NAMESPACE = datawire
NAME = bakerstreet-hello
VERSION = 1

.PHONY: all build test tag_latest

all: build

build:
	docker build -t $(NAME):v$(VERSION) --rm image

test:
	env NAME=$(NAME) VERSION=v$(VERSION) ./test/runner.sh

tag_latest:
	docker tag -f $(NAME):v$(VERSION) $(NAME):latest