default: build

build:
	docker-compose build

run:
	docker-compose down -rmi
	docker-compose up

restart:
	docker-compose restart web