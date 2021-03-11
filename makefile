
exec_postgres:
	docker-compose exec postgres psql -U postgres -d postgres

exec_mongo:
	docker-compose exec mongodb mongo

exec_example:
	docker-compose exec example bash
