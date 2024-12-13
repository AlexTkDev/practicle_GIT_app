# Git Learning Game

This game is designed for learning and practicing Git commands through an interactive approach. The project is created using the Kivy framework for developing the graphical user interface.

## Features

- Interactive GUI for learning Git commands.
- Different difficulty levels for missions.
- Hints for incorrect answers.
- Comprehensive coverage of basic Git commands.

## Installation

To install the necessary dependencies and run the game, follow these steps:

   1. Clone the repository:
```bash
   git clone https://github.com/AlexTkDev/practicle_GIT_app.git

   cd practicle_GIT_app
```

   2. Create and activate a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate  # For Unix

   venv\Scripts\activate  # For Windows
```

   3. Install the dependencies:
```bash
    pip install -r requirements.txt
```

## Running the Game

To start the game, use the following command:
```bash   
   python main.py
```

## Project Structure

- `main.py` - The main file to run the application.
- `requirements.txt` - File with project dependencies.
- `README.md` - Project documentation.

## Missions and Commands

### Missions

Missions are divided into three difficulty levels:

#### Easy

- Initializing a new repository
- Adding a file to be tracked
- Viewing the repository status
- Creating a commit with a message
- Viewing commit history
- Creating a new branch and switching to it

#### Medium

- Cloning a repository
- Adding changes and creating a commit
- Switching branches
- Viewing differences between commits
- Stashing and applying changes
- Creating a tag for a commit
- Adding a remote repository
- Fetching changes from a remote repository

#### Hard

- Pushing changes to a remote repository
- Fetching and merging changes from a remote repository
- Creating a new branch, switching to it, and merging changes
- Cherry-picking commits onto another branch
- Reverting changes to the last commit
- Reverting the last commit
- Viewing commit details by ID
- Viewing commit history in one line
- Setting user name and email

### Commands

Complete list of commands used in the game:

- `git init` - Creates a new repository.
- `git clone <url>` - Clones an existing repository.
- `git add <file>` - Adds files to the next commit.
- `git commit -m 'message'` - Records changes with a comment.
- `git push` - Pushes commits to a remote repository.
- `git pull` - Fetches and merges changes from a remote repository.
- `git status` - Shows the status of changed files.
- `git log` - Shows commit history.
- `git branch` - Manages branches in the repository.
- `git merge <branch>` - Merges changes from a branch.
- `git checkout <branch>` - Switches to a branch.
- `git checkout -b <new_branch>` - Creates a new branch and switches to it.
- `git diff` - Shows differences between commits.
- `git rebase <branch>` - Cherry-picks commits onto another branch.
- `git stash` - Temporarily saves changes.
- `git stash apply` - Applies stashed changes.
- `git tag <name>` - Creates tags for commits.
- `git remote add <name> <url>` - Adds a remote repository.
- `git fetch <remote>` - Fetches changes from a remote repository.
- `git config --global user.name '[name]'` - Sets the user name.
- `git config --global user.email '[email address]'` - Sets the user email.
- `git reset --hard` - Reverts changes to the last commit.
- `git revert HEAD` - Reverts the last commit.
- `git show <ID>` - Shows details of a commit by ID.
- `git log --oneline` - Shows commit history in one line.

## Author

AlexTkDev - Project developer.

## License

MIT
