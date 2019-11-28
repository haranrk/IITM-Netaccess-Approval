#!/usr/bin/python
# script for automatic Netaccess approval for IIT Madras network

import getpass
import mechanize
import argparse 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username","-u",default="Username",help="LDAP username")
    parser.add_argument("--password","-p",default="Password",help="LDAP password")
    args = parser.parse_args()

    username=args.username
    password=args.password

    try:
        br=mechanize.Browser()

        try:
            response=br.open("https://netaccess.iitm.ac.in/account/login") 
            print('1/3 Page')
        except:
            print("ERROR: Webpage unavailable - check LAN connection and server status")
            exit(1)
        try:
            br.select_form(nr=0)
        except:
            print("ERROR: Webpage unavailable - check LAN connection and server status")
            exit(1)

        if (username=="Username"):
            print("Username has not been set in code. Enter LDAP Username")
            username=input('Username: ')
        if (password=="Password"):
            print("Password has not been set in code. Enter LDAP Password")
            password=getpass.getpass()
        print(password)

        br.form["userLogin"]=username
        br.form["userPassword"]=password
        url1=br.geturl()
        result=br.submit()
        url2=br.geturl()
        if (url1==url2):
            print("ERROR: Wrong username or password")
            exit(1)

        # Second page
        print('2/3 Page')
        br.visit_response(result)

        # Third page
        print('3/3 Page')
        br.follow_link(br.find_link(url_regex="approve"))
        br.select_form(nr=0)
        br.form["duration"] = ["2"]
        result=br.submit()

        print("APPROVAL SUCCESFUL")
    except:
        print("APPROVAL UNSUCCESSFULL")

if __name__ == "__main__":
    main()
