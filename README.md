# Client Manager with Python

A simple customer management system built with Python, featuring:

- Command-line and Tkinter GUI interfaces
- FastAPI REST API for customer CRUD operations
- CSV-based persistent storage

## Features

- Add, edit, remove, and delete customers
- Search for customers by ID
- RESTful API endpoints for integration
- Input validation for customer data

## Project Structure

```
api.py              # FastAPI REST API
config.py           # Configuration (CSV path, etc.)
customers.csv       # Main customer data storage
database.py         # Customer data model and persistence
helpers.py          # Utility functions (validation, input, etc.)
menu.py             # Command-line menu interface
run.py              # Entry point (CLI or GUI)
ui.py               # Tkinter GUI
tests/              # Unit tests and test data
```

## Requirements

- Python 3.10+
- See [Pipfile](Pipfile) for dependencies

## Installation

1. Clone the repository:
    ```sh
    git clone (https://github.com/CodeHarold/FastAPI_manager_with_Python.git)
    cd client-manager-with-python
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Command-Line Menu

```sh
python run.py -t
```

### GUI

```sh
python run.py
```

### API

Start the FastAPI server:
```sh
uvicorn api:app --reload
```
Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API documentation.

## Running Tests

```sh
python -m unittest discover tests
```


