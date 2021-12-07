
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
import json

class GetMessage:
  def __init__(self,From,To,Subject):
    self.msg=MIMEMultipart("alternative")
    self.msg["From"]=From
    self.msg["To"]=To
    self.msg["Subject"]=Subject
  def create_message(self, message):
    for message_text,type in message:
      # self.msg.
      self.msg.attach(MIMEText(message_text,type))
  def returnMessage(self):
    # return(self.msg)
    m={"raw":base64.urlsafe_b64encode(bytes(self.msg.as_string(),"utf-8")).decode()}
    print(type(m))
    with open("message.json","w") as f:
      json.dump(m,f)
    return(m)
    # print(create_message())

if __name__=="__main__":
  From="jrtyagi"
  To="sachin"
  Subject="hello there!"
  message='Hello Sachin'
  l=[[message,"plain"]]
  a=GetMessage(From,To,Subject)
  a.create_message(l)
  print(a.returnMessage())

