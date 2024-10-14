DB_NAME=odoo

detach: ## Up container in detach mode
	@docker compose up -d

up: ## Up container in the foreground
	@docker compose up

down: ## Stop and remove containers
	@docker compose down

logs: ## Show logs from the web container, follow mode
	@docker-compose logs -f web

version: ## Switch odoo version - changed files: settings.json, docker-compose.yaml, Makefile, Dockerfile
	@sed -i '' "s/odoo-base\/[0-9]*\.[0-9]*/odoo-base\/$${v}/g" .vscode/settings.json;
	@sed -i '' "s/FROM odoo:[0-9]*\.[0-9]*/FROM odoo:$${v}/g" Dockerfile;
	@sed -i '' "s/image: \([a-zA-Z0-9_-]*\):[0-9]*\.[0-9]*/image: \1:$${v}/g" docker-compose.yaml;
	@sed -i '' "s/docker build -t \([a-zA-Z0-9_-]*\):[0-9]*\.[0-9]*/docker build -t \1:$${v}/g" Makefile;

build: ## Build the Docker image
	@docker build -t <-mk_init_project_image->:<-mk_init_odoo_version-> .

shell: ## Open Odoo shell with connection to the PostgreSQL database
	@docker exec -it odoo-web /usr/bin/odoo shell --db_host db -d ${DB_NAME} -r odoo -w odoo

u-all: ## Update all Odoo modules in the specified database and stop after completion
	@docker exec -it odoo-web /usr/bin/odoo -u all --db_host db -d ${DB_NAME} -p 8888 -r odoo -w odoo --stop-after-init

ssh: ## Open a bash shell inside the Odoo web container
	@docker exec -it odoo-web bash

db-ssh: ## Open a bash shell inside the PostgreSQL database container
	@docker exec -it odoo-db bash

db-backup: ## Backup the PostgreSQL database and save it to the backup directory
	@docker exec -it odoo-db pg_dump -U odoo -F c -b -v -f /lib/postgresql/backup/${DB_NAME}.dump ${DB_NAME}

help: ## Show help for each target
	@echo "target     |  action"
	@echo "-----------|--------"
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*##"}; {printf "%-10s | %s\n", $$1, $$2}'