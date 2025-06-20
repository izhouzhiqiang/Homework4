.PHONY: all env generate_env

generate_env:
	pip freeze > requirements.txt

env:
	pip install -r requirements.txt