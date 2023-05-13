build:
    poetry run build

publish:
	poetry run publish

format:
	poetry run black .
	poetry run ruff . --fix

test:
	poetry run pytest --cov=python_html_dsl

coverage:
	poetry run coverage html

test-cov: test coverage
