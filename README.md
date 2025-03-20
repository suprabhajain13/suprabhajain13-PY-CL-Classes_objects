# PY-CL-Classes_objects

## Overview

This project simulates the behavior of lightbulbs. It includes functionality to create lightbulb objects, toggle their state, and get their description. The project also includes unit tests to ensure the correctness of the implemented functionality.

## Files

### app.py
The `app.py` file serves as the entry point for the project. It demonstrates the usage of the `create_bulb` function from `lab.py` to create lightbulb objects with different initial states and prints their descriptions.

### lab.py
The `lab.py` file contains the implementation of the Lightbulb class, which represents a lightbulb object. It includes methods to initialize the state of the lightbulb, get its current state, set its state, and get its description based on its state.

### lab_test.py
The `lab_test.py` file contains unit tests for the Lightbulb class in `lab.py`. It ensures that the implemented methods behave as expected by testing them with various scenarios such as initial state, description, and state setting.

## Project Structure

src/
  ├── main/
  │     ├── app.py
  │     └── lab.py
  └── test/
        └── lab_test.py

## Getting Started

- Open the `src/main/app.py` file.
- Run the `app.py` file to interactively create lightbulb objects and see their descriptions.
- Refer to the comments in the code for guidance on usage.

## Testing

- Open the `src/test/lab_test.py` file.
- Run the `lab_test.py` file to execute the unit tests.
- Ensure that all tests pass, indicating that the implemented methods are working correctly.

## Conclusion

This project provides a simple demonstration of object-oriented programming in Python. By exploring the Lightbulb class and running the tests, users can enhance their understanding of classes, objects, and unit testing in Python.

Happy Coding!