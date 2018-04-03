help:
	@echo "help:"
	@echo "  make lint	- check lint via flake8"
	@echo "  make test	- run test"

lint:
	flake8  ./*.py alloy tests scripts

test:
	./alo test $(args) ${target}
