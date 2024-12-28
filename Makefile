# postgres commands
postgres-create:
	docker pull postgres:alpine

postgres-start:
	docker run --name fastapi-postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:alpine

postgres-exec:
	docker exec -it fastapi-postgres psql -U postgres


# docker commands
docker-images:
	docker images

docker-ps:
	docker ps


# python commands
py-install:
	pip install --upgrade pip
	pip install -r requirements.txt --upgrade

py-run-tests:
	pytest tests


# fastapi commands
fastapi-run:
	uvicorn main:app --reload
