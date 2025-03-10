#name length check madoo candition

name = input("enter a name:")

if len(name) <3:
    print("Name is very short")

elif len(name) >60:
    print("Name is very long")

else:
    print("Name is just right")
