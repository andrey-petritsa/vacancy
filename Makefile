COMPOSE = docker compose -f docker/docker-compose.yaml
export URL = http://host.docker.internal

run_dev_build:
	TARGET=dev ${COMPOSE} -f docker/docker-compose.override.yaml up -d --build front back

run_test_build:
	TARGET=test ${COMPOSE} -f docker/docker-compose.override.yaml up -d --build front back

run_prod_build:
	TARGET=prod ${COMPOSE} up -d --build  back front

run_tests:
	TARGET=prod ${COMPOSE} up -d --build  back front
	${COMPOSE} run --build --rm tests
