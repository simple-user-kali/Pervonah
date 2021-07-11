class Settings:
    def __init__(self):
        self.LOGIN = 'login user'
        self.PASSWORD = 'password user'
        self.DELAY = 3
        self.PROXY = False
        self.LIST_MESSAGE = ['message']
        self.PHOTOS = []
        self.PROXY_LIST = ({'http': 'IP:PORT'})


    def get_banner(self):
        BANNER = '''
        
            ██████╗░███████╗██████╗░██╗░░░██╗░█████╗░███╗░░██╗░█████╗░██╗░░██╗
            ██╔══██╗██╔════╝██╔══██╗██║░░░██║██╔══██╗████╗░██║██╔══██╗██║░░██║
            ██████╔╝█████╗░░██████╔╝╚██╗░██╔╝██║░░██║██╔██╗██║███████║███████║
            ██╔═══╝░██╔══╝░░██╔══██╗░╚████╔╝░██║░░██║██║╚████║██╔══██║██╔══██║
            ██║░░░░░███████╗██║░░██║░░╚██╔╝░░╚█████╔╝██║░╚███║██║░░██║██║░░██║
            ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝
        '''
        return BANNER


