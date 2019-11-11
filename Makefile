.PHONY: env

# Python virtual environment

env:
	rm -rf .env
	virtualenv -p `which python 3.6` .env
	( \
		. ./.env/bin/activate; \
		pip install -r requirements.txt; \
	)