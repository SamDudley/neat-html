build:
    poetry run build

publish:
	poetry run publish

format:
	poetry run black .
	poetry run ruff . --fix

check:
	poetry run black . --check
	poetry run ruff .
	poetry run mypy .

test:
	poetry run pytest --cov=python_html_dsl --cov-fail-under=100

coverage:
	poetry run coverage html

test-cov: test coverage
