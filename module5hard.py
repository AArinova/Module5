
class Video:
    def __init__(self, *args, time_now = 0, adult_mode = False):
        self.title = args[0] #(заголовок, строка),
        self.duration = args[1] #(продолжительность, секунды),
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}, длительность: {self.duration}, возрастное ограничение: {self.adult_mode}'

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
                    #print(each)

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
print(v1)
# Добавление видео
ur.add(v1, v2)
print(ur.videos)

# Проверка поиска
#print(ur.get_videos('лучший'))
#print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
#ur.watch_video('Лучший язык программирования 2024 года!')