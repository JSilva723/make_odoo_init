DB_NAME=odoo

detach:
	@docker compose up -d

up:
	@docker compose up

down:
	@docker compose down

logs:
	@docker-compose logs -f web

build:
	@docker build -t <-mk_init_project_image->:<-mk_init_odoo_version-> .

shell:
	@docker exec -it odoo-web /usr/bin/odoo shell --db_host db -d ${DB_NAME} -r odoo -w odoo

u-all:
	@docker exec -it odoo-web /usr/bin/odoo -u all --db_host db -d ${DB_NAME} -p 8888 -r odoo -w odoo --stop-after-init

ssh:
	@docker exec -it odoo-web bash

db-ssh:
	@docker exec -it odoo-db bash

db-backup:
	@docker exec -it odoo-db pg_dump -U odoo -F c -b -v -f /lib/postgresql/backup/${DB_NAME}.dump ${DB_NAME}