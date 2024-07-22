# test3

## Get started

First, clone the repository.

Create the `main`, `develop` and, `gh-pages` branches.

Whenever you want to change something, create a new branch. If it is done, create a pull request to the `develop` branch.

Only pull from `develop` to `main` with fully functional, tested and documented new versions.

### Repository Settings
**Branch Protection Rules**
TODO: Write this Section

**Actions Permissions**
1. Go to the repository settings
2. Open `Actions` > `General` in the left sidebar
3. Under `Workflow permissions`, select
   - `Read and write permissions`
   - `Allow GitHub Actions to create and approve pull requests`

### Set Up Project
1. [Optional] Create a new virtual environment
2. Run `pip install -e .[test,docs]`

**Documentation Setup**
1. Create a `docs` folder in the root of the project and open it (`mkdir docs && cd docs`)
2. Run `spinx-quickstart` to create a new documentation (On Windows, run `sphinx-quickstart.exe`). Fill out all relevant information.
    - Select no `[n]` when asked `Separate source and build directories (y/n) [n]`
3. [Optionally] Run `make html` to build the documentation (On Windows, might have to write full path to `make.bat`).
4. Copy `docs/conf.py` into your own docs folder, replacing the existing one.
5. Change all relevant fields in the `pyproject.toml` and `docs/conf.py` files. (Don't forget the intersphinx setup)

If you want to run sphinx locally: 
- `sphinx-apidoc --separate --module-first -d 2 -H "API reference" --follow-links -o apidocs ../src/test3`
- `make.bat` html
- Open `docs/_build/html/index.html` in your browser