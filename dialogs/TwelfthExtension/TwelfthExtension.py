TwelfthExtension = """
    "Владыка, жители города говорят, что видели оборотня, стоит усилить патрулирование? // Да // Нет //  // None"
    true:
        "Господин, мы нуждаемся в финансовых реформах, люди отказываются работаться, а экономика рушится // Да // Нет //  // None"
        true:
            "Нам стоит развивать международные отношение? Это поможет избежать войн // Да // Нет //  // None"
            true:
                "{ThirteenthExtension}"
            false:
                "{ThirteenthExtension}"
        false:
            "Народ протестует и угрожает штурмом, пойти на их условия? // Да // Нет //  // None"
            true:
                "Нам стоит развивать международные отношение? Это поможет избежать войн // Да // Нет //  // None"
                true:
                    "{ThirteenthExtension}"
                false:
                    "{ThirteenthExtension}"
            false:
                "Повелитель, наша защита больше не может сдерживать протесты жителей // Что... // Что... //  // None"
                true:
                    "*Вы были пойманы и отправлены на публичную виселицу. Стоит лучше думать о своём народе* // None // None //  // None"
                false:
                    "*Вы были пойманы и отправлены на публичную виселицу. Стоит лучше думать о своём народе* // None // None //  // None"
    
    
    
    false:
        "Господин, мы нуждаемся в финансовых реформах, люди отказываются работаться, а экономика рушится // Да // Нет //  // None"
        true:
            "Нам стоит развивать международные отношение? Это поможет избежать войн // Да // Нет //  // None"
            true:
                "{ThirteenthExtension}"
            false:
                "{ThirteenthExtension}"
        false:
            "Народ протестует и угрожает штурмом, пойти на их условия? // Да // Нет //  // None"
            true:
                "Нам стоит развивать международные отношение? Это поможет избежать войн // Да // Нет //  // None"
                true:
                    "{ThirteenthExtension}"
                false:
                    "{ThirteenthExtension}"
            
            
            
            false:
                "Повелитель, наша защита больше не может сдерживать протесты жителей // Что... // Что... //  // None"
                true:
                    "*Вы были пойманы и отправлены на публичную виселицу. Стоит лучше думать о своём народе* // None // None //  // None"
                false:
                    "*Вы были пойманы и отправлены на публичную виселицу. Стоит лучше думать о своём народе* // None // None //  // None"
"""