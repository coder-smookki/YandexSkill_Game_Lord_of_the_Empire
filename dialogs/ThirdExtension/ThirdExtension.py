ThirdExtension = """
    "Командир Родион $ Военные жалуется на маленькую зарплату, нужно повысить плату // Повысить // Отказать //  // None"
    true:
        "Кондрат $ Король, на улицах города бушует новая болезнь, стоит ли лечить население? // Да // Нет //  // None"
        true:
            "Маг-целитель Хрисанф $ Я хочу провести опыт для создания нового лекарства. Вы поможете? // Да // Нет //  // None"
            true:
                "Кондрат $ Владыка, Хрисанф в ходе опыта создал зомби-вирус, который распространяется! // Что... // Что... //  // None"
                true:
                    "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  //None"
                false:
                    "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
            
            false:
                "{FourthExtension}"         
        false:
            "Кондрат $ Люди бунтуют, болезнь оказалась очень опасной, они недовольны, тем что мы никак не реагируем // Командир! // Окажите помощь всем нуждающимся! //  // None"
            true:
                "*Вы одурманены адским зельем на улицах города, среди разгула и восстания. Вы стараетесь не потерять свою голову, но это все равно случается* // Выйти // None //  // None"
            false:
                "Маг-целитель Хрисанф $ Я хочу провести опыт для создания нового лекарства. Вы поможете? // Да // Нет //  // None"
                true:
                    "Кондрат $ Владыка, Хрисанф в ходе опыта создал зомби-вирус, который распространяется! // Что... // Что... //  // None"
                    true:
                        "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                    false:
                        "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                false:
                    "{FourthExtension}"
    false:
        "Кондрат $ Король, на улицах города бушует новая болезнь, стоит ли лечить население? // Да // Нет //  // None"
        true:
            "Маг-целитель Хрисанф $ Я хочу провести опыт для создания нового лекарства. Вы поможете? // Да // Нет //  // None"
            true:
                "Кондрат $ Владыка, Хрисанф в ходе опыта создал зомби-вирус, который распространяется! // Что... // Что... //  // None"
                true:
                    "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                false:
                    "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
            false:
                "{FourthExtension}"
        
        false:
            "Кондрат $ Люди бунтуют, болезнь оказалась очень опасной, они недовольны, тем что мы никак не реагируем // Командир! // Окажите помощь всем нуждающимся! //  // None"
            true:
                "*Вы одурманены адским зельем на улицах города, среди разгула и восстания. Вы стараетесь не потерять свою голову, но это все равно случается* // Выйти // None //  // None"
            false:
                "Маг-целитель Хрисанф $ Я хочу провести опыт для создания нового лекарства. Вы поможете? // Да // Нет //  // None"
                true:
                    "Кондрат $ Владыка, Хрисанф в ходе опыта создал зомби-вирус, который распространяется! // Что... // Что... //  // None"
                    true:
                        "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                    false:
                        "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"            
                false:
                    "{FourthExtension}"
"""

