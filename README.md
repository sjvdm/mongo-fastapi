# mongo-fastapi
Project to expose behavioural metrics stored in Mongo on a fastapi-api based API. 

## Installation

This project is based on a Python 3.12 implementation and uses Poetry to manage packages.

1. Ensure you have pipx installed. This ensures isolated packages for tools such as Poetry. See [pipx on Github](https://github.com/pypa/pipx)
2. Install [poetry](https://python-poetry.org/docs/#installing-with-pipx) (suggested via pipx to keep poetry isolated in its own environment)
3. Clone this repo locally or on your server.
4. In this repo directory, initialize the environment, installs and shell by running the following (note this is dependent on poetry being installed):
```
poetry install
poetry shell
```
5. Your virtual enviroment should now be activated with all dependencies.
