# Make Odoo init

## Overview

`make_odoo_init` is a CLI tool designed to scaffold Odoo projects with specific configurations. It allows users to quickly create project directories and configure essential components like Odoo version, PostgreSQL version, and the base path for Odoo.

## Features

- Scaffolds Odoo projects using a pre-defined template.
- Replaces placeholders in template files with user-provided configurations.
- Supports configuration for:
  - Odoo version
  - PostgreSQL version
  - Odoo base path

## Requirements

- **Python 3.6+** (Recommended)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/JSilva723/make_odoo_init
   cd make_odoo_init
   ```

2. Install the package:

   ```bash
   pip install .
   ```

## Usage

Once installed, you can use the command `mkoi` to generate a new Odoo project scaffold:

```bash
mkoi
```

This will prompt you to enter:

1. **Project Name**: The name of your new project.
2. **Odoo Version**: The version of Odoo you want to use (default is `17.0`).
3. **PostgreSQL Version**: The version of PostgreSQL (default is `13.0`).
4. **Odoo Base Path**: The base path where Odoo is installed.

After entering the values, the tool will generate a project structure based on the template provided in the `templates` directory.

## Example

```bash
$ mkio
Please, specify Project Name: my_project
Please, specify Odoo version (default: 17.0): 16.0
Please, specify PostgreSQL version (default: 13.0):
Please, specify odoo base path: /home/user/odoo/17.0
```

## Project Structure

The generated project will follow this structure:

```
/my_project
    ├── Dockerfile
    ├── docker-compose.yml
    ├── README.md
    └── ...
```

## Recommended Extensions for Development

If you're using **Visual Studio Code** for development, we recommend using the following extensions to enhance your Python development workflow:

### Pyright

- **Name**: Pyright
- **Id**: ms-pyright.pyright
- **Description**: VS Code static type checking for Python.
- **Version**: 1.1.383
- **Publisher**: Microsoft
- **VS Marketplace Link**: [Pyright - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright)

This extension provides static type checking for Python in VS Code, helping catch potential errors early in the development process.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
