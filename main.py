import random

strings = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"
print("THIS IS VERY SIMPLE IF YOU ACTUALLY NEED A PASSWORD I SUGGEST USING A WEBSITE FOR THIS")
while 1:
  length_of_passwords = int(input("whats the length of the passwords you want generated: "))
  count_of_passwords = int(input("how many passwords do you want generated: "))
  for x in range(0,count_of_passwords):
      password = ""
      for x in range(0,length_of_passwords):
          password_char  = random.choice(strings)
          password       = password + password_char
      print(password)
