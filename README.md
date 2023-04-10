# fastapi-clean-template

> Library reference
>
> [tiangolo/fastapi: FastAPI framework, high performance, easy to learn, fast to code, ready for production (github.com)](https://github.com/tiangolo/fastapi)
>
> [tiangolo/sqlmodel: SQL databases in Python, designed for simplicity, compatibility, and robustness. (github.com)](https://github.com/tiangolo/sqlmodel)
>
> [sqlalchemy/alembic: A database migrations tool for SQLAlchemy. (github.com)](https://github.com/sqlalchemy/alembic)
>
> [audreyfeldroy/cookiecutter-pypackage: Cookiecutter template for a Python package. (github.com)](https://github.com/audreyfeldroy/cookiecutter-pypackage)
>
> [fastapi-clean-architecture/database.py at main · Flaiers/fastapi-clean-architecture (github.com)](https://github.com/Flaiers/fastapi-clean-architecture/blob/main/internal/config/database.py)

## How to use it

Go to the directory where you want to create your project and run:

```bash
$ pipx install cookiecutter
$ cookiecutter https://github.com/Etuloser/fastapi-clean-template
```

### Input variables

The input variables, with their default values (some auto generated) are:

- `project_name`: The name of the project
- `project_slug`: The development friendly name of the project. By default, based on the project name
- `project_port`: The port of the project serverd by uvicorn
- `db_user`: username of mysql database
- `db_pass`: password of mysql database
- `db_host`: host of mysql database
- `db_port`: port of mysql database
- `db_name`: name of mysql database