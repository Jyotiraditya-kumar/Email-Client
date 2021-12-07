# from GoogleLogin import GoogleLogin
from DATABASE import EmailDatabase

class GmailMessages():
    def __init__(self,glogin):
        self.glogin=glogin
        self.UserId="Emails"#self.glogin.get_profile().split("@")[0]
        # self.messageList=self.glogin.getMessageList()
        self.getNewMessages()
    
    def getNewMessages(self):
        a=EmailDatabase(self.UserId)
        query={}
        fields={"_id":1}
        x=a.fetch(query,fields)
        lst=[]
        print(list(x))        
        
if __name__ == '__main__':
    a=GmailMessages(None)
    
        
        
        
        
        