# Push One Line File (POLF)
<p align="center">
  • 
  <a href="#about">About</a> •
  <a href="#setup">Setup</a> •
  <a href="#how-to">How To</a> •
</p>

## About
POLF can be used to quickly push a file with the content copied from the clipboard to a remote repository.

POLF was created after I started to do [codewars](https://www.codewars.com/) to improve my coding skills. Code challenges are sorted from the lowest **``8 kyu``** to the highest **``1 kyu``** difficulties. Most of the **``8 kyu``** challenges can be solved in one line.

Create a new file, copy the solution, paste the solution, stage the file, commit, include the message, and push is too many steps to do for a file containing only one line.

Using **POLF** the steps are reduce to two steps, create a new file and include the commit message.

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