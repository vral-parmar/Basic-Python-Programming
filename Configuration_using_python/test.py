#import class
from configparser import ConfigParser
# create an instance of ConfigParser class.
parser = ConfigParser()
# read and parse the configuration file.
parser.read('Configuration_using_python/conf.ini')
['Configuration_using_python/conf.ini']
# get option value in specified section.
mysql_conn_host = parser.get('mysql_conn', 'host')
#print option values
print(mysql_conn_host)
#get user account Info
account = parser.get('account', 'user_name') 
print(account) 
