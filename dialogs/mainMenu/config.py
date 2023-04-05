from utils.triggerHelper import *
from utils.responseHelper import *
from utils.dbHandler import *
from utils.globalStorage import *


def getConfig(event):
    config = {
        "tts":
            """ 
Вы в главном меню.
Скажите или нажмите кнопку.
Играть - чтобы начать игру.
Сбросить сохранение - чтобы стереть ваш игровой процесс. При этом ваша статистика не будет сброшена.
Повторить ещё раз - чтобы снова послушать текст.
Что ты умеешь? - чтобы узнать, что делает навык.
Помощь - чтобы узнать ответ на интересующие вопросы и также для связи с разработчиками игры.
Выход - чтобы выйти из навыка.
            """,
        "buttons": [
            'Играть',
            'Статистика',
            "Помощь",
            "Что ты умеешь?",
            'Сбросить сохранение',
            "Повторить ещё раз",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1533899/dcca2fdc4295374a69bc",
            "title": "ГЛАВНОЕ МЕНЮ",
            "description":
                """
Выберите нужную категорию, которая поможет вам.
                """,
        },
    }

    session_state = {"branch": "mainMenu"}

    config = {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }

    conn = globalStorage["mariaDBconn"]

    config['user_state_update'] = {}
    config['user_state_update']['addStats'] = []

    if haveGlobalState(event, 'addStats') and type(getGlobalState(event, 'addStats')) == list:
        stats = getGlobalState(event, 'addStats')
        for stat in stats:
            print('mainMenuStat')
            increaseStat(conn, getUserId(event), deaths=stat[0], openEnds=stat[1])
        if not 'user_state_update' in config:
            config['user_state_update'] = {}
        config['user_state_update']['addStats'] = []

    return config
