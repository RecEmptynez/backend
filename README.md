# Kandidatarbete

Backend repo for our bachelors thesis.

## Team members

- Philip Wisnes, [@philipwinsnes](https://github.com/philipwinsnes)
- Eric Erlandsson Hollgren, [@EricErlandssonHollgren](https://github.com/EricErlandssonHollgren)
- Lucas Albinsson, [@Lucasalb51](https://github.com/Lucasalb51)
- Emil Jonsson, [@Jonsson01](https://github.com/Jonsson01)
- Pavlos Stampoulis, [@PavlosStampoulis](https://github.com/PavlosStampoulis)
- Felix La, [@Lafelix](https://github.com/Lafelix)

### Coding guidelines

- Coding guidelines - `./CONTRIBUTING.md`.

### Code and GitHub Actions

- GitHub Actions CI is found in `./github/workflows`.

## External resources

- [Jira](https://recemptynez.atlassian.net/jira/software/projects/REC/boards/1).

## Installation and running:
Use a CLI (Terminal for MacOS, CMD/PowerShell for Windows) and use the below commands.

## Downloading this repo:

Either use GitHub desktop or use your terminal to clone the repo.

```console
git clone git@github.com:RecEmptynez/backend.git
```

## Commands

You'll need to use the following commands in the terminal:

* `cd path/to/this/directory` changes the directory to `path/to/this/directory`.
* `git clone https://github.com/...` clones repositories, write the URL to the repository you want to clone

### Change directory to this repo:
```console
cd path/to/this/directory
```

### First time running:
```console
cd path/to/backend
```
```console
python -m venv env
```
windows:
```console
env/Scripts/activate 
```
Mac:??
```console
env/bin/activate 
```
When this is done you should see (env) in your terminal. If that is the case continue otherwise discord or google for help

### Install required libraries: 
```console
pip install -r requirements.txt
```
### Create environment variables file
create a file and name it ".env" in the outer backend directory.
copy and paste the following code in the new file and fill in what is needed.

POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=name_of_your_db

### Run app:
```console
cd backend
```
```console
uvicorn main:app --reload
```

### If it doesn't work
Make sure to be in the right directory (the same directory where the git repository is on your computer)
