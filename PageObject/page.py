from loginForm import LoginForm

class Page():
    def __init__(self, driver):
        self.driver_ = driver
        self.login_form_ = None
        # self.login_form.login(login,password)

    @property
    def login_form(self):
        if self.login_form_ is None:
            self.login_form_ = LoginForm(self.driver_)
        return self.login_form_

    def open(self, url):
        self.driver_.get(url)






    # def setLogin(self, login):
    #     self.login_ = login
    #     return self
    #
    # def setPassword(self, password):
    #     self.password_ = password
    #     return self

    # def input(self):
    #     if self.login_ is None or self.password_ is None:
    #         print("Ошибка! Сначала введите корректные логин и пароль!")
    #     if self.login_form is None:
    #         self.login_form = LoginForm(self.driver)
    #     self.login_form.login(self.login_, self.password_)
    #     return self

    def getUserName(self):
        if self.login_form_ is None:
            print("Ошибка! Сначала войдите на сайт!")
        else:
            return self.login_form_.getUserName()


    def getCurrentUrl(self):
        return self.login_form_.getCurrentUrl()
