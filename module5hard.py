import time
class Video:
    def __init__(self, *args, time_now = 0, adult_mode = False):
        self.title = args[0] #(заголовок, строка),
        self.duration = args[1] #(продолжительность, секунды),
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}, длительность: {self.duration}, возрастное ограничение: {self.adult_mode}'

    def __repr__(self): #вывод списка
        return self.__str__()

    def get_name(self):
        return self.title
class User:
    def __init__(self, *args):
        self.nickname = args[0]  # (имя пользователя, строка),
        self.password = args[1]  # (в хэшированном виде, число),
        self.age = args[2] #(возраст, число)

    def __str__(self):
        return f'Пользователь: {self.nickname}, пароль: {self.password} возраст: {self.age}'

class UrTube:

    users = []  # (список  объектов User),
    videos = []  # (список объектов Video),

    def __str__(self):
        return self.current_user
    def register( self, nick_name, password, age):
        if nick_name in self.users:
            print(f"Пользователь {nick_name} уже существует")
        else:
            new_user = User(nick_name, password, age)
            self.users.append(new_user)
            self.current_user = new_user
        return self

    def add(self, *args):
        for each in args:
            if isinstance(each, Video):
                if each in self.videos:
                    print('Уже есть видео с таким названием.')
                else:
                    self.videos.append(each)

    def get_videos(self, find_word):
        found_videos = []
        find_word = find_word.lower()
        for item in self.videos:
            if find_word in item.title.lower():
                found_videos.append(item.title)
        return found_videos

    def get_video(self, find_title): # поиск видео по названию
        for item in self.videos:
            if item.title == find_title:
                return item
            else:
                continue
    def watch_video(self, video_title):
        found = self.get_video(video_title)
        print(f'Идёт видео \'{found.title}\'.')
        for i_time in range(0, found.duration):
            print(f"Идёт {i_time} секунда видео.")
            time.sleep(i_time)
        found.time_now = 0
        print(self)
        print(f'Закончилось видео \"{found.title}\".')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print(*ur.videos)

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
#ur.watch_video('Лучший язык программирования 2024 года!')