# Python Learning Workspace

Welcome to your Python learning workspace! This project is set up with a virtual environment using `uv`, structured learning modules, and a testing framework.

## Workspace Structure

- [hello.py](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/hello.py): Demonstrates basic syntax, functions, and string formatting.
- [loop.py](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/loop.py): Demonstrates `for` loops, `while` loops, and logic within loops.
- [class_demo.py](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/class_demo.py): Demonstrates Object-Oriented Programming (OOP) concepts via a simple `BankAccount` class. (Note: This is named `class_demo.py` instead of `class.py` because `class` is a reserved keyword in Python, and using it as a module name causes syntax errors when importing it.)
- **[tests/](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/tests/)**: A folder containing test suites for each Python file:
  - [test_hello.py](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/tests/test_hello.py)
  - [test_loop.py](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/tests/test_loop.py)
  - [test_class_demo.py](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/tests/test_class_demo.py)

---

## Getting Started

### 1. Activate the Virtual Environment

To start using the virtual environment created with `uv`:

```bash
# On macOS / Linux
source .venv/bin/activate
```

### 2. Run the Files

You can execute any of the Python files directly using Python from the virtual environment:

```bash
python hello.py
python loop.py
python class_demo.py
```

### 3. Run the Tests

We use `pytest` for running automated tests. You can run all tests using the following command:

```bash
pytest
```
*(Or if you haven't activated the environment, you can run `.venv/bin/pytest` directly.)*
