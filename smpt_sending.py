'''import smtplib
var = 123456
content=f"Your OTP is: {var} "
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
sender='ticketingtool12@gmail.com'
receipient='ginnarapuprasad@gmail.com'
mail.login('ticketingtool12@gmail.com','ticketing@12')
header='To:'+receipient+'\n'+'From:'\
+sender+'\n'+'subject:OTP from Ticketing Tool\n'
content=header
mail.sendmail(sender,receipient, "This is content")
mail.close()'''
##
####import re
####str_test = "todayisthursday"
####res = re.split('[a,e,i,o,u]',str_test)
####print(res)
##
####str_test = "todayisthursday"
##'''vow='aeiou'
##lst=['a','e','i','o','u']'''
####res=str_test.split(lst)
####print(res)
##'''for i in range(len(str_test)):
##    if str_test[i] in vow:
##        res = str_test.split(str_test[i])
##        print(res)'''
####vow = 'aeiou'
####for i in range(len(str_test)):
####    if i in 
####    res = str_test.split('a'|'e'|'i'|'o'|'u')
####    print(res)
##
##import re
##test = "Hello,how:are!you?"
##res = re.split('\W', test)
##print(res)
##
##
##
##
##
##
##
##
##
##
"""
input_string = "STAR"
output_string=""
c=0
if len(input_string)<4:
    output_string=input_string+input_string[0]
elif input_string[0].isupper():
    
    output_string=input_string[1:]
elif input_string.isalnum()==False:
    for i in input_string:
        if i.isalnum()==False:
            sp = i
            c+=1
            if c>1 and c<=5:
                output_string=input_string+i
else:
    output_string = input_string.casefold()
print(output_string)"""

var = 123465
content=f"Your OTP is: {var}"
header = "header"
content=header+content
print(content)






