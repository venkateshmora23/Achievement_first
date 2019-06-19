#!/usr/bin/python
from ConfigParser import SafeConfigParser
import codecs,urllib2,json,sys
try:
    import requests, validators
except ImportError as error:
        print(error.__class__.__name__ + ": " + error.message + " Please Install " + error.message.split()[3])
        sys.exit()
def api_call(api_url,guser):
    try:
        response = requests.get(url = api_url+guser+'/repos').json()
        if len(response) == 0:
            print 'No Public Repositories for the user', guser
        else:
            for i in range(len(response)):
                print response[i]['full_name'].split(guser,1)[1][1:]
    except :
        print('Exception occurred retreving data')
def validate_user(api_url,guser):
    try:
        return urllib2.urlopen(api_url+guser).code
    except urllib2.HTTPError as err:
        return err.code
def validate_url(api_url):
    return validators.url(api_url)

def main():
    parser = SafeConfigParser()
    with codecs.open('credentials.ini', 'r') as cred_file:
        parser.readfp(cred_file)
    api_url = parser.get('Achievement_First', 'api_url')
    guser = parser.get('Achievement_First', 'guser')
    #Handle Seperately URL and Username
    url_val =validate_url(api_url)
    user_val=validate_user(api_url,guser)
    if url_val != True:
        print('API URL is not valid')
        sys.exit()
    elif user_val != 200:
         print('Unable to validate the user because of',validate_user(api_url,guser))
         sys.exit()
    elif (validate_url(api_url)) and (validate_user(api_url,guser) == 200):
        api_call(api_url,guser)
    else:
        print 'Please verify GitHub User and API'
        sys.exit()

if __name__ == '__main__':
    main()
