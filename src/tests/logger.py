class Logger:
    @staticmethod
    def err(message):
        print("[!] " + message)
    
    @staticmethod
    def success(message):
        print(f"[^] {message}")
    
    @staticmethod
    def annotation(message):
        print(f"[*] {message}")
    
    @staticmethod
    def warn(message):
        print(f"[#] {message}")