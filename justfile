default:
	@just --list

build:
    poetry build

publish:
	poetry publish

format:
	poetry run black .
	poetry run ruff check . --fix

fix: format

check:
	poetry run black . --check
	poetry run ruff check .
	poetry run mypy .

test *args:
	poetry run pytest --cov=neat_html {{args}}

coverage:
	poetry run coverage html

view-coverage:
	poetry run python -m webbrowser -t "htmlcov/index.html"

test-cov: test coverage view-coverage
