COMPOSE = docker compose -f docker-compose.yaml

run_dev:
	TARGET=dev ${COMPOSE} -f docker-compose.override.yaml up -d --build

run_prod:
	TARGET=prod ${COMPOSE} up -d --build

run_tests:
	TARGET=prod ${COMPOSE} up -d --build
	${COMPOSE} build test
	docker compose run --rm test
