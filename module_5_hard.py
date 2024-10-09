from time import sleep

# Class User ===========================================================================================================

class User:
    def __init__(self, name, password, age):
        self.name = name
        self.password = hash(password)
        self.age = age

# Class Video ==========================================================================================================

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

# Class UrTube =========================================================================================================

class UrTube:
    users = []
    videos = []
    current_user = None
    
#========================================================
    def log_in(self, name, password):
        for user in self.users:
            if user.name == name:
                print('логин верный')
                if user.password == hash(password):
                    print('пароль подтвержден')
                    self.current_user = user
                    return 0
        print('логин не найден')
        self.log_out()

# ========================================================
    def log_out(self):
        self.current_user = None
        print('log_out')

# =======================================================
    def register(self, name, password, age):
        user_new = User(name,password,age)
        if not self.users:
            self.users.append(user_new)
            self.current_user = user_new
        else:
            for user in self.users:
                if user.name == user_new.name:
                    print('такой пользователь уже существует')
                    # self.log_out()
                    return False
                else:
                    self.users.append(user_new)
                    self.current_user = user_new
                    print(f'пользователь {user_new.name} добавлен')
                    return True

# =======================================================
    def add(self, *args): # принимает не ограниченное количество видео и добавляет в videos если такого нет
        # print(self.videos)
        for video in args:
            if video.title not in self.videos:
                self.videos.append(video)

# =======================================================
    def get_videos(self, text):
        text_lower = text.lower()
        find_film = []
        for film in self.videos:
            if text_lower in film.title.lower():
                find_film.append(film.title)
                # print(f'найден фильм {film.title}')
        return find_film

# =======================================================
    def watch_video(self, name_film):
        if self.current_user == None:
            print('Войдите в аккаунт что бы смотреть видео')
            return False
        for film in self.videos:
            if film.title == name_film:
                if film.adult_mode and self.current_user.age <= 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return False
                while film.time_now < film.duration:
                    print(film.time_now, end = '.')
                    film.time_now += 1
                    sleep(0.1)
                print(' Конец видео')
                film.time_now = 0
                return True
        print('такого фильма нет')


#                                 ===== Test Case =====

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
print('проверка входа')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.name)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

while True:
    choice = int(input('выберите: \n0 - для выхода из программы\n'))
    if choice == 0:
        print('program execution completed')
        break
    elif choice == 1:
        ur.register(input('name: '), input('password: '), int(input('age: ')))
    elif choice == 2:
        ur.log_in(input('login: '), input('password: '))
    elif choice == 3:
        ur.log_out()
    elif choice == 4:
        if ur.current_user != None:
            print(ur.current_user.name)
        else: print('none')







