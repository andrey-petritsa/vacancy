#!/bin/bash
poetry --directory vacancy_back run pytest
poetry --directory vacancy_back run behave acceptance_tests/features