import subprocess
from tkinter import Tk
from pathlib import Path

#! Change `file_path` according to your file path
path = Path.cwd()
file_path = path / 'codewars' / 'JavaScript' / '8kyu'

def push():
    """
    Used to push to repo by executing these commands in the terminal:
    1. Run `git add <file>` - Stage file
    2. Run `git commit -m <commit_msg>` - Commit with the provided message
    3. Run `git push` - Push to repo
    """
    def run(*args):
        return subprocess.check_call(['git'] + list(args))

    commit_msg = input('Type in your commit message: ')
    run('add', file_path)
    run('commit', '-m', commit_msg)
    run('push')

def create_file():
    """
    Used to create a file with the stored clipboard as the file's content
    """
    root = Tk()
    root.withdraw()
    file_name = input('File Name: ')
    file_content = root.clipboard_get()
    full_path = file_path / file_name
    root.destroy()

    with open(full_path, 'w') as file:
        file.write(file_content)

def main():
    create_file()
    push()

# run the program
main()