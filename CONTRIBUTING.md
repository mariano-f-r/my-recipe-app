# Contributing to my-recipe-app

We love and appreciate receiving any contributions.
Here are some ways you (Yes, you) can help out.

## Bug Reports

To file a bug report, open an issue and title it "BUG: \<name of the bug\>".
Then describe what you did when you go the bug.
Finally, add the "bug" label to the issue.

## Suggesting a Feature

To suggest a feature, open an issue, title it "FEATURE: \<name of feature\>".
Then type up the feature you would like to see.

## Contributing Code

Here are guidelines on how you can contribute code.

### Branch Structure

This project uses the Git flow workflow. This means that there will only ever be **5** (five) types of branches as seen below.

 Branch Type | Purpose
------------ | -------------
Main | This is what is running in production. This branch will be open at all time. Ideally, everything here should be bug free and deployable.
Development | This is where the next release is being built. This branch will also be open at all time.
Feature | Branched off the development branch, this is where new features are written. Once those features are finished, if the feature is approved, the branch is merged into the development branch and closed. Otherwise it is just closed.Note: All new code, including the addition of code commenting, additions to README/CONTRIBUTING, etc, should be done this way.
Release | Once a set number of features is met, which in this case would be 5, a release branch is created off of the development branch. In this branch, development code is tested, and prepared for release. Once this is done, the release branch is merged into both development and main, and then closed.
Bugfix | These branches are branched of main in the event of any bug. Once the bugs are fixed, the branch is merged back into main, development, and the closed

### Setting up locally

You will need:

1. Python3
2. The virtualenv Python package
3. Git

Here is how to set up on Linux/Mac (Windows instructions also included).

1. First, enter the terminal in the directory you want to contain the project, create a new directory, ideally called "recipe-app", and within it run `virtualenv env` (Note: on Windows, you may have to do `python -m virtualenv env`).
2. From the terminal, run `source env/bin/activate` (Note: Use the apropriate activation file for your shell) to activate the virtual environment (On Windows: `source env\Scripts\activate`). 
3. Install the local dependencies (Django), by doing `env/bin/python3 - m pip install django python-dotenv django-on-heroku`. (`env\Scripts\python3 -m pip install django python-dotenv django-on-heroku` on Windows)
4. Clone the repository using git (`git clone <url>`. You can find the URL by clicking the "code" tab, and then clicking on the "Code" dropdown).
5. Next, enter the new directory created by git, and create a new file called ".env". 
6. Now it's time to generate a secret token to use in your development version of the app. To do this, pull up a Python shell (`python3` on Linux and Mac, and `python` on Windows). Next run the following:
```python
>>> import secrets
>>> secrets.token_hex(24)
```
7. Copy all of the output inside the quotes. Inside the .env file, write the following:
```
token='<paste output here>'
debug='True'
```
8. Lastly, run `../env/bin/python3 manage.py migrate` (Windows: `..\env\Scripts\python3 manage.py migrate`), to create the SQL tables, and `../env/bin/python3 manage.py createsuperuser` (Windows: `..\env\Scripts\python3 manage.py createsuperuser`), to create an admin account.
9. With that, you can start the development server with `../env/bin/python3 manage.py runserver` (Windows: `..\env\Scripts\python3 manage.py runserver`). Log in to your admin account at 127.0.0.1:8000/admin and start your work!

### Adding code

For all new branches, please prefix the branch name with the type of branch it is, either "feature/\<feature-name>", or "bugfix/\<bug-name>".
This makes it a lot easier for maintainers.
Also when creating pull requests, name them after the type of branch they are (ie, "FEATURE: \<name here>", or "BUGFIX: \<name here>")

To create a new feature, create a new branch off the development branch. Write your code, and then create a pull request on the development branch.

To create a new bugfix, create a new branch off the main branch. Patch the bug, and then open a pull request on the main branch.

Releases will be handled by maintainers.