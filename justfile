default:
	@just --list

build:
    poetry build

publish:
	poetry publish

format:
	poetry run black .
	poetry run ruff . --fix

check:
	poetry run black . --check
	poetry run ruff .
	poetry run mypy .

test:
	poetry run pytest --cov=python_html_dsl

coverage:
	poetry run coverage html

view-coverage:
	poetry run python -m webbrowser -t "htmlcov/index.html"

test-cov: test coverage view-coverage
