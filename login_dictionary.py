# program login system using dictionary
#Internship practice - Python basics
users={
  "vinushree":1034,
  "anushree":1357,
  "manushree":1254,
  "sonushree":8088
}
username=input("Enter Username:").strip()
try:
   password=int(input("Enter password:"))
   if username in users:
    if users[username]==password:
        print("Login successful")
    else:
        print("wrong password")
   else:
    print("wrong user name")
except:
  print("password must be a number")
