import re

##test = "123abc456abc789ABC"
##pattern = re.compile(r"abc")
##res = pattern.finditer(test)      #returns object
##for i in res:
##    print(i)
                    
#------------------------------
##test = "123abc456abc789ABC"
##res = re.finditer(r'abc',test)    #returns object
##for i in res:
##    print(i)
#------------------------------
##test = "123abc456abc789ABC"
##res = re.findall(r'abc',test)     #returns matched string
##for i in res:
##    print(i)           

#-------------------------------
##test = "123abc456abc789ABC"
##res = re.search(r'abc',test)      #returns object of first occurence
##print(res)
#--------------------------------
##test = "123abc456abc789ABC"
##pattern = '123'
##res = re.match(pattern,test)         #returns object of first occurence
##
##print(res.group())                  #group() will gives the matched string
##print(res.span())                   #span() will gives the start and end indexes in tuple of matched string
##print(res.start())                  #start() will gives the start index of span() tuple
##print(res.end())                    #end() will gives the end index of span() tuple 
#--------------------------------


test = "123abc456abc789ABC"
res = re.finditer('\d',test)
for i in res:
    print(i)




















