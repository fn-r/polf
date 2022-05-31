import subprocess
from tkinter import Tk
from pathlib import Path

#! Change `file_path` according to your file path
path = Path.cwd()
file_path = path / 'codewars' / 'JavaScript' / '8kyu'

def push(file_name):
    """
    Used to push to repo by executing these commands in the terminal:
    1. Run `git add <file_path>` - Stage file
    2. Run `git commit -m <commit_msg>` - Commit with the provided message
    3. Run `git push` - Push to repo
    """
    def run(*args):
        return subprocess.check_call(['git'] + list(args))

    commit_msg = input('Type in your commit message: ')
    if (commit_msg == ''):
        # commit message is empty
        commit_msg = f"Add '{file_name}' solution"
    run('add', file_path)
    run('commit', '-m', commit_msg)
    run('push')

def create_file():
    """
    Used to create a file with the stored clipboard as the file's content
    """
    invalid_file_name = '\\/:*?"<>|'

    root = Tk()
    root.withdraw()
    file_content = root.clipboard_get()
    print('Copied Content:')
    print(file_content)
    print('')

    file_name = input('File Name: ')
    if any (c in invalid_file_name for c in file_name):
        print(f"A file name can't contain any of the following characters: {', '.join(invalid_file_name)}")
        print('')
        create_file()
    else:
        full_path = file_path / file_name
        root.destroy()

        with open(full_path, 'w') as file:
            file.write(file_content)
        
        return full_path.name

def main():
    file_name = create_file()
    push(file_name)

# run the program
main()
