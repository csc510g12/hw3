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

## Task: Create your own branch

1. Add extra code (any algorithm with issues; the algorithm should be different from your group members’). It is recommended that students implement the algorithm by hand rather than copying an example online. This approach will help reinforce the understanding of debugging techniques, which are key learning objectives of this assignment.

2. Run tools on all files:

```bash
pylint hw2_debugging.py rand.py > pylint_report.txt
pyflakes hw2_debugging.py rand.py > pyflakes_report.txt
```

3. Fix issues reported by static analysis

   - Correct coding style violations, security concerns, and potential logical errors.
   - Ensure that all fixes maintain the intended functionality.

4. Re-run the Tools: After fixing issues, rerun each tool and save the updated results inside a post_traces folder.
5. After fixing the code, commit changes to your repository.

Task done by:

- [x] `zgong6`
- [ ] `azkuang2`
- [ ] `opdesai2`

## Task: Write 3 test cases for merge sort using pytest

Task done by:

- [x] `zgong6` added pytest for [`None` input](tests/test_none_input.py), [empty list](tests/test_empty_input.py), and a [list with one element](tests/test_single_element_input.py)
- [x] `azkuang2` added pytest for [Two inputs with six elements each](tests/test_six_elements.py), added bandit to test code pre-commit
- [ ] `opdesai2`

## Task: Merge all branches

## Task: Configure github actions

1. Configure automated testing to run on every commit

- [x] Added pytest by @visualDust

1. Configure static analysis tools running on every commit

- [x] Bandit added by @azkuang
- [x] Pylint added by @visualDust

Now you can see output of those tools in workflow outputs.
![image](https://github.com/user-attachments/assets/3274ec8f-b038-4ce9-acd6-10a2f8801de1)
