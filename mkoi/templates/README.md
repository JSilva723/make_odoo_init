## Step 1
Build docker image
```sh
make build
````

## Step 2
Create the addons directory inside the web folder to add custom modules:
```
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

```
/my_project
    ├── .vscode
    |    ├── launch.json
    |    └── settings.json
    ├── db
    |    └── data/
    ├── web
    |    ├── addons
    |    |    └── ...
    |    ├── filestore/
    |    └── odoo.conf
    ├── docker-compose.yml
    ├── Dockerfile
    ├── Makefile
    └── README.md
```
***
## Help
```sh
make help
```