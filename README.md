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

***

# Git Learning Game

Эта игра предназначена для изучения и практики команд Git с использованием интерактивного подхода. Проект создан с использованием фреймворка Kivy для создания графического интерфейса пользователя.

## Особенности

- Интерактивный GUI для изучения команд Git.
- Разные уровни сложности миссий.
- Подсказки при неправильных ответах.
- Полное покрытие основных команд Git.

## Установка

Для установки необходимых зависимостей и запуска игры выполните следующие шаги:

   1. Клонируйте репозиторий:
```bash
   git clone https://github.com/AlexTkDev/practicle_GIT_app.git

   cd practicle_GIT_app
```

   3. Создайте и активируйте виртуальное окружение:
```bash
   python -m venv venv
   source venv/bin/activate

   venv\Scripts\activate
```

   4. Установите зависимости:
```bash
    pip install -r requirements.txt
```

## Запуск игры

Для запуска игры используйте следующую команду:
```bash   
   python main.py
```


## Структура проекта

- `main.py` - Главный файл для запуска приложения.
- `requirements.txt` - Файл с зависимостями проекта.
- `README.md` - Документация проекта.

## Миссии и Команды

### Миссии

Миссии разделены на три уровня сложности:

#### easy

- Инициализация нового репозитория
- Добавление файла в отслеживаемые
- Просмотр статуса репозитория
- Создание коммита с сообщением
- Просмотр истории коммитов
- Создание новой ветки и переключение на неё

#### medium

- Клонирование репозитория
- Добавление изменений и создание коммита
- Переключение на ветку
- Просмотр разницы между коммитами
- Сохранение изменений и их применение
- Создание тега для коммита
- Добавление удаленного репозитория
- Получение изменений из удаленного репозитория

#### hard

- Отправка изменений на удалённый репозиторий
- Получение и объединение изменений из удаленного репозитория
- Создание новой ветки, переключение на неё и объединение изменений
- Перенос коммитов на другую ветку
- Откат изменений до последнего коммита
- Отмена последнего коммита
- Просмотр деталей коммита по ID
- Просмотр истории коммитов в одну строку
- Установка имени и email пользователя

### Команды

Полный список команд, используемых в игре:

- `git init` - Создает новый репозиторий.
- `git clone <url>` - Клонирует существующий репозиторий.
- `git add <file>` - Добавляет файлы к следующему коммиту.
- `git commit -m 'message'` - Фиксирует изменения с комментарием.
- `git push` - Отправляет коммиты на удаленный репозиторий.
- `git pull` - Получает и объединяет изменения из удаленного репозитория.
- `git status` - Показывает статус измененных файлов.
- `git log` - Показывает историю коммитов.
- `git branch` - Управление ветками в репозитории.
- `git merge <branch>` - Объединяет изменения из ветки.
- `git checkout <branch>` - Переключение на ветку.
- `git checkout -b <new_branch>` - Создает новую ветку и переключается на нее.
- `git diff` - Показывает разницу между коммитами.
- `git rebase <branch>` - Переносит коммиты на другую ветку.
- `git stash` - Временно сохраняет изменения.
- `git stash apply` - Применяет сохраненные изменения.
- `git tag <name>` - Создает теги для коммитов.
- `git remote add <name> <url>` - Добавляет удаленный репозиторий.
- `git fetch <remote>` - Получает изменения из удаленного репозитория.
- `git config --global user.name '[имя]'` - Устанавливает имя пользователя.
- `git config --global user.email '[адрес электронной почты]'` - Устанавливает email пользователя.
- `git reset --hard` - Откатывает изменения до последнего коммита.
- `git revert HEAD` - Отменяет последний коммит.
- `git show <ID>` - Показывает детали коммита по ID.
- `git log --oneline` - Показывает историю коммитов в одну строку.

## Автор

AlexTkDev - разработчик проекта.

## Лицензия

MIT
