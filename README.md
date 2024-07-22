# test3

## Get started
1. Clone the repository
2. [Optional] Create a new virtual environment
3. Run `pip install -e .[test,docs]`
4. Create a `docs` folder in the root of the project and open it (`mkdir docs && cd docs`)
5. Run `spinx-quickstart` to create a new documentation (On Windows, run `sphinx-quickstart.exe`). Fill out all relevant information.
    - Select no `[n]` when asked `Separate source and build directories (y/n) [n]`
6. [Optionally] Run `make html` to build the documentation (On Windows, might have to write full path to `make.bat`).
7. Copy `docs/conf.py` into your own docs folder, replacing the existing one.
8. Change all relevant fields in the `pyproject.toml` and `docs/conf.py` files. (Don't forget the intersphinx setup)

If you want to run sphinx locally: 
- `sphinx-apidoc --separate --module-first -d 2 -H "API reference" --follow-links -o apidocs ../src/test3`
- `make.bat` html
- Open `docs/_build/html/index.html` in your browser