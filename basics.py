# import datetime

# mynow = datetime.datetime.now()
# print("The date and time is", mynow)

# x = 10
# y = "10"

# sum1 = x + x
# sum2 = y + y

u_input = ""
response = ""

while u_input != "/end":
  response = response + u_input
  u_input = input("Say something: ")
  
print(response)
