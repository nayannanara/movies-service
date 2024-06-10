pycache:
	@echo "Running Clean Pycache..."
	@find . \( -name *.py[co] -o -name __pycache__ \) -delete

precommit:
	@poetry run pre-commit install

run:
	@poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

start-scraper:
	@poetry run python -m app.scraper.run

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(description)

start-flow:
	@poetry run python -m app.flows.main

test:
	@poetry run pytest

test-matching:
	@poetry run pytest ./tests -vv -k $(K)


coverage:
	@poetry run pytest --cov=app --cov-report=term-missing --cov-report=xml ./tests/

lint:
	@poetry run ruff check .

lint-fix:
	@poetry run ruff check . --fix

.PHONY: run test generate-coverage lint-check lint-fix
