import time
import random
from termcolor import colored  # Убедитесь, что модуль установлен через pip install termcolor

# Глобалки
inventory = []
risk_level = 0
time_remaining = 30
news_feed = ["Правительство сообщает, что всё под контролем.", 
             "В стране процветает стабильность, утверждают СМИ."]

# персы
officials = [
    {
        "name": "Виктор Иванов",
        "position": "Министр финансов",
        "sins": ["Отмывание денег", "Коррупция в крупном размере"],
        "risk_level": "medium",
    },
    {
        "name": "Екатерина Сергеева",
        "position": "Министр пропаганды",
        "sins": ["Подстроенная пропаганда", "Сокрытие фактов"],
        "risk_level": "high",
    },
    {
        "name": "Алексей Смирнов",
        "position": "Глава разведки",
        "sins": ["Множественные убийства", "Пытки"],
        "risk_level": "critical",
    },
    {
        "name": "Ольга Петрова",
        "position": "Советник президента",
        "sins": ["Подделка документов", "Коррупция в малом размере"],
        "risk_level": "low",
    }
]

def print_slow(text, color=None, delay=0.03):
    """Эффект медленной печати с цветом."""
    if color:
        text = colored(text, color)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def boot_sequence():
    """Эффект запуска компьютера, как в фильмах."""
    print_slow("Initializing system...", "cyan", delay=0.05)
    time.sleep(1)
    print_slow("[OK] BIOS Check Complete", "green", delay=0.05)
    print_slow("[OK] Network Connection Established", "green", delay=0.05)
    print_slow("[OK] Encryption Layer Active", "green", delay=0.05)
    print_slow("[WARNING] Unauthorized Access Detected...", "yellow", delay=0.05)
    print_slow("Launching Darknet Interface...", "cyan", delay=0.05)
    time.sleep(1)
    print_slow("Welcome, Hacker. System Ready.", "cyan", delay=0.05)

def update_news(action):
    """Обновляет новости в зависимости от действий игрока."""
    global news_feed
    if action == "corruption":
        news_feed.append("В СМИ появилась информация о возможной коррупции в правительстве.")
    elif action == "propaganda":
        news_feed.append("Всплыли доказательства манипуляции общественным мнением через пропаганду.")
    elif action == "murder":
        news_feed.append("Независимые источники сообщают о причастности властей к убийствам.")
    elif action == "success":
        news_feed.append("Общественное мнение начинает требовать расследования против правительства.")
    elif action == "failure":
        news_feed.append("Хакера поймали, но доказательств недостаточно для дела.")

def display_news():
    """Показывает текущие новости."""
    print_slow("\n=== Последние новости ===", "cyan")
    for news in news_feed[-3:]:
        print_slow(f"- {news}", "yellow")

def display_officials():
    """Вывод информации о коррумпированных чиновниках."""
    print_slow("\n=== Файлы правительства ===", "cyan")
    for official in officials:
        color = "green" if official["risk_level"] == "low" else "yellow" if official["risk_level"] == "medium" else "red"
        print_slow(f"- {official['name']} ({official['position']})", color)
        for sin in official["sins"]:
            print_slow(f"  * {sin}", color)
    print()

def decrypt_file():
    """Мини-задача: расшифровка файла."""
    print_slow("Вы пытаетесь расшифровать файл с секретными данными.", "cyan")
    encrypted_message = "Uifsf jt b tfdsfu tfswfs"
    print_slow(f"Зашифрованное сообщение: {encrypted_message}", "yellow")
    print_slow("Подсказка: шифр Цезаря со сдвигом на -1.", "green")
    answer = input("Введите расшифрованное сообщение: ").strip()

    if answer.lower() == "there is a secret server":
        print_slow("Расшифровка успешна! Вы получили важные данные.", "green")
        inventory.append("Расшифрованный файл")
        update_news("corruption")
    else:
        print_slow("Неверно. Шифрование осталось неразгаданным.", "red")
        update_news("failure")

def find_keyword():
    """Мини-задача: поиск ключевого слова."""
    print_slow("Вы анализируете огромный лог серверов в поисках ключевого слова.", "cyan")
    log_data = ["access_granted", "error", "restart", "SECRET_KEY_FOUND", "logout", "login"]
    print_slow(f"Логи: {', '.join(log_data)}", "yellow")
    print_slow("Найдите слово, указывающее на ключ доступа.", "green")
    answer = input("Введите ключевое слово: ").strip()

    if answer == "SECRET_KEY_FOUND":
        print_slow("Вы нашли ключ! Доступ открыт.", "green")
        inventory.append("Секретный ключ")
        update_news("propaganda")
    else:
        print_slow("Неверный ввод. Ключ остался не найден.", "red")
        update_news("failure")

