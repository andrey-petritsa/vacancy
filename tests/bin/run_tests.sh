#!/bin/bash

export $(grep -v '^#' .env | xargs)

EXIT_CODE=0
behave tests/acceptance_tests/features/completed || EXIT_CODE=1
pytest -m "not slow" --cache-clear tests || EXIT_CODE=1

exit $EXIT_CODE
