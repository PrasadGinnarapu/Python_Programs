import pandas as pd
import datetime
import smtplib
import os
current_path=os.getcwd()

gmail_id=input("Enter your email: ")
gmail_pwd=input("Enter password for your email id mentioned above: ")
def sendEmail(to,sub,msg):
    print(f"Email to {to} sent: \nSubject: {sub},  \nMessage: {msg}")
    s=smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(gmail_id,gmail_pwd)
    s.sendmail(gmail_id, to, f"Subject: {sub} \n\n{msg}")
    s.quit()

if __name__=="__main__":
    df=pd.read_excel("autobirthday.xlsx")
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeindex=[]
    for index,item in df.iterrows():
        bday=item["Birthday"]              
        bday=datetime.datetime.strptime(bday,"%d-%m-%Y")
##        print("after parsing",bday)
        bday=bday.strftime("%d-%m")
        if (today==bday) and yearNow not in str(item["LastWishedYear"]):
            sendEmail(item["Mailid"],"Birthday Wishes",item["Dialogue"])
            writeindex.append(index)
    if writeindex != None:
        for i in writeindex:
            oldYear = df.loc[i, 'LastWishedYear']
            df.loc[i, 'LastWishedYear'] = str(oldYear) + ", " + str(yearNow)
    df.to_excel("autobirthday.xlsx", index=False)
          
