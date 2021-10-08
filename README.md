Corona Travel server
====================

Development
-----------
1. install [`git-flow`]() and [`pyenv`](https://github.com/pyenv/pyenv)
2. use one of git-flow commands to start a branch, run `poetry run dev` to develop on that branch and view changes on http://localhost:4000, finish and push your change to remote repository
    ```sh
    git flow feature start <name>
    poetry run dev
    git flow feature finish
    git flow feature publish
    ```
