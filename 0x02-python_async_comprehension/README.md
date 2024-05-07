# 0x02. Python - Async Comprehension

## Description
This project focuses on asynchronous programming in Python, specifically on asynchronous generators and comprehensions. It explores the usage of async functions, async generators, and async comprehensions, providing hands-on exercises to reinforce understanding. The project culminates in measuring the runtime of asynchronous operations executed in parallel.

## Resources
- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#asynchronous-generators)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Learning Objectives
By the end of this project, learners should be able to:
- Write an asynchronous generator
- Utilize async comprehensions effectively
- Type-annotate generators for improved code readability and maintainability

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Mandatory README.md file at the root of the project folder
- Code should follow PEP 8 style guidelines (version 2.5.x)
- File length tested using `wc`
- All modules must have documentation
- All functions and coroutines must be documented and type-annotated

## Tasks
1. **Async Generator**
   - Write a coroutine `async_generator` that loops 10 times, waiting asynchronously for 1 second on each iteration, then yielding a random number between 0 and 10.

2. **Async Comprehensions**
   - Import `async_generator` from the previous task and write a coroutine `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`, then returns the collected numbers.

3. **Run time for four parallel comprehensions**
   - Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather`. Measure the total runtime and return it.

## Repository
- GitHub repository: [alx-backend-python](https://github.com/Muna-Saeed/alx-backend-python/0x02-python_async_comprehension)
- Directory: 0x02-python_async_comprehension
