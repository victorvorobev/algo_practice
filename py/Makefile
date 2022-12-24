LINE_LENGTH := 120

type-check:
	mypy algo

lint:
	pylint --fail-under=10 algo tests --max-line-length=$(LINE_LENGTH) --load-plugins pylint_quotes

style-check:
	flake8 algo tests --max-line-length=$(LINE_LENGTH)

test:
	pytest tests
