import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.logged_in = False
        self.videos = []
        self.users = []
        self.current_user = None
        self.current_user_age = None
        self.current_video = None
        self.current_video_duration = None

    def log_in(self, nickname, password):  # Готово
        for user in self.users:
            if user[0] == nickname and user[1] == password:
                self.current_user = user[0]
                self.current_user_age = user[2]
                self.logged_in = True
                return

    def register(self, nickname, password, age):  # Готово
        for user in self.users:
            if user[0] == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = nickname, password, age
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):  # Готово
        for user in self.users:
            self.current_user = None
            return

    def add(self, *args):  # Готово
        for video in args:
            video_exist = False
            for title in self.videos:
                if title == video.title:
                    video_exist = True
                    break
            if not video_exist:
                self.videos.append(video)

    def get_videos(self, search_word):  # Готово
        searching = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                searching.append(video.title)
        return searching

    def watch_video(self, video_title):
        if not self.logged_in:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video_title.lower() in video.title.lower():
                if self.current_user_age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                else:
                    self.current_video = video
                    for i in range(1, video.duration + 1):
                        print(i, end=" ")
                        time.sleep(1)
                    print("Конец видео")
                    self.current_video = None
                    return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
