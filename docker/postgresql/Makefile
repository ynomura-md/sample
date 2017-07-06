.DEFAULT_GOAL := help

TAG = 0.1
PREFIX = pa-1/postgresql

CONTAINER_NAME = $(shell echo $(PREFIX) | sed -e 's/\//_/')

PORT=5432

RUN_NET = host
RUN_NET = ${DOCKER_NETWORK}

build: ## Build docker image
	docker build -t $(PREFIX):$(TAG) .

daemon:
	docker run -d -p $(PORT):5432 --name $(CONTAINER_NAME) $(PREFIX):$(TAG)

help: ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