def validate_password():
    """Мини-задача: подбор пароля."""
    print_slow("Вы пытаетесь подобрать пароль к серверу.", "cyan")
    password = "Pa$$w0rd"
    attempts = 3
    print_slow("Подсказка: Пароль содержит символы $, цифру 0, и начинается с 'P'.", "yellow")
    while attempts > 0:
        answer = input(f"Введите пароль (осталось попыток: {attempts}): ").strip()
        if answer == password:
            print_slow("Пароль верный! Вы получили доступ к серверу.", "green")
            inventory.append("Доступ к серверу")
            update_news("murder")
            return
        else:
            attempts -= 1
            print_slow("Неверно. Попробуйте снова.", "red")
    print_slow("Попытки закончились. Доступ заблокирован.", "red")
    update_news("failure")

def hack_servers():
    """Выполнение взлома серверов."""
    global risk_level, time_remaining
    print_slow("\nВы подключаетесь к серверу...", "yellow")
    time.sleep(2)

    
    target = random.choice(officials)
    print_slow(f"Вы атакуете сервер {target['name']} ({target['position']}).", "cyan")
    print_slow(f"Уровень риска: {target['risk_level']}.", "red" if target['risk_level'] == "critical" else "yellow" if target['risk_level'] == "medium" else "green")
    time.sleep(1)

    
    tasks = [decrypt_file, find_keyword, validate_password]
    task = random.choice(tasks)
    task()

    risk_increase = random.randint(10, 25)
    risk_level += risk_increase
    time_remaining -= 5
    check_risk()
    main_menu()

def talk_to_prosecutor():
    """Связь с прокурором."""
    print_slow("\nВы связываетесь с прокурором.", "cyan")
    print_slow("'Привет! Ты что-то нашёл?'", "cyan")
    print_slow("1. Какие доказательства приоритетны?", "green")
    print_slow("2. Как поступить с риском?", "yellow")
    print_slow("3. Вернуться в главное меню", "green")

    choice = input("Ваш выбор (1-3): ").strip()
    if choice == "1":
        print_slow("'Главное — найти следы крупной коррупции и пропаганды. Без этого дела не выиграть.'", "cyan")
    elif choice == "2":
        print_slow("'Если уровень риска поднимется выше 70%, тебе лучше остановиться и сбежать.'", "red")
    elif choice == "3":
        main_menu()
        return
    else:
        print_slow("Неверный выбор. Попробуйте снова.", "red")
    talk_to_prosecutor()

def check_risk():
    """Проверка уровня риска."""
    if risk_level >= 70:
        print_slow("Ваш риск достиг критического уровня! Нужно немедленно принять меры.", "red")
    elif risk_level >= 40:
        print_slow("Уровень риска растёт. Будьте осторожны.", "yellow")

def main_menu():
    """Главное меню игры."""
    global time_remaining
    if time_remaining <= 0:
        print_slow("Время истекло! Правительство нашло вас. Вы проиграли.", "red")
        return

    print_slow("\n=== Главное меню ===", "cyan")
    print_slow("1. Связаться с прокурором", "green")
    print_slow("2. Начать взлом серверов", "yellow")
    print_slow("3. Изучить найденные файлы", "green")
    print_slow("4. Просмотреть новости", "green")
    print_slow(f"Оставшееся время: {time_remaining} минут. Текущий риск: {risk_level}%", "yellow")

    choice = input("\nВаш выбор (1-4): ").strip()
    if choice == "1":
        talk_to_prosecutor()
    elif choice == "2":
        hack_servers()
    elif choice == "3":
        display_officials()
    elif choice == "4":
        display_news()
    else:
        print_slow("Неверный выбор. Попробуйте снова.", "red")
    main_menu()

def start_game():
    """Запуск игры."""
    global inventory, risk_level, time_remaining
    inventory = []  # Инвентарь
    risk_level = 0  # Уровень риска
    time_remaining = 30  # Время на завершение игры

    boot_sequence()
    print_slow("\n=== Добро пожаловать в игру: \"Киберборец\" ===", "cyan")
    print_slow("Вы — хакер, стремящийся разоблачить коррумпированное правительство.", "cyan")
    print_slow("Ваша задача: собрать доказательства и передать их прокурору.", "cyan")
    print_slow("Будьте осторожны: каждое действие увеличивает риск быть пойманным.", "red")
    main_menu()

# Запуск игры
start_game()