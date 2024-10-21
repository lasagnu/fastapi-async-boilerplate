# FastAPI Async Boilerplate

This repository provides a boilerplate for building an asynchronous FastAPI application. It includes configurations for development tools like `pytest`, `pylint`, `isort`, and `black` to streamline the development workflow, ensure code quality, and maintain consistent coding standards.

## Features

- **FastAPI**: An async web framework for building fast APIs with Python 3.7+ based on standard Python type hints.
- **Async Ready**: The app is structured to use asynchronous endpoints, making it suitable for high-concurrency applications.
- **Testing with pytest**: `pytest` is pre-configured for running unit and integration tests, ensuring smooth testing workflows.
- **Code Formatting with black**: `black`, the uncompromising code formatter, is integrated for automatic code formatting.
- **Import Sorting with isort**: `isort` is configured to automatically sort imports based on standard conventions.
- **Code Linting with pylint**: `pylint` is set up for static analysis, ensuring that the codebase adheres to best practices and style guidelines.

## Installation

1. Clone the repository:
   ```bash
   git clone https://https://github.com/lasagnu/fastapi-boilerplate.git
   cd fastapi-boilerplate/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install dependencies for testing & development (optional):
   ```bash
   pip install -r requirements-dev.txt
   ```

## Usage

1. Run the FastAPI development server:
   ```bash
   uvicorn app:app --reload
   ```

2. Access the auto-generated OpenAPI docs at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.

## Testing

Run tests using `pytest`:

```bash
pytest
```

## Code Coverage with pytest-coverage

The repository is configured to automatically generate test coverage reports when running `pytest`, using `pytest-coverage`.

## Code Quality and Formatting

### Black (Code Formatter)

To automatically format your code using `black`, run:

```bash
black .
```

### isort (Import Sorting)

Ensure that your imports are sorted according to the configured rules:

```bash
isort .
```

### Pylint (Static Code Analysis)

Run `pylint` to check the code quality and adherence to Python style conventions:

```bash
pylint . --rcfile .pylintrc
```

## Configuration

### Pytest

The [setup.cfg](backend/setup.cfg) file includes configuration for `pytest` to ensure it looks for tests in the `backend/tests` directory.

### Pylint

The [.pylintrc](backend/.pylintrc) file contains settings for `pylint` to enforce coding standards.


### Black & isort

The [pyproject.toml](backend/pyproject.toml) file contains settings for `black` and `isort`


## Contributing

Feel free to open an issue or submit a pull request if you'd like to contribute to this boilerplate or have suggestions for improvements.