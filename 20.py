from  abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logged in using Google")
    def logout(self):
        print("Logged out of Google account")
class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logged in using Facebook account")
    def logout(self):
        print("Logged out of Facebook account")
google = GoogleAuth()
google.login()
google.logout()
facebook = FacebookAuth()
facebook.login()
facebook.logout()