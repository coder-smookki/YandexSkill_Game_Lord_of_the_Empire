from dialogs.SecondExtension.SecondExtension import *

FirstExtension = f'''
    "Мы можем повысить арендную плату в домах, которые мы построили для малоимущих // Да // Нет // None"
    
    true:
        "Как вы могли так поступить с нами? // Смирись и терпи! // Моя вина // None"
        true:
            "Владыка! Армия соседней страны группируется у Западной  границы нашего государства, отправить армию? // Да // Нет // None"
            true:
                "У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // None"
                true:
                    "*Армия перегрупировалась и сокрушила наступление* // Продолжить // None // None"
                    true:
                        {SecondExtension}
                false:
                    "65% 35% // Продолжить // None // None"
                    true:
                        {SecondExtension}
            false:
                 "У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // None"
                true:
                    "*Армия перегрупировалась и сокрушила наступление* // Продолжить // None // None"
                    true:
                        {SecondExtension}
                false:
                    "65% 35% // Продолжить // None // None"
                    true:
                        {SecondExtension}
        false:
            "Владыка! Армия соседней страны группируется у Западной  границы нашего государства, отправить армию? // Да // Нет // None"
            true:
                "У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // None"
                true:
                    "*Армия перегрупировалась и сокрушила наступление* // Продолжить // None // None"
                    true:
                        {SecondExtension}
                false:
                    "65% 35% // Продолжить // None // None"
                    true:
                        {SecondExtension}
            false:
                "Армия врага развернулась, ложная тревога, нам больше ничего не угрожает! // Да // Нет // None"
                true:
                    {SecondExtension}
                false:
                    {SecondExtension}

    
    
    
    
    
    
    
    false:
        "Владыка! Армия соседней страны группируется у Западной  границы нашего государства, отправить армию? // Да // Нет // None"
        true:
            "У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // None"
            true:
                "*Армия перегрупировалась и сокрушила наступление* // Продолжить // None // None"
                true:
                    {SecondExtension}
            false:
                "65% 35% // Продолжить // None // None"
                true:
                    {SecondExtension}
        false:
            "Армия врага развернулась, ложная тревога, нам больше ничего не угрожает! // Да // Нет // None"
            true:
                {SecondExtension}
            false:
                {SecondExtension}





'''