x = "w3.school"
y = '123456789' 
u = '987654321' 

body = {"URL:"+ x,
      "AcessToken:"+ y,
      "ClientID:" + u,
}
print("body \n")
for i in body:
    print (i)