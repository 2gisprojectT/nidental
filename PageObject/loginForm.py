from baseComponent import BaseComponent

class LoginForm(BaseComponent):
    keyWords = {
        'login': 'login_field',
        'password': 'password',
        'buttonOK': 'commit',
        'avatar': 'avatar',
        'myLogin': 'alt',
    }

    def login(self, login, password):
        self.driver.find_element_by_id(self.keyWords['login']).send_keys(login)
        self.driver.find_element_by_id(self.keyWords['password']).send_keys(password)
        self.driver.find_element_by_name(self.keyWords['buttonOK']).click()


    def getUserName(self):
        return self.driver.find_element_by_class_name(self.keyWords['avatar']).get_attribute(self.keyWords['myLogin'])

    def getCurrentUrl(self):
        return self.driver.current_url

