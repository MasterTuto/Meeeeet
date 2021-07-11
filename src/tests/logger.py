class Logger:
    @staticmethod
    def err(message):
        print( Logger.get_err(message) )
    
    @staticmethod
    def success(message):
        print(f"[^] {message}")
    
    @staticmethod
    def annotation(message):
        print(f"[*] {message}")
    
    @staticmethod
    def warn(message):
        print(f"[#] {message}")
    
    @staticmethod
    def get_err(message):
        return  "[!] " + message