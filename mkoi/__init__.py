#!/usr/bin/env python3
import os
import shutil
import argparse

def ask_inputs():
    odoo_image = input("Please, specify Odoo image (odoo): ") or "odoo"
    odoo_version = input("Please, specify Odoo version (17.0): ") or "17.0"
    postgres_version = input("Please, specify PostgreSQL version (13.0): ") or "13.0"
    odoo_base_path = input("Please, specify odoo base path: ")

    while not odoo_base_path:
        odoo_base_path = input("Please, specify odoo base path: ")

    return odoo_image, odoo_version, postgres_version, odoo_base_path

def replace_values_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()

    for key, value in replacements.items():
        content = content.replace(key, value)

    with open(file_path, 'w') as file:
        file.write(content)

def copy_template_and_replace(template_dir, project_dir, replacements):
    if not os.path.exists(project_dir):
        shutil.copytree(template_dir, project_dir)
    
    for root, dirs, files in os.walk(project_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            replace_values_in_file(file_path, replacements)

def main():
    parser = argparse.ArgumentParser(description="Create a new Odoo project")
    parser.add_argument("project_name", help="The name of the project to create")
    args = parser.parse_args()

    project_name = args.project_name

    # Get path where command is executed
    root_dir = os.getcwd()
    project_dir = os.path.join(root_dir, project_name)

    # Get template path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(script_dir, "templates")

    # Get inputs values
    odoo_image, odoo_version, postgres_version, odoo_base_path = ask_inputs()
    replacements = {
        "<-mk_init_odoo_version->": odoo_version,
        "<-mk_init_postgres_version->": postgres_version,
        "<-mk_init_odoo_image->": odoo_image,
        "<-mk_init_odoo_base_path->": odoo_base_path,
    }

    copy_template_and_replace(template_dir, project_dir, replacements)

if __name__ == "__main__":
    main()
