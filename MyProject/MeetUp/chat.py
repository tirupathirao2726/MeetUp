class Msg:
    def __init__(self,msg,user):
        self.__msg=msg
        self.__user=user
        self.__next=None
    def get_msg(self):
        return self.__msg
    def get_user(self):
        return self.__user
    
