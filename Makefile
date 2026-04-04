test:
	uv run pytest --cov --cov-branch --cov-report=xml:coverage/coverage.xml --junitxml=coverage/junit.xml -o junit_family=legacy

lint:
	uv run ruff check .

type:
	uv run ty check .
