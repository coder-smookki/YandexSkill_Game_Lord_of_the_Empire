FirstExtension = """
    "Господин Авдей $ Мы можем повысить арендную плату в домах, которые мы построили для малоимущих // Да // Нет // 0 0 -20 +15 $ 0 0 +15 -20 // None"
    true:
        "Крестьянин Иакинф $ Как вы могли так поступить с нами? // Смирись и терпи! // Моя вина // 0 +5 -10 0 $ 0 0 0 0 // None"
        true:
            "Разведчик Кирилл $ Владыка! Армия соседней страны группируется у Западной границы нашего государства, отправить армию? // Да // Нет // 0 -15 0 0 $ 0 +15 0 0 // None"
            true:
                "Командир Родион $ У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // 0 +20 0 0 $ +20 -10 0 0 // None"
                true:
                    "*Армия перегруппировалась и сокрушила наступление* // Продолжить // None //  // None"
                    "{SecondExtension}"
                false:
                    "[chance] 65 35"
                    chance:
                        "Командир Родион $ Нам удалось отбиться, враг отступает! // Продолжить // None // 0 +20 0 0 // None"
                        true:
                            "{SecondExtension}"
                    
                        "Командир Родион $ Владыка, нам не удалось остановить врага, они приближаются к нам! // Что... // Что... // 0 -30 0 0 // None"
                        true:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None //  // None"
                        false:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None //  // None"
            false:
                "Командир Родион $ У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // 0 +20 0 0 $ +20 -10 0 0 // None"
                true:
                    "*Армия перегруппировалась и сокрушила наступление* // Продолжить // None //  // None"
                    "{SecondExtension}"
                false:
                    "[chance] 65 35"
                    chance:
                        "Командир Родион $ Нам удалось отбиться, враг отступает! // Продолжить // None // 0 +20 0 0 // None"
                        true:
                            "{SecondExtension}"
                    
                    "Командир Родион $ Владыка, нам не удалось остановить врага, они приближаются к нам! // Что... // Что... // 0 -25 0 0 // None"
                    true:
                        "*Армия врага вошла в столицу, вы были казнены!* // None // None //  // None"
                    false:
                        "*Армия врага вошла в столицу, вы были казнены!* // None // None //  // None"
        false:
            "Разведчик Кирилл $ Владыка! Армия соседней страны группируется у Западной границы нашего государства, отправить армию? // Да // Нет // 0 -15 0 0 $ 0 +15 0 0 // None"
            true:
                "Командир Родион $ У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // 0 +20 0 0 $ +20 -10 0 0 // None"
                true:
                    "*Армия перегруппировалась и сокрушила наступление* // Продолжить // None //  // None"
                    "{SecondExtension}"
                false:
                    "[chance] 65 35"
                    chance:
                        "Командир Родион $ Нам удалось отбиться, враг отступает! // Продолжить // None // 0 +20 0 0 // None"
                        true:
                            "{SecondExtension}"
                    
                    "Командир Родион $ Владыка, нам не удалось остановить врага, они приближаются к нам! // Что... // Что... // 0 -25 0 0 // None"
                    true:
                        "*Армия врага вошла в столицу, вы были казнены!* // None // None //  // None"
                    false:
                        "*Армия врага вошла в столицу, вы были казнены!* // None // None //  // None"
            false:
                "Разведчик Кирилл $ Армия врага развернулась, ложная тревога, нам больше ничего не угрожает! // Да // Нет // 0 0 0 0 $ 0 -20 0 0 // None"
                true:
                    "{SecondExtension}"
                false:
                    "{SecondExtension}"
    false:
        "Разведчик Кирилл $ Владыка! Армия соседней страны группируется у Западной границы нашего государства, отправить армию? // Да // Нет // 0 -15 0 0 $ 0 +15 0 0 // None"
        true:
            "Командир Родион $ У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // 0 +20 0 0 $ +20 -10 0 0 // None"
            true:
                "*Армия перегруппировалась и сокрушила наступление* // Продолжить // None //  // None"
                "{SecondExtension}"
            false:
                "[chance] 65 35"
                chance:
                    "Командир Родион $ Нам удалось отбиться, враг отступает! // Продолжить // None // 0 +25 0 0 // None"
                    true:
                        "{SecondExtension}"
                    
                    "Командир Родион $ Владыка, нам не удалось остановить врага, они приближаются к нам! // Что... // Что... // 0 -25 0 0 // None"
                    true:
                        "*Армия врага вошла в столицу, вы были казнены!* // None // None //  // None"
                    false:
                        "*Армия врага вошла в столицу, вы были казнены!* // None // None //  // None"
        false:
            "Разведчик Кирилл $ Армия врага развернулась, ложная тревога, нам больше ничего не угрожает! // Да // Нет // 0 0 0 0 $ 0 -20 0 0 // None"
            true:
                "{SecondExtension}"
            false:
                "{SecondExtension}"
"""
