##line no, time,level,message,user
import logging
logging.basicConfig(filename='employee.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='%(lineno)s:%(asctime)s:%(levelname)s:%(message)s:%(name)s')


logger = logging.getLogger('prasad')
def validation(fun):
    logger.info('Entered validation function')
    def fun(user_input):
        logger.info('Before Checking in Database')
        data=['prasad',]
        if user_input in data:
            logger.info('username present in database')
            return 'welcome '+user_input
        else:
            logger.warning('username Not present in database')
            return 'wrong user'
    return fun

@validation
def login_user(user_input):
    return user_input
user_input=input("Enter UserName: ")
logger.info('User Input given')
print(login_user(user_input))

'''======================================================'''
logger = logging.getLogger('Sandeep')
def validation(fun):
    logger.info('Entered validation function')
    def fun(user_input):
        logger.info('Before Checking in Database')
        data=['sandeep',]
        if user_input in data:
            logger.info('username present in database')
            return 'welcom '+user_input
        else:
            logger.warning('username Not present in database')
            return 'wrong user'
    return fun

@validation
def login_user(user_input):
    return user_input
user_input=input("Enter UserName: ")
logger.info('User Input given')
print(login_user(user_input))

##lst = ['prasad','sandeep']
##logging.basicConfig(filename='emp.log',
##                    encoding='utf-8',
##                    level=logging.INFO,
##                    format='%(lineno)s::%(asctime)s::%(levelname)s::%(message)s::%(name)s')
##usrinput = input('Enter Username: ')
##logging.info('User input given')
##
##if usrinput in lst:
##    logging.info('User present in DB')
##    print('Welcom ',usrinput)
##else:
##    logging.warning('User Not Present in DB')
##    print('Wrong user')
             
