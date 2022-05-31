# Push One Line File (POLF)
<p align="center">
  • 
  <a href="#about">About</a> •
  <a href="#used-on">Used On</a> •
  <a href="#technology-stack">Technology Stack</a> •
  <a href="#optimizations">Optimizations</a> •
  <a href="#lesson-learned">Lesson Learned</a> •
  <a href="#setup">Setup</a> •
  <a href="#how-to">How To</a> •
</p>

## About
POLF can be used to quickly push a file with the content copied from the clipboard to a remote repository.

POLF was created after I started to do [codewars](https://www.codewars.com/) to improve my coding skills. Code challenges are sorted from the lowest **``8 kyu``** to the highest **``1 kyu``** difficulties. Most of the **``8 kyu``** challenges can be solved in one line.

Create a new file, copy the solution, paste the solution, stage the file, commit, include the message, and push is too many steps to do for a file containing only one line.

Using **POLF** the steps are reduce to two steps, create a new file and include the commit message.

<img src="https://github.com/fn-r/portfolio/blob/main/images/gif/polf.gif" width="100%" alt="POLF"/>

## Used On
- **[My Coding Challenges Repository](https://github.com/fn-r/coding-questions)**

## Technology Stack
![PYTHON BADGE](https://custom-icon-badges.herokuapp.com/badge/-python-A5FFCE?style=for-the-badge&logo=python&logoColor=A5FFCE&labelColor=000000)

My learning for this project is by purposely not using GitHub API and other libraries that require installation as I have made this project for those that just started to code.

## Optimizations
I may further improve this project by utilizing the new Python standard library, **[ConfigParser](https://docs.python.org/3/library/configparser.html)**. This way it would prompt user for the local path only during setup. In order to change this path, however, I would also need to add a menu similar to this:
```console
----- Main Menu -----
1. Push to Remote Repo
2. Edit Local Path
Enter your choice: _
```

## Lesson Learned
- subprocess:
    ``subprocess`` is used to replaced Python deprecated ``os`` module. The ``os`` module is [susceptibility to shell injection](https://hackernoon.com/calling-shell-commands-from-python-ossystem-vs-subprocess-mc253z4f), so it is best to avoid using it.
- It's risky to use deprecated methods, make sure to check Python documentation to check for the modern approach.
- Make sure to include error checking. Some special characters are not allowed as the file name.

## Setup
1. Make sure Git is already setup and configured
    ```console
    $ git config --global user.name "Your Name"
    $ git config --global user.email "yourname@example.com"
    ```
1. Python 3.5 and above is needed to run the script. You can check Python 3 is installed and its version with the following command
    ```console
    $ python3 --version
    ```
1. If it is not installed, you can install it with the following commands
    ```console
    $ sudo apt-get update
    $ sudo apt-get install python3
    ```
1. Go to your local repo
1. Clone this repo into your local repo
    ```console
    $ git clone https://github.com/fn-r/polf.git
    ```
1. Cut the roots of this repo with the following command
    ```console
    $ rm -rf polf/.git
    ```
1. Go to ``polf`` > ``main.py`` and change **file_path** according to your remote repo path
1. Create **.gitignore** file (ignore this step if you already have it)
1. In **.gitignore**, add the following line
    ```
    /polf
    ```

## How To
1. Copy content
1. Run **POLF** in the terminal (make sure you are in your local repo) using the following command:
    ```console
    $ python polf/main.py
    ```
1. Enter file name
1. Enter commit message