# 0x03. Unittests and Integration Tests

Overview: Unit and Integration Testing in Python

## Introduction

In this project, you will learn about and implement both unit tests and integration tests in Python. You will use the `unittest` framework and the `unittest.mock` library to create comprehensive tests for your code, ensuring that each component works correctly in isolation and that the system works correctly as a whole.

## Key Concepts

### Unit Testing

- **Definition**: Unit testing involves testing individual functions or methods to ensure they return expected results for various inputs. 
- **Purpose**: To verify that a function works as intended when all external dependencies behave as expected.
- **Scope**: Focused on the logic within a single function. 
- **Mocking**: Used to replace calls to external services, databases, or other functions to isolate the function being tested.
- **Goal**: To ensure that if everything outside the function is correct, the function itself produces the correct result.

### Integration Testing

- **Definition**: Integration testing involves testing multiple components or systems together to ensure they work correctly as a whole.
- **Purpose**: To verify that different parts of the code interact correctly.
- **Scope**: End-to-end testing of the entire code path, including interactions between components.
- **Mocking**: Limited to low-level functions making external calls (e.g., HTTP requests, file I/O, database I/O).
- **Goal**: To ensure that all parts of the system work together as expected.

## Testing Execution

To run your tests, use the following command:

```bash
$ python -m unittest path/to/test_file.py
```

## Resources

- **[unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)**
- **[unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)**
- **[How to mock a readonly property with mock?](https://stackoverflow.com/questions/44666053/how-to-mock-a-readonly-property-with-mock)**
- **[parameterized](https://pypi.org/project/parameterized/)**
- **[Memoization](https://en.wikipedia.org/wiki/Memoization)**

## Learning Objectives

By the end of this project, you should be able to:

1. Explain the difference between unit and integration tests.
2. Apply common testing patterns such as mocking, parameterizations, and fixtures.

## Requirements

1. **Environment**:
   - Your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
   
2. **Code Style**:
   - All files should end with a new line.
   - The first line of all files should be exactly `#!/usr/bin/env python3`.
   - Use `pycodestyle` style (version 2.5).
   - All files must be executable.

3. **Documentation**:
   - Each module, class, and function should have a proper docstring explaining its purpose.
   - Documentation should be meaningful and not just a single word.
   - Use the following command to verify documentation:
     ```bash
     python3 -c 'print(__import__("my_module").__doc__)'
     python3 -c 'print(__import__("my_module").MyClass.__doc__)'
     python3 -c 'print(__import__("my_module").my_function.__doc__)'
     python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
     ```

4. **Type Annotations**:
   - All functions and coroutines must be type-annotated.

## Conclusion

This project will help you develop a strong foundation in writing tests for Python code, using the `unittest` framework, and understanding the importance of unit and integration testing. By the end of this project, you will be able to confidently write tests that ensure the reliability and correctness of your code.

---

Remember, good tests are critical to maintainable and reliable software. Happy testing!

Here's the `README.md` for the `0x03. Unittests and Integration Tests` project:

```markdown
# 0x03. Unittests and Integration Tests

## Overview
This project focuses on unit testing and integration testing in Python. Unit testing is used to ensure individual functions work as expected, while integration testing verifies that different parts of the application work together correctly.

### Objectives
- Understand the difference between unit and integration tests.
- Learn common testing patterns such as mocking, parametrizations, and fixtures.

### Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the folder is mandatory.
- Code should use the `pycodestyle` style (version 2.5).
- All files must be executable.
- Modules should have documentation.
- Classes should have documentation.
- Functions (inside and outside a class) should have documentation.
- All functions and coroutines must be type-annotated.

### Resources
Read or watch:
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/17351166/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

### How to Execute Tests
Execute your tests with:
```sh
$ python -m unittest path/to/test_file.py
```

## Tasks

### 0. Parameterize a unit test
- **File:** `test_utils.py`
- **Description:** Implement `TestAccessNestedMap.test_access_nested_map` method to test the `utils.access_nested_map` function.
- **Input/Output:** Test different nested maps and paths using `@parameterized.expand`.

### 1. Parameterize a unit test
- **File:** `test_utils.py`
- **Description:** Implement `TestAccessNestedMap.test_access_nested_map_exception` to test that a `KeyError` is raised for invalid paths.
- **Input/Output:** Use `assertRaises` and `@parameterized.expand`.

### 2. Mock HTTP calls
- **File:** `test_utils.py`
- **Description:** Implement `TestGetJson` class and `test_get_json` method to test `utils.get_json` without making external HTTP calls.
- **Input/Output:** Use `unittest.mock.patch` to mock `requests.get`.

### 3. Parameterize and patch
- **File:** `test_utils.py`
- **Description:** Implement `TestMemoize` class and `test_memoize` method to test `utils.memoize` decorator.
- **Input/Output:** Use `unittest.mock.patch` to mock a method.

### 4. Parameterize and patch as decorators
- **File:** `test_client.py`
- **Description:** Implement `TestGithubOrgClient` class and `test_org` method to test `GithubOrgClient.org`.
- **Input/Output:** Use `@patch` and `@parameterized.expand`.

### 5. Mocking a property
- **File:** `test_client.py`
- **Description:** Implement `test_public_repos_url` to unit-test `GithubOrgClient._public_repos_url`.
- **Input/Output:** Use `patch` as a context manager.

### 6. More patching
- **File:** `test_client.py`
- **Description:** Implement `test_public_repos` to unit-test `GithubOrgClient.public_repos`.
- **Input/Output:** Use `@patch` and `patch`.

### 7. Parameterize
- **File:** `test_client.py`
- **Description:** Implement `test_has_license` to unit-test `GithubOrgClient.has_license`.
- **Input/Output:** Parameterize the test with different inputs and expected results.

### 8. Integration test: fixtures
- **File:** `test_client.py`
- **Description:** Implement `TestIntegrationGithubOrgClient` class with `setUpClass` and `tearDownClass` methods for integration tests.
- **Input/Output:** Use `@parameterized_class` and `patch`.

### 9. Integration tests
- **File:** `test_client.py`
- **Description:** Implement `test_public_repos` and `test_public_repos_with_license` to test `GithubOrgClient.public_repos`.
- **Input/Output:** Ensure the methods return expected results based on fixtures.

## Required Files
- `utils.py`
- `client.py`
- `fixtures.py`

## Conclusion
This project provides a comprehensive understanding of unit testing and integration testing, including how to mock external dependencies, parameterize tests, and use fixtures for more complex test scenarios.

```

