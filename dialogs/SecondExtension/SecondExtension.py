

SecondExtension = """
    "Улицы нашей прекрасной столицы воняют сточными водами, нужно построить канализацию // Да // Нет // None"    
    true:
        "Мой друг-врач спас меня от смертельной болезни, он хочет поговорить с вами, но тот немного маг // Впустить его.. // Я занят // None"
        true:
            "Здравствуйте, я маг-целитель Хрисанф, я хочу вам помочь защиться от смерти, либо улучшить вам жизнь своими навыками // Да // Нет // None"
            true:
                "Вы сможете обратиться ко мне за любой помощью! *даёт вам странную нить и уходит* // Продолжить // None // None"
                "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"
                true:
                    "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None // None"
                    "Прошу, спаси меня! // Да // Нет // None"
                    true:
                        "Ты хочешь забрать её? // Напасть! // Да // None"
                        true:
                            "*Вы ожесточёно сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                            true:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                            false:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                        false:
                            "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None // None"
                            "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None // None"
                            "Хотите ли вы стать моим принцем? // Да // Нет // None"
                                true:
                                    "{ThirdExtension}"
                                false:
                                    "{ThirdExtension}"
                    false:
                        "Вы разворачиваетесь и убегаете.. // Продолжить // None // None"
                        "{ThirdExtension}"
                    false:
                        "{ThirdExtension}"       
            false:
                "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"
                true:
                    "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None // None"
                    "Прошу, спаси меня! // Да // Нет // None"
                        true:
                        "Ты хочешь забрать её? // Напасть! // Да // None"
                        true:
                            "*Вы ожесточёно сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                            true:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                            false:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                        false:
                            "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None // None"
                            "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None // None"
                            "Хотите ли вы стать моим принцем? // Да // Нет // None"
                            true:
                                "{ThirdExtension}"
                            false:
                                "{ThirdExtension}"
                    false:
                        "Вы разворачиваетесь и убегаете.. // Продолжить // None // None"
                        "{ThirdExtension}"
                false:
                    "{ThirdExtension}"       
        false:
            "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"
            true:
                "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None // None"
                "Прошу, спаси меня! // Да // Нет // None"
                true:
                    "Ты хочешь забрать её? // Напасть! // Да // None"
                    true:
                        "*Вы ожесточёно сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                        true:
                            "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                        false:
                            "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                    false:
                        "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None // None"
                        "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None // None"
                        "Хотите ли вы стать моим принцем? // Да // Нет // None"
                        true:
                            "{ThirdExtension}"
                        false:
                            "{ThirdExtension}"
                false:
                    "Вы разворачиваетесь и убегаете.. // Продолжить // None // None"
                    "{ThirdExtension}"
            false:
                "{ThirdExtension}"
    
    
    
    
    
    
    
    
    false:
        "Мой друг-врач спас меня от смертельной болезни, он хочет поговорить с вами, но тот немного маг // Впустить его.. // Я занят // None"
        true:
            "Здравствуйте, я маг-целитель Хрисанф, я хочу вам помочь защиться от смерти, либо улучшить вам жизнь своими навыками // Да // Нет // None"   
            true:
                "Вы сможете обратиться ко мне за любой помощью! *даёт вам странную нить и уходит* // Продолжить // None // None"
                "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"
                true:
                    "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None // None"
                    "Прошу, спаси меня! // Да // Нет // None"
                    true:
                        "Ты хочешь забрать её? // Напасть! // Да // None"
                        true:
                            "*Вы ожесточёно сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                            true:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                            false:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                        false:
                            "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None // None"
                            "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None // None"
                            "Хотите ли вы стать моим принцем? // Да // Нет // None"
                                true:
                                    "{ThirdExtension}"
                                false:
                                    "{ThirdExtension}"
                false:
                    "Вы разворачиваетесь и убегаете.. // Продолжить // None // None"
                    "{ThirdExtension}"        
            false:
                "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"   
                true:
                    "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None // None"
                    "Прошу, спаси меня! // Да // Нет // None"
                    true:
                        "Ты хочешь забрать её? // Напасть! // Да // None"
                        true:
                            "*Вы ожесточёно сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                            true:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                            false:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                        false:
                            "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None // None"
                            "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None // None"
                            "Хотите ли вы стать моим принцем? // Да // Нет // None"
                                true:
                                    "{ThirdExtension}"
                                false:
                                    "{ThirdExtension}"
                false:
                    "Вы разворачиваетесь и убегаете.. // Продолжить // None // None"
                    "{ThirdExtension}"     
        false:
            "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"
            true:
                "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None // None"
                "Прошу, спаси меня! // Да // Нет // None"
                true:
                    "Ты хочешь забрать её? // Напасть! // Да // None"
                    true:
                        "*Вы ожесточёно сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                        true:
                            "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                        false:
                            "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                    false:
                        "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None // None"
                        "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None // None"
                        "Хотите ли вы стать моим принцем? // Да // Нет // None"
                            true:
                                "{ThirdExtension}"
                            false:
                                "{ThirdExtension}"
                false:
                    "Вы разворачиваетесь и убегаете.. // Продолжить // None // None"
                    "{ThirdExtension}"
            false:
                "{ThirdExtension}"








"""