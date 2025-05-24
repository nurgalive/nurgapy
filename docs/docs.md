# NurgaPy Documentation 🧻

> Here I will publish design decision and additional info about how NurgaPy build and working.

# Table of Contents
- [Documentation for developers](#Documentation-for-developers)
- [Architecture decisions](#Architecture-decisions)

# Documentation for developers
If you want to hack and develop around NurgaPy this section of the documentation will be helpful for you.


This project uses [Poetry](https://python-poetry.org/docs/) for the package management.

Install Poetry (if not installed)
```
curl -sSL https://install.python-poetry.org | python3 -
```

It is [advised](https://www.youtube.com/watch?v=0f3moPe_bhk) to use the [Poetry virtual environment](https://python-poetry.org/docs/managing-environments/) inside the project folder.
It can be turned on using this command:
```bash
poetry config virtualenvs.in-project true
```

Install project dependencies and create a virtual environment:
```bash
poetry install
```
It will create a virtual environment in folder `.venv` inside the project folder.

You can check created environments using command:
```
poetry self update
```

In order to activate the created environment use:
```
source .venv/bin/activate
```
And run the project example as usual python script:
```
python examples/annotation_class.py
```
Deactivate the virtual environment:
```
deactivate
```

Also, you can run project example using poetry without activating the virtual environment:
```
poetry run python examples/annotation_class.py
```

## Installing pre-commit checks
Pre-commit is a library, which runs checks before every commit. And it will not allow run commit until all the checks are succeeded. The currently used rules can be reviewed in the file [`.pre-commit-config.yaml`](../.pre-commit-config.yaml).

Install pre-commit hooks
```
poetry run pre-commit install
```

[Pre-commit](https://pre-commit.com/) will run automatically after running `git commit`.
But it is also possible to run pre-commit checks against all files manually.
Adding `--verbose` will also print more detailed info. Helpful for debugging test.
```
poetry run pre-commit run --all-files
```

Update the pre-commit hooks.
```
poetry run pre-commit autoupdate
```


## Running tests
Pytest is the Python testing library with the lean syntax.

Run tests using pytest.

```bash
poetry run pytest -v
```

`-s` - will print the `print()` statements. Use it for debug.

## Publish a new version

In NurgaPy semantic versioning is used. After pushing a new version, a GitHub Actions workflow will be triggered, which will push a new version to PyPi and will also create a new GitHub Release.
In order to publish a new version, apply the next steps:
```
poetry version patch  # 0.0.x

poetry version minor  # 0.x.0

poetry version major  # x.0.0
```

Then create a proper git tag
```
git tag x.x.x
```

And push it
```
git push origin --tags
```
# Architecture decisions

Main focus of this project it to avoid me copying the same code between projects.
As well as this project is focused on the software engineering practices, and will serve for me as blueprint for future projects as a best practices for building a project from scratch and state-of-the-art technologies in software engineering.
This includes:
- proper file structure of the package
- usage of the correct code style (e.g. PEP-8 and Google Code Style)
- usage of different tools, which makes life a software engineer easier
(package management, style formatting and checks, code checks, spelling checks)
- extensive usage of automation and code testing

In this section of the docs I will elaborate my decisions onto different parts of the project.

## Project structure
This project uses one of the traditional project structure for the Python projects.

```
.
├── docs
│   └── docs.md
├── examples
│   ├── annotation_class.py
│   └── tyme_function_call.py
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── README.md
├── src
│   └── nurgapy
│       ├── __init__.py
│       ├── trackbar.py
│       └── tyme.py
└── tests
    ├── __init__.py
    ├── trackbar_test.py
    └── tyme_test.py
```

Project package has all the files located in the `src/nurgapy

## Code testing
As a testing library was chosen Pytest, as a current standard in the Python testing. There is also built-in unittest library available, but community leaning towards pytest.

## Package manager

## Code linting and formatting

## GitHub Actions CI/CD

## Pre-commit checks
