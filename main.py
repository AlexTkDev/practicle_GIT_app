from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock

# Команды Git и их описания
commands = {
    "git init": "Создает новый репозиторий.",
    "git clone <url>": "Клонирует существующий репозиторий.",
    "git add <file>": "Добавляет файлы к следующему коммиту.",
    "git commit -m 'message'": "Фиксирует изменения с комментарием.",
    "git push": "Отправляет коммиты на удаленный репозиторий.",
    "git pull": "Получает и объединяет изменения из удаленного репозитория.",
    "git status": "Показывает статус измененных файлов.",
    "git log": "Показывает историю коммитов.",
    "git branch": "Управление ветками в репозитории.",
    "git merge <branch>": "Объединяет изменения из ветки.",
    "git checkout <branch>": "Переключение на ветку.",
    "git checkout -b <new_branch>": "Создает новую ветку и переключается на нее.",
    "git diff": "Показывает разницу между коммитами.",
    "git rebase <branch>": "Переносит коммиты на другую ветку.",
    "git stash": "Временно сохраняет изменения.",
    "git stash apply": "Применяет сохраненные изменения.",
    "git tag <name>": "Создает теги для коммитов.",
    "git remote add <name> <url>": "Добавляет удаленный репозиторий.",
    "git fetch <remote>": "Получает изменения из удаленного репозитория.",
    "git config --global user.name '[имя]'": "Устанавливает имя пользователя.",
    "git config --global user.email '[адрес электронной почты]'": "Устанавливает email пользователя.",
    "git reset --hard": "Откатывает изменения до последнего коммита.",
    "git revert HEAD": "Отменяет последний коммит.",
    "git show <ID>": "Показывает детали коммита по ID.",
    "git log --oneline": "Показывает историю коммитов в одну строку."
}

# Сюжетные задания
missions = {
    "easy": [
        {"task": "Инициализируйте новый репозиторий", "commands": ["git init"]},
        {"task": "Добавьте файл в отслеживаемые", "commands": ["git add <file>"]},
        {"task": "Посмотрите статус репозитория", "commands": ["git status"]},
        {"task": "Сделайте коммит с сообщением", "commands": ["git commit -m 'message'"]},
        {"task": "Покажите историю коммитов", "commands": ["git log"]},
        {"task": "Создайте новую ветку и переключитесь на неё", "commands":
            ["git checkout -b <new_branch>"]},
    ],
    "medium": [
        {"task": "Клонируйте репозиторий", "commands": ["git clone <url>"]},
        {"task": "Добавьте изменения и сделайте коммит", "commands": ["git add <file>",
                                                                      "git commit -m 'message'"]},
        {"task": "Переключитесь на ветку", "commands": ["git checkout <branch>"]},
        {"task": "Покажите разницу между коммитами", "commands": ["git diff"]},
        {"task": "Сохраните изменения и примените их", "commands": ["git stash", "git stash apply"]},
        {"task": "Создайте тег для коммита", "commands": ["git tag <name>"]},
        {"task": "Добавьте удалённый репозиторий", "commands": ["git remote add <name> <url>"]},
        {"task": "Получите изменения из удалённого репозитория", "commands": ["git fetch <remote>"]},
    ],
    "hard": [
        {"task": "Отправьте изменения на удалённый репозиторий", "commands": ["git push"]},
        {"task": "Получите и объедините изменения из удалённого репозитория", "commands": ["git pull"]},
        {"task": "Создайте новую ветку, переключитесь на неё и объедините изменения",
         "commands": ["git checkout -b <new_branch>", "git merge <branch>"]},
        {"task": "Перенос коммитов на другую ветку", "commands": ["git rebase <branch>"]},
        {"task": "Откатите изменения до последнего коммита", "commands": ["git reset --hard"]},
        {"task": "Отмените последний коммит", "commands": ["git revert HEAD"]},
        {"task": "Покажите детали коммита по ID", "commands": ["git show <ID>"]},
        {"task": "Покажите историю коммитов в одну строку", "commands": ["git log --oneline"]},
        {"task": "Установите имя и email пользователя", "commands":
            ["git config --global user.name '[имя]'",
             "git config --global user.email '[адрес электронной почты]'"]},
    ]
}


# Стильный главный экран
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        label = Label(text="Изучение и практика Git", font_size=32, bold=True, size_hint=(1, 0.2))
        start_button = Button(text="Начать игру", size_hint=(1, 0.2), on_release=self.start_game)
        about_button = Button(text="О приложении", size_hint=(1, 0.2), on_release=self.about)
        exit_button = Button(text="Выход", size_hint=(1, 0.2), on_release=self.exit_app)

        # Применение стилей
        for widget in [start_button, about_button, exit_button]:
            widget.background_color = (0.5, 0.7, 0.9, 1)
            widget.color = (0, 0, 0, 1)

        layout.add_widget(label)
        layout.add_widget(start_button)
        layout.add_widget(about_button)
        layout.add_widget(exit_button)
        self.add_widget(layout)

    def start_game(self, instance):
        self.manager.current = 'level_selection'

    def about(self, instance):
        self.manager.current = 'about'

    def exit_app(self, instance):
        App.get_running_app().stop()


