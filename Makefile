pip.install:
	pip install -r requirements.txt

run:
	python runner.py

config.env:
	cp .env.sample .env