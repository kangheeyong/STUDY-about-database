
exec_postgres:
	docker-compose exec postgres psql -U postgres -d postgres

exec_mongo1:
	docker-compose exec mongodb1 mongo

exec_mongo2:
	docker-compose exec mongodb2 mongo

exec_mongo3:
	docker-compose exec mongodb3 mongo

exec_example:
	docker-compose exec example bash

exec_elasticsearch:
	docker-compose exec elasticsearch bash

exec_kibana:
	docker-compose exec kibana bash

exec_logstash:
	docker-compose exec logstash bash

docker_volume_list:
	docker volume ls