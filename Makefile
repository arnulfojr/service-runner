# Load .env file if existing
-include .env
export

VERBOSE=1

local:
	ln -sfv conf/docker-compose.local.yml docker-compose.override.yml
	docker-compose config
.PHONY: local

clone:
.PHONY: clone
