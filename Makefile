
# Default target executed when no arguments are given to make.
all: help

lint:
	hatch fmt --check

format:
	hatch fmt

test:
	hatch test

wheel:
	hatch build

clean:
	hatch clean

######################
# HELP
######################

help:
	@echo '----'
	@echo 'lint                         - run linters'
	@echo 'format                       - run code formatters'
	@echo 'test                         - run unit tests'
	@echo 'wheel                        - build wheel package'
	@echo 'clean                        - clean up'