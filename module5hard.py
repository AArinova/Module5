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
        self.password = args[1]
        self.age = args[2] #(возраст, число)

    def __str__(self):
        return f'Пользователь: {self.nickname}, пароль: {self.password} возраст: {self.age}'

    def __eq__(self, other):
        if( isinstance( other, User)):
            if self.nickname == other.nickname and self.age == other.password and self.age == other.age:
                return True
            else:
                return False
    def get_nick(self):
        return self.nickname

class UrTube:

    users = []  # список  объектов User)
    videos = []  # список объектов Video)
    current_user = None

    def __str__(self):
        return self.current_user

    def register( self, nick_name, password, age):
        nick_list = []
        for each in self.users:
            nick_list.append(each.get_nick())
        #print('Ники', nick_list )
        if nick_name in nick_list:
            print(f"Пользователь {nick_name} уже существует")
        else:
            new_user = User(nick_name, password, age)
            self.users.append(new_user)
            self.current_user = new_user

        return self

    def log_in(self, nickname, password):
        is_found = False
        for each in self.users:
            if nickname == each.nickname and password == each.password:
                is_found = True
                self.current_user = each
                break
            else:
                continue
        if is_found == False:
            print(f'Пользователь {nickname} не существует!')

    def log_out(self):
        self.current_user = None
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
        is_found = False
        for item in self.videos:
            if item.title == find_title:
                is_found = True
                return item
            else:
                continue
        if is_found == False:
            return None
    def watch_video(self, video_title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
        else:
            found = self.get_video(video_title)
            if found != None:
                if found.adult_mode and self.current_user.age < 18:
                    print( self.current_user.nickname, 'Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print(f'Идёт видео \'{found.title}\'.')
                    for i_time in range(0, found.duration):
                        print(f"Идёт {i_time} секунда видео.")
                        time.sleep(1)
                    found.time_now = 0
                    print(f'Конец видео \"{found.title}\".')
            else:
                print('Нет такого видео.')

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
print(ur.current_user)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

#Тестирование методов log_in, log_out
# ur.log_in('musya_pupkina', 'F8098FM8fjm9jmi2')
# print('\nСейчас пользователь: ',ur.current_user)
# ur.log_out()
# print('\nСейчас пользователь: ',ur.current_user)

#Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')