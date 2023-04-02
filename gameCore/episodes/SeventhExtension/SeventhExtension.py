SeventhExtension = """
    "Господин Авдей $ В соседней деревушке жители начали ходить на четвереньках и гавкать, что нам делать? // Ничего // Отправить армию // +5 0 0 0 $ 0 +5 -5 0 // None"
    true:
        "*Церковь восприняла их еретиками и сама разобралась с ними...* // Продолжить // None // -5 0 0 0 // None"
        "Епископ Галактион $ Владыка, церковь хочет провести глобальные реформы. Вы согласны? // Да // Нет // +10 0 0 0 $ -10 0 0 0 // None"
        true:
            "Епископ Галактион $ Дайте нам власть, чтоб остановить ересь. // Да // Нет // +5 0 0 0 $ -25 0 0 0 // None"
            true:
                "Кондрат $ Сэр, влияние, оказываемое церковью слишком большое. Вы больше не управляете страной. // Что... // Почему... // 0 0 0 0 $ 0 0 0 0 // None"
                true:
                    "*Против вас организовали заговор. Вы были отправлены в темницу.* // Продолжить // None // 0 0 0 0 // None"
                    "Дух прошлого короля $ Теперь, ты тоже здесь. // Здравствуйте! // Опять ты // 0 0 0 0 $ 0 0 0 0 // None"
                    true:
                        "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                        true:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                        false:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                    false:
                        "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                        true:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                        false:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                false:
                    "*Против вас организовали заговор. Вы были отправлены в темницу.* // Продолжить // None // 0 0 0 0 // None"
                    "Дух прошлого короля $ Теперь, ты тоже здесь. // Здравствуйте! // Опять ты // 0 0 0 0 $ 0 0 0 0 // None"
                    true:
                        "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                        true:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                        false:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                    false:
                        "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                        true:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                        false:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
            false:
                "Маг-целитель Хрисанф $ Владыка, могу ли я построить больницу? Это поможет уменьшить заболеваемость различных болезней. // Да // Нет // 0 0 +10 -10 $ 0 0 -10 +10 // None"
                true:
                    "{EighthExtension}"
                false:
                    "{EighthExtension}"
        false:
            "Маг-целитель Хрисанф $ Владыка, могу ли я построить больницу? Это поможет уменьшить заболеваемость различных болезней. // Да // Нет // 0 0 +10 -10 $ 0 0 -10 +10 // None"
            true:
                "{EighthExtension}"
            false:
                "{EighthExtension}"
    false:
        "Епископ Галактион $ Владыка, церковь хочет провести глобальные реформы. Вы согласны? // Да // Нет // +10 0 0 0 $ -10 0 0 0 // None"
        true:
            "Епископ Галактион $ Дайте нам власть, чтоб остановить ересь // Да // Нет // +5 0 0 0 $ -25 0 0 0 // None"
            true:
                "Кондрат $ Сэр, влияние, оказываемое церковью слишком большое. Вы больше не управляете страной. // Что... // Почему... // 0 0 0 0 $ 0 0 0 0 // None"
                true:
                    "*Против вас организовали заговор. Вы были отправлены в темницу* // Продолжить // None // 0 0 0 0 // None"
                    "Дух прошлого короля $ Теперь, ты тоже здесь // Здравствуйте! // Опять ты // 0 0 0 0 $ 0 0 0 0 // None"
                    true:
                        "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                        true:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                        false:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                    false:
                        "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                        true:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                        false:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                false:
                    "*Против вас организовали заговор. Вы были отправлены в темницу* // Продолжить // None // 0 0 0 0 // None"
                    "Дух прошлого короля $ Теперь, ты тоже здесь // Здравствуйте! // Опять ты // 0 0 0 0 $ 0 0 0 0 // None"
                    true:
                        "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                        true:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                        false:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                    false:
                        "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                        true:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
                        false:
                            "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                            "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски // None // None //  // None"
            false:
                "Маг-целитель Хрисанф $ Владыка, могу ли я построить больницу? Это поможет уменьшить заболеваемость различных болезней // Да // Нет // 0 0 +10 -10 $ 0 0 -10 +10 // None"
                true:
                    "{EighthExtension}"
                false
                    "{EighthExtension}"
        false:
            "Маг-целитель Хрисанф $ Владыка, могу ли я построить больницу? Это поможет уменьшить заболеваемость различных болезней // Да // Нет // 0 0 +10 -10 $ 0 0 -10 +10 // None"
            true:
                "{EighthExtension}"
            false:
                "{EighthExtension}"
"""