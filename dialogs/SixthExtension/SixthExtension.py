from dialogs.SeventhExtension.SeventhExtension import *


SixthExtension = f'''
    "Шахтёры отказываются спускаться в шахту, они требуют повышения зарплаты // Да // Нет // None"
    true:
        "Владыка, незнакомка просится к вам, говорит, что она предскажет ваше будущее // Да // Нет // None"
        true:
            "Здравствуйте, я Ионна Разумовская - гадалка, хотите узнать свою судьбу? // Продолжай // Нет // None"
            true:
                "Я вижу что-то очень тёмное, словно демона, поджидающего вас // Продолжай // Хватит! // None"
                true:
                    "*После слов: "О нет..мне очень жаль" - гадалка убегает* // Продолжить // None // None"
                    true:
                        "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                        true:
                            {SeventhExtension}
                false:
                    "*Гадалка удаляется, бормоча что-то о большой опасности* // Продолжить // None // None"
                    true:
                        "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                        true:
                            {SeventhExtension}
            false:
                "*Гадалка удаляется, бормоча что-то о большой опасности* // Продолжить // None // None"
                true:
                    "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                    true:
                        {SeventhExtension}
        false:
            "Сэр, мы никак не смогли её сдержать // Продолжить // None // None"
            true:
                "Здравствуйте, я Ионна Разумовская - гадалка, хотите узнать свою судьбу? // Продолжай // Нет // None"
                true:
                    "Я вижу что-то очень тёмное, словно демона, поджидающего вас // Продолжай // Хватит! // None"
                    true:
                        "*После слов: "О нет..мне очень жаль" - гадалка убегает* // Продолжить // None // None"
                        true:
                            "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                            true:
                                {SeventhExtension}
                    false:
                        "*Гадалка удаляется, бормоча что-то о большой опасности* // Продолжить // None // None"
                        true:
                            "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                            true:
                                {SeventhExtension}
                false:
                    "*Гадалка удаляется, бормоча что-то о большой опасности* // Продолжить // None // None"
                    true:
                       "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                       true:
                          {SeventhExtension} 
    
    
    
    
    
    
    
    
    
    
    
    
    false:
        "Владыка, незнакомка просится к вам, говорит, что она предскажет ваше будущее // Да // Нет // None"
        true:
            "Здравствуйте, я Ионна Разумовская - гадалка, хотите узнать свою судьбу? // Продолжай // Нет // None"
            true:
                "Я вижу что-то очень тёмное, словно демона, поджидающего вас // Продолжай // Хватит! // None"
                true:
                    "*После слов: "О нет..мне очень жаль" - гадалка убегает* // Продолжить // None // None"
                    true:
                        "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                        true:
                            {SeventhExtension}
                false:
                    "*Гадалка удаляется, бормоча что-то о большой опасности* // Продолжить // None // None"
                    true:
                        "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                        true:
                            {SeventhExtension}
            false:
                "*Гадалка удаляется, бормоча что-то о большой опасности* // Продолжить // None // None"
                true:
                    "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                    true:
                        {SeventhExtension}
               
        false:
            "Сэр, мы никак не смогли её сдержать // Продолжить // None // None"
            true:
                "Здравствуйте, я Ионна Разумовская - гадалка, хотите узнать свою судьбу? // Продолжай // Нет // None"
                true:
                    "Я вижу что-то очень тёмное, словно демона, поджидающего вас // Продолжай // Хватит! // None"
                    true:
                        "*После слов: "О нет..мне очень жаль" - гадалка убегает* // Продолжить // None // None"
                        true:
                            "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                            true:
                                {SeventhExtension}
                    false:
                        "*Гадалка удаляется, бормоча что-то о большой опасности* // Продолжить // None // None"
                        true:
                            {SeventhExtension}
                false:
                    "*Гадалка удаляется, бормоча что-то о большой опасности* // Продолжить // None // None"
                    true:
                        "*Вы очень взволнованы, но пути назад уже нет* // Продолжить // None // None"
                        true:
                            {SeventhExtension}






'''