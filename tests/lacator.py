class Xpath:
    NAME_INPUT = '//label[contains(text(), "Имя")]/following-sibling::input'
    EMAIL_INPUT = '//label[contains(text(), "Email")]/following-sibling::input'
    PASSWORD_INPUT = '//*[@type="password"]'
    REGISTER_LINK = '//*[@id="root"]/div/main/div/div/p[1]/a'
    ERROR_MESSAGE = '//*[contains(text(), "Некорректный пароль")]'
    LOG_IN = '//button[text()="Войти в аккаунт"]'
    REGISTER_BUTTON = '//button[text()="Зарегистрироваться"]'
    personal_account = '//p[contains(text(), "Личный Кабинет")]'