# Экран выбора уровня
class LevelSelection(Screen):
    def __init__(self, **kwargs):
        super(LevelSelection, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        label = Label(text="Выберите уровень", font_size=32, bold=True, size_hint=(1, 0.2))
        easy_button = Button(text="Начальный уровень", size_hint=(1, 0.2), on_release=self.start_easy)
        medium_button = Button(text="Средний уровень", size_hint=(1, 0.2), on_release=self.start_medium)
        hard_button = Button(text="Продвинутый уровень", size_hint=(1, 0.2), on_release=self.start_hard)
        back_button = Button(text="Назад", size_hint=(1, 0.2), on_release=self.back_to_menu)

        # Применение стилей
        for widget in [easy_button, medium_button, hard_button, back_button]:
            widget.background_color = (0.5, 0.7, 0.9, 1)
            widget.color = (0, 0, 0, 1)

        layout.add_widget(label)
        layout.add_widget(easy_button)
        layout.add_widget(medium_button)
        layout.add_widget(hard_button)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def start_easy(self, instance):
        self.manager.current = 'game'
        self.manager.get_screen('game').start_level('easy')

    def start_medium(self, instance):
        self.manager.current = 'game'
        self.manager.get_screen('game').start_level('medium')

    def start_hard(self, instance):
        self.manager.current = 'game'
        self.manager.get_screen('game').start_level('hard')

    def back_to_menu(self, instance):
        self.manager.current = 'main_menu'


# Экран игры с современным интерфейсом и анимациями
class GameScreen(Screen):
    level = StringProperty('')
    score = NumericProperty(0)
    mission_index = NumericProperty(0)
    command_attempts = NumericProperty(0)

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        self.label = Label(text="", font_size=24, size_hint=(1, 0.1))
        self.mission_label = Label(text="", font_size=18, size_hint=(1, 0.2))
        self.input = TextInput(hint_text="Введите команду Git", multiline=False, size_hint=(1, 0.1))
        self.input.bind(on_text_validate=self.check_answer)
        self.output = Label(text="", size_hint=(1, 0.4))
        self.score_label = Label(text=f"Счет: {self.score}", font_size=18, size_hint=(1, 0.1))
        self.back_button = Button(text="Назад", size_hint=(1, 0.1), on_release=self.back_to_levels)

        # Применение стилей
        for widget in [self.input, self.back_button]:
            widget.background_color = (0.5, 0.7, 0.9, 1)
            widget.color = (0, 0, 0, 1)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.mission_label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.output)
        self.layout.add_widget(self.score_label)
        self.layout.add_widget(self.back_button)
        self.add_widget(self.layout)

    def start_level(self, level):
        self.level = level
        self.score = 0
        self.mission_index = 0
        self.command_attempts = 0
        self.load_mission()

    def load_mission(self):
        if self.mission_index < len(missions[self.level]):
            mission = missions[self.level][self.mission_index]
            self.label.text = f"Уровень: {self.level.capitalize()}"
            self.mission_label.text = mission["task"]
            self.output.text = ""
            self.input.text = ""
            self.command_attempts = 0
        else:
            self.mission_label.text = "Поздравляем! Вы завершили уровень!"
            self.output.text = ""
            self.input.disabled = True

    def check_answer(self, instance):
        mission = missions[self.level][self.mission_index]
        answer = self.input.text.strip()

        if answer in mission["commands"]:
            self.output.text = "Правильно!"
            self.score += 10
            self.mission_index += 1
            Clock.schedule_once(lambda dt: self.load_mission(), 1)
        else:
            self.command_attempts += 1
            if self.command_attempts >= 2:
                self.output.text = f"Неправильно. Подсказка: {mission["commands"]}"
            else:
                self.output.text = "Неправильно, попробуйте снова."
            self.score -= 2
        self.score_label.text = f"Счет: {self.score}"

    def back_to_levels(self, instance):
        self.manager.current = 'level_selection'


# Экран с информацией о приложении
class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        label = Label(text="О приложении", font_size=32, bold=True, size_hint=(1, 0.2))
        info_label = Label(text="Это приложение разработано для изучения и практики команд Git.\n"
                                "Оно включает в себя разные уровни сложности.\n"
                                "Приятного обучения!\n"
                                "by AlexTkDev",
                           font_size=18, size_hint=(1, 0.6))
        back_button = Button(text="Назад", size_hint=(1, 0.2), on_release=self.back_to_menu)

        # Применение стилей
        for widget in [back_button]:
            widget.background_color = (0.5, 0.7, 0.9, 1)
            widget.color = (0, 0, 0, 1)

        layout.add_widget(label)
        layout.add_widget(info_label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def back_to_menu(self, instance):
        self.manager.current = 'main_menu'


# Управление экранами
class GitLearningApp(App):
    def build(self):
        sm = ScreenManager(transition=WipeTransition())
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(LevelSelection(name='level_selection'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(AboutScreen(name='about'))
        return sm


if __name__ == '__main__':
    GitLearningApp().run()
