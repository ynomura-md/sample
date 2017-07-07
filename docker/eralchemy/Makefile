.DEFAULT_GOAL := help

TAG = 0.1
PREFIX = pa-1/eralchemy

CONTAINER_NAME = $(shell echo $(PREFIX) | sed -e 's/\//_/')

PORT=5432

DEFAULT_NET  = bridge
DOCKER_NETWORK ?= $(DEFAULT_NET)

LINK = --link pa-1_postgresql:pa1-db

VOLUME = -v $(PWD)/tmp:/usr/src/app/eralchemy

build: ## Build docker image
	docker build -t $(PREFIX):$(TAG) .

#run: build ## Run at local (use openstack presto)

debug:
	docker run --rm -it \
		-e "DB_HOST=pa1-db" \
		-e "DB_PORT=5432" \
		-e "DB_NAME=pa1" \
		-e "DB_USER=pa1" \
		-e "DB_PASSWORD=test" \
		--net=$(DOCKER_NETWORK) $(LINK) $(VOLUME) $(PREFIX):$(TAG) \
		sh

run: build
	docker run --rm -it \
		-e "DB_HOST=pa1-db" \
		-e "DB_PORT=5432" \
		-e "DB_NAME=pa1" \
		-e "DB_USER=pa1" \
		-e "DB_PASSWORD=test" \
		--net=$(DOCKER_NETWORK) $(LINK) $(VOLUME) $(PREFIX):$(TAG) \
		python main.py

clean:
	@rm -rf $(PWD)/tmp/*

help: ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

