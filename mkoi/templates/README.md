## Step 1
Build docker image
```sh
make build
````

## Step 2
Create the addons directory inside the web folder to add custom modules:
```sh
/my_project
    ├── Dockerfile
    ├── docker-compose.yml
    ├── README.md
    ├── web
    |    ├── addons
    |    └── odoo.conf
    └── ...
```

## Step 3

Up containers
```sh
make detach # make up
````

```sh
/my_project
    ├── .vscode
    |    ├── launch.json
    |    └── settings.json
    ├── db/
    ├── web
    |    ├── addons
    |    |    └── ...
    |    ├── data/
    |    └── odoo.conf
    ├── docker-compose.yml
    ├── Dockerfile
    ├── Makefile
    └── README.md
```
***

## Note
Linux users uncomment that lines in docker-compose.yaml
```sh
user: "${UID}:${GID}" # for linux users
```
## Help
```sh
make help
```