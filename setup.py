from setuptools import setup, find_packages
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('mkio/templates')

setup(
    name='make_odoo_init',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    package_data={
        'mkoi': extra_files,
    },
    entry_points={
        'console_scripts': [
            'mkoi=mkoi:main',
        ],
    },
    description='CLI Tool for scaffolding Odoo projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author_email='silvajonatanivan@gmail.com',
    url='https://github.com/JSilva723/make_odoo_init',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)