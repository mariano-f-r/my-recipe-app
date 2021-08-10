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
Main | This is what is running in production. This branch will be open at all time. Ideally, everything here should be bug free.
Development | This is where the next release is being built. This branch will also be open at all time.
Feature | Branched off the development branch, this is where new features are written. Once those features are finished, if the feature is approved, the branch is merged into the development branch and closed. Otherwise it is just closed.
Release | Once a set number of features is met, which in this case would be 5, a release branch is created off of the development branch. In this branch, development code is tested, and prepared for release. Once this is done, the release branch is merged into both development and main, and then closed.
Bugfix | These branches are branched of main in the event of any bug. Once the bugs are fixed, the branch is merged back into main, development, and the closed

### Setting up locally

You will need:

1. Python3
2. The virtualenv Python package
3. The Django Python package
4. Git

Here is how to set up on Linux/Mac (Windows instructions also included).

1. First, create a new folder, ideally called, "recipe-app"
2. Secondly, enter the terminal in the new directory, and run `virtualenv env` (Note: on Windows, you may have to do `python -m virtualenv env`).
3. From the terminal, run `env/bin/activate` (Note: Use the apropriate activation file for your shell) to activate the virtual environment (On Windows: `env\Scripts\activate`). 
4. Install the local dependencies (Django), by doing `env/bin/python3 - m pip install django`. (`env\Scripts\python3 -m pip install django`)
5. Clone the repository using git (`git clone <url>`. You can find the URL by clicking the "code" tab, and then clicking on the "Code" dropdown).
6. Lastly, enter the terminal from the new directory created by git, and run `../env/bin/python3 manage.py runserver`. The local development server will start up and you will be able to see it at 127.0.0.1:8000.