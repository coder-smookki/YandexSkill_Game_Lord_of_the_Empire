def getConfig(event):
    config = {
        "tts": """
Данный навык представляет собой карточную квест-игру. Где ты принимаешь на себя роль владыки и управляешь своим государством. 
Тебе предстоит делать сложные решения, которые приведут тебя и твоё государство к определенному результату. 
Для того, чтоб начать игру скажите или нажмите на кнопку, Играть. 
Выбор можно определить с помощью кнопок на нижней панели или голосового ввода. 
Приятного правления!

Варианты ответов которые доступны вам сейчас:
Играть. Повторить ещё раз. Что ты умеешь?. Назад. Выход.""",

        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1533899/d371aab5224c91137cfc",
            "title": "КАК ПОЛЬЗОВАТЬСЯ?",
            "description": """
            Данный навык представляет собой карточную квест-игру, где ты принимаешь на себя роль владыки и управляешь своим государством, тебе предстоит делать сложные решения, которые приведут тебя и твоё государство к определенному результату.
            Для того, чтоб начать игру нажми на кнопку "Играть", выбор можно определить с помощью кнопок на нижней панели или голосового ввода. Приятного правления!
            """,
        },
    }

    session_state = {"branch": "howToUse"}

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }