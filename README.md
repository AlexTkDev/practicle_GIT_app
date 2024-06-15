# Git Learning Game

Эта игра предназначена для изучения и практики команд Git с использованием интерактивного подхода. Проект создан с использованием фреймворка Kivy для создания графического интерфейса пользователя.

## Оглавление

- [Особенности](#особенности)
- [Установка](#установка)
- [Запуск игры](#запуск-игры)
- [Структура проекта](#структура-проекта)
- [Миссии и Команды](#миссии-и-команды)
- [Автор](#автор)
- [Лицензия](#лицензия)

## Особенности

- Интерактивный GUI для изучения команд Git.
- Разные уровни сложности миссий.
- Подсказки при неправильных ответах.
- Полное покрытие основных команд Git.

## Установка

Для установки необходимых зависимостей и запуска игры выполните следующие шаги:

   1. Клонируйте репозиторий:

      git clone https://github.com/AlexTkDev/practicle_GIT_app.git
      cd practicle_GIT_app

   3. Создайте и активируйте виртуальное окружение:

      python -m venv venv
      source venv/bin/activate

      venv\Scripts\activate


   4. Установите зависимости:

         pip install -r requirements.txt

## Запуск игры

Для запуска игры используйте следующую команду:
   
   python main.py
   


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
