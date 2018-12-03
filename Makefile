.PHONY: all help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# install
settings:
	@cd src && python3.6 -m scripts.generate_secret -a default

# run
runserver:
	@python3.6 src/manage.py runserver

# test
test:
	@python3.6 src/manage.py test src --noinput
