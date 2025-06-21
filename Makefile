.PHONY: all env generate_env

env:
	pip3 install -r requirements_mac.txt

generate_env:
	pip3 freeze > requirements_mac.txt

all:
	echo "use `make env` to install python package"
