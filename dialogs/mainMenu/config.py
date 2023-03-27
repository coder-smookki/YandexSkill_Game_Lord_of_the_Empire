from utils.triggerHelper import isNewSession

def getConfig(event):
    config = {
    "ru-RU": {
        "tts":
            """ 
            Вы всегда сможете использовать функции: "Помощь", "Повторить ещё раз", "Что ты умеешь", "Выйти".
            Выберите нужную категорию, которая поможет вам.
            Новости.
            Студенческий офис.
            Первокурсникам.
            Расписание занятий.
            Общеуниверситетские модули в бакалавриате.
            Общеуниверситетские модули в магистратуре.
            Иностранному студенту.
            Библиотека.
            Учебные и методические издания.
            Стипендии.
            Шахматы.
            Викторина.
            Случайный факт.
            """,
        "buttons": [
            "Новости",
            "Студенческий офис",
            "Первокурсникам",
            "Расписание занятий",
            "Общеуниверситетские модули в бакалавриате",
            "Общеуниверситетские модули в магистратуре",
            "Иностранному студенту",
            "Библиотека",
            "Учебные и методические издания",
            "Стипендии",
            "Шахматы",
            "Викторина",
            "Случайный факт",
            "Сменить язык",
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "997614/e38bbfd1a2235c7229b1",
            "title": "КАТАЛОГ",
            "description":
                """
Выберите нужную категорию, которая поможет вам.
                """,
        },
    },
    "en-US": {
        "tts":
            """ 
            You can always use the functions: "Help", "Repeat again", "What can you do", "Exit".
            Choose the right category to help you.
            News.
            student office.
            Freshmen.
            Timetable of classes.
            University-wide undergraduate modules.
            University-wide modules in the magistracy.
            foreign student.
            Library.
            Educational and methodical publications.
            scholarships.
            Chess.
            Quiz.
            random fact.
            """,
        "buttons": [
            "News",
            "Student Office",
            "For freshmen",
            "Timetable of classes",
            "University-wide modules in undergraduate studies",
            "University-wide modules in the magistracy",
            "Foreign student",
            "Library",
            "Educational and methodical publications",
            "Scholarships",
            "Chess",
            "Quiz",
            "Random Fact",
            "Change language",
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "997614/e38bbfd1a2235c7229b1",
            "title": "CATALOG",
            "description":
                """
Choose the right category to help you.
                """,
        },
    },
}

    session_state = {"branch": "mainMenu"}

    lang = "ru-RU"
    
    if isNewSession(event):
        config["en-US"]['tts'] = 'Hi! This is an ITMO assistant skill. ' + config["en-US"]['tts']
        config["en-US"]['card']['description'] = 'Hi! This is ITMO Helper. ' + config["en-US"]['card']['description'] 

        config["ru-RU"]['tts'] = 'Привет! Это навык - ИТМО помощник. ' + config["ru-RU"]['tts']
        config["ru-RU"]['card']['description'] = 'Привет! Это навык - ИТМО помощник. ' + config["ru-RU"]['card']['description']

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
        "user_state_update": {"language": lang},
    }
