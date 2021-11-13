import random
log_list=["kaliri", "vko"]
pas_list=["2212", "6565"]

def login(n: str, l:list): #Проверяем, есть ли такой зарегистрированный пользователь. Внутренняя фунция. Поиск в списках.
    """Control login in list
       Return login in bool form
       :value parameter str n: requaired name
       :rtype: bool
    """
    if n in l:
        t=True
    else:
        t=False
    return t
     

def auto_reg(l,p): #Создаем пароль из random. Сохраняем его в pas_list
    """Building password
       Return password in str layout
       :rtype: str
    """

    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    pas = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    p.append(pas)
    print("Ваш пароль: ", pas)
    print("Вы успешно зарегистрированы!")
    return pas
  

def autor(l:list, p:list): # Авторизация, то что видет и самостоятельно заполняет пользователь.
    """ Control login and password in lists.
        Return True
    """

    n=input("Введите имя пользователя для авторизации: ")
    t=login(n,l)
    while t!=True:
       n=input("Введите имя пользователя еще раз: ")
       t=login(n,l)
    pas=input("Введите пароль: ")
    t=login(pas,p)
    if t==True and l.index(n)==p.index(pas):
        t=True
    else: 
        t=False
    return t

def reg(v: str, l:list, p:list): #регистрируем нового пользователя
    """Registration in social media
        Return login and password
        :value parameter str v: building password
        rtype: list, list
    """ 
    t=login(input("Введите имя пользователя: "),l)
    while t==True:
            t=login(input("Введите правильное имя пользователя: "),l)
    if v=="a":
        pas=auto_reg(l,p)
    else:
        self_reg(t,l,p)
    return l,p

def self_reg(t: str, l:list, p:list): #Добавляем нового пользователя с паролем
    """Add new user.
       Append and return pas_list and log_list
    """
    log_list.append(t)
    b=input("Введите пароль: ")
    pas_list.append(b)
    print("Регистрация успешно завершена!")
    return l, p

while 1:
    print("Регистрируемся - r, авторизируемся - a или выходим - v?")
    v=input("Вы выбрали: ")
    if v=="r":
        reg(input("Регистрация самостоятельная - y или автоматическая - a?"), log_list,pas_list)
    elif v=="a": 
        t=autor(log_list, pas_list) #true, false
        if t:
            print("Добро пожаловать!")
        else:
            v=input("Хотите зарегистрироваться - y?")
            if v=="y":
                print("Регистрация")
                reg(input("Авторизация самостоятельная или автоматическая?"), log_list,pas_list)
            
    else:
        break

