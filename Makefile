default: build

build:
	docker-compose build

run: build
	docker-compose down
	docker-compose up

restart:
	docker-compose restart web