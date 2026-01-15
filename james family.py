Jamesfamily=["vishu","shelin","riya","neha"]
Rajputfamily=["rekha","pihu","yash","meesho"]
Senfamily=["minu","kaku","siya","mahi"]


Jamesfamily.append("rekha")
print(Jamesfamily)

Rajputfamily.append("SenFamily")
print(Rajputfamily)



name=input("enter your name : Rajputfamily")

if name in Jamesfamily:
    print("you are a member of Jamefamily")
elif name is Senfamily:
    print ("you are member of Senfamily")

else:
    print("your family is not in the list")