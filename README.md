# Homework 3

## Configure

1. clone the repository

2. install dependencies via poetry

```bash
poetry install
```

3. install pre-commit hooks

```bash
poetry run pre-commit install
```

4. do your tasks

5. commit your changes
6. if pre-commit hooks fail, such as blocked by prettier, add your files again and commit

## Task: Run Static Analysis Tools

Add package to dependencies:

- [x] black (code formatting)
  - [x] added to pre commit
- [x] pylint (general static analysis and code quality)
  - [x] added to pre commit
- [x] pyflakes (error detection)
- [x] bandit (security vulnerabilities)
- [ ] radon (complexity analysis)
- [x] prettier (code formatting for web development)
  - [x] added to pre commit

## Task: Write 3 test cases for merge sort using pytest

Task done by:

- [x] `zgong6` added pytest for [`None` input](tests/test_none_input.py), [empty list](tests/test_empty_input.py), and a [list with one element](tests/test_single_element_input.py)
- [x] `azkuang2` added pytest for [Two inputs with six elements each](tests/test_six_elements.py), added bandit to test code pre-commit
- [x] `opdesai2` added pytest for [Duplicates in input](tests/test_duplicate_input.py) and [Negative inputs](tests/test_negative_input.py)

## Task: Configure github actions

- [x] Added pytest by @visualDust
- [x] Bandit added by @azkuang
- [x] Pylint added by @visualDust
- [x] Pyflakes (flake8) added by @odesai840

Now you can see output of those tools in workflow outputs.
![image](https://github.com/user-attachments/assets/3274ec8f-b038-4ce9-acd6-10a2f8801de1)
