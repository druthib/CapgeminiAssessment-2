class Notification:
    def __init__(self,msg):
        self.msg=msg
    def send(self):
        print(f"{self.msg} is notified")
class EmailNotif(Notification):
    def __init__(self, msg):
        super().__init__(msg)
    def send(self):
        print(f"{self.msg} is notified from mail")
class SMSNotif(Notification):
     def __init__(self, msg):
        super().__init__(msg)
     def send(self):
        print(f"{self.msg} is notified from sms")
def myfunc(obj):
    obj.send()
n=Notification("hello")
e=EmailNotif("yo")
sms=SMSNotif("hellooo")
myfunc(n)
myfunc(e)
myfunc(sms)
    
    