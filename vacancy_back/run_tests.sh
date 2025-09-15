#!/bin/bash
poetry run behave --tags="~wip" acceptance_tests/features # запустить готовые приемочные тесты
poetry run pytest
