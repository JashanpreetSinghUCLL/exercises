class Account:
    def __init__(self, login, password):
        self.login = login
        self.__password = password
    
    def is_correct_password(self, pw):
        return len(self.__password) == len(pw)
    
account = Account("Jashan", "J123")
print(account.is_correct_password("J123"))
