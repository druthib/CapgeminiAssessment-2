class Logger:
    def log(self,error=None, warning=None,info=None):
        self.error=error
        self.warning=warning
        self.info=info
        if error and warning and info:
            print(f"error msg:{error} warning msg:{warning} info msg:{info}")
        elif error and warning:
            print(f"error msg:{error} warning msg:{warning}")
        elif error and info:
            print(f"error msg:{error} warning msg:{info}")
        elif error:
            print(f"error msg:{error}")
        elif warning and info:
            print(f"warning msg:{warning} info msg:{info}")
        elif warning:
            print(f"warning msg:{warning}")
        else:
            print(f"info msg{info}")
obj=Logger()    
obj.log()     
obj.log(error="connection lost")  
            
            
            
            