FifthExtension = """
    "Господин Авдей $ Господин, мы хотим построить новые школы // Да // Нет //  // None"
    true:
        "Крестьянин Александр $ Мы нашли сокровище! Что будем делать? // Разделить между всеми // Всё в казну! //  // None"
        true:
            "Командир Родион $ Шут Радмир разбил вашу статую в главном зале. Что прикажете с ним делать? // Казнить! // Приведите его ко мне //  // None"
            true:
                "Господин Авдей $ Мы хотим построить рынок, который откроет для нас новые возможности на международной арене. // Да // Нет //  // None"
                true:
                    "{SixthExtension}"
                false:
                    "{SixthExtension}"
            false:
                "Шут Радмир $ Я сделал это не специально! Казни - это скучно, нам нужны салюты и веселые анекдоты! // Казнить // Помиловать //  // None"
                true:
                    "{SixthExtension}"
                false:
                    "{SixthExtension}"
        false:
            "Командир Родион $ Шут Радмир разбил вашу статую в главном зале. Что прикажете с ним делать? // Казнить! // Приведите его ко мне //  // None"
            true:
                "Господин Авдей $ Мы хотим построить рынок, который откроет для нас новые возможности на международной арене. // Да // Нет //  // None"
                true:
                    "{SixthExtension}"
                false:
                    "{SixthExtension}"
            false:
                "Шут Радмир $ Я сделал это не специально! Казни - это скучно, нам нужны салюты и веселые анекдоты! // Казнить // Помиловать //  // None"
                true:
                    "{SixthExtension}"
                false:
                    "{SixthExtension}"
    false:
        "Крестьянин Александр $ Мы нашли сокровище! Что будем делать? // Разделить между всеми // Всё в казну! //  // None"
        true:
            "Командир Родион $ Шут Радмир разбил вашу статую в главном зале. Что прикажете с ним делать? // Казнить! // Приведите его ко мне //  // None"
            true:
                "Господин Авдей $ Мы хотим построить рынок, который откроет для нас новые возможности на международной арене. // Да // Нет //  // None"
                true:
                    "{SixthExtension}"
                false:
                    "{SixthExtension}"
            false:
                "Шут Радмир $ Я сделал это не специально! Казни - это скучно, нам нужны салюты и веселые анекдоты! // Казнить // Помиловать //  // None"
                true:
                    "{SixthExtension}"
                false:
                    "{SixthExtension}"
        false:
            "Командир Родион $ Шут Радмир разбил вашу статую в главном зале. Что прикажете с ним делать? // Казнить! //  // Приведите его ко мне //  // None"
            true:
                "Господин Авдей $ Мы хотим построить рынок, который откроет для нас новые возможности на международной арене. // Да // Нет //  // None"
                true:
                    "{SixthExtension}"
                false:
                    "{SixthExtension}"
            false:
                "Шут Радмир $ Я сделал это не специально! Казни - это скучно, нам нужны салюты и веселые анекдоты! // Казнить // Помиловать //  // None"
                true:
                    "{SixthExtension}"
                false:
                    "{SixthExtension}"
"""