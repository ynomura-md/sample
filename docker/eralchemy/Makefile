.DEFAULT_GOAL := help

TAG = 0.1
PREFIX = pa-1/eralchemy

CONTAINER_NAME = $(shell echo $(PREFIX) | sed -e 's/\//_/')

PORT=5432

DEFAULT_NET  = bridge
DOCKER_NETWORK ?= $(DEFAULT_NET)

LINK = --link pa-1_postgresql:db

build: ## Build docker image
	docker build -t $(PREFIX):$(TAG) .

#run: build ## Run at local (use openstack presto)

debug:
	docker run --rm -it \
		-e "PRESTO_HOST=presto.ssp.devel.scaleout.jp" \
		-e "PRESTO_PORT=80" \
		-e "DB_HOST=azs-dev-db" \
		-e "DB_PORT=9999" \
		-e "DB_NAME=azs" \
		-e "DB_USER=azs" \
		-e "DB_PASSWORD=test" \
		--net=$(DOCKER_NETWORK) $(LINK) $(PREFIX):$(TAG) \
		sh
help: ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

