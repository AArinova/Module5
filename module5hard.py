
class Video:
    def __init__(self, *args, time_now = 0, adult_mode = False):
        print(args)
        self.title = args[0] #(заголовок, строка),
        self.duration = args[1] #(продолжительность, секунды),
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, *args):
        self.nickname = args[0]  # (имя пользователя, строка),
        self.password = args[1]  # (в хэшированном виде, число),
        self.age = args[2] #(возраст, число)

    def __str__(self):
        return f'Пользователь: {self.nickname}, пароль: {self.password} возраст: {self.age}'

class UrTube:
    users = []  # (список  объектов User),
    videos = []  # (список    объектов    Video),

    #def __init__(self):
     #   self.current_user = ''  # (текущий    пользователь, User)
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

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)