import os
import email
import base64


class ExtractEmails:
    def __init__(self,data):
        self.raw_email=data["raw"]
        self.ID=data["id"]
        self.msg=email.message_from_bytes(self.Decode(self.raw_email))
        self.Dire=os.path.join(os.getcwd(),"emailtest",self.ID)
    def Main(self):
        partno=1
        for part in self.msg.walk():
            # print(part.get_content_maintype())
            if part.get_content_maintype()=="multipart":
                continue
            else :
                # print(part)
                self._handle_data(part,f"part {partno}")
                partno+=1
    def _handle_data(self,part,partno):
        if part.get_content_maintype()=='text':
            if part.get_content_subtype()=='plain':
                text=part.get_payload(decode=True)
                Path=os.path.join(self.Dire,partno+".txt")
                print("-----------------------------------------------------------")
    #             print(dire)
    #             print(text)
                print("-----------------------------------------------------------")
                self.save_file(text,Path)
            elif part.get_content_subtype()=='html':
                text=part.get_payload(decode=True)
                Path=os.path.join(self.Dire,partno+".html")
    #             text = bytes(text,'utf-8').decode()
                print("-----------------------------------------------------------")
    #             print(Path)
    #             print(text)
                print("-----------------------------------------------------------")
                self.save_file(text,Path)
        else:
            data=part.get_payload(decode=True)
            filename=part.get_filename()
            Path=os.path.join(self.Dire,"Attachments",filename)
            try:
                os.makedirs(Path)
            except:
                pass
            self.save_file(data,Path)
        