ThirdExtension = """
    "Командир Родион $ Военные жалуются на маленькую зарплату, нужно повысить плату. // Повысить // Отказать // 0 +10 0 -5 $ 0 -15 0 10 // None"
    true:
        "Кондрат $ Король, на улицах города бушует новая болезнь, стоит ли лечить население? // Да // Нет // 0 0 5 0 $ 0 0 -20 0 // None"
        true:
            "Маг-целитель Хрисанф $ Я хочу провести опыт по созданию нового лекарства. Вы поможете? // Да // Нет // 0 0 0 0 $ +10 0 -5 0 // None"
            true:
                "Кондрат $ Владыка, Хрисанф в ходе опыта создал зомби-вирус, который распространяется! // Что же... // Как... // 0 0 0 0 $ 0 0 0 0 // None"
                true:
                    "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  //None"
                false:
                    "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
            false:
                "{FourthExtension}"
        false:
            "Кондрат $ Люди бунтуют, болезнь оказалась очень опасной, они недовольны тем, что мы никак не реагируем. // Командир! // Окажите поддержку всем нуждающимся! // 0 +100 -100 0 $ 0 0 0 0 // None"
            true:
                "*Вы одурманены адским зельем на улицах города, среди разгула и восстания. Вы стараетесь не потерять свою голову, но это все равно случается.* // None // None // 0 0 0 0 // None"
            false:
                "Маг-целитель Хрисанф $ Я хочу провести опыт по созданию нового лекарства. Вы поможете? // Да // Нет // 0 0 0 0 $ +10 0 -5 0 // None"
                true:
                    "Кондрат $ Владыка, Хрисанф в ходе опыта создал зомби-вирус, который распространяется! // Что же... // Как... // 0 0 0 0 $ 0 0 0 0 // None"
                    true:
                        "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                    false:
                        "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                false:
                    "{FourthExtension}"
    false:
        "Кондрат $ Король, на улицах города бушует новая болезнь, стоит ли лечить население? // Да // Нет // 0 0 5 0 $ 0 0 -20 0 // None"
        true:
            "Маг-целитель Хрисанф $ Я хочу провести опыт по созданию нового лекарства. Вы поможете? // Да // Нет // 0 0 0 0 $ +10 0 -5 0 // None"
            true:
                "Кондрат $ Владыка, Хрисанф в ходе опыта создал зомби-вирус, который распространяется! // Что же... // Как... // 0 0 0 0 $ 0 0 0 0 // None"
                true:
                    "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                false:
                    "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
            false:
                "{FourthExtension}"
        
        false:
            "Кондрат $ Люди бунтуют, болезнь оказалась очень опасной, они недовольны тем, что мы никак не реагируем. // Командир! // Окажите поддержку всем нуждающимся! // 0 +100 -100 0 $ 0 0 0 0 // None"
            true:
                "*Вы одурманены адским зельем на улицах города, среди разгула и восстания. Вы стараетесь не потерять свою голову, но это все равно случается.* // None // None // 0 0 0 0 // None"
            false:
                "Маг-целитель Хрисанф $ Я хочу провести опыт по созданию нового лекарства. Вы поможете? // Да // Нет // 0 0 0 0 $ +10 0 -5 0 // None"
                true:
                    "Кондрат $ Владыка, Хрисанф в ходе опыта создал зомби-вирус, который распространяется! // Что же... // Как... // 0 0 0 0 $ 0 0 0 0 // None"
                    true:
                        "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                    false:
                        "*Вирус распространился слишком быстро. Вы и ваши мозги были съедены.* // None // None //  // None"
                false:
                    "{FourthExtension}"
"""

