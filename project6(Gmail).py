gmail = input("Enter your gmail:")
k = 0
j = 0
d = 0
if len(gmail)>=6:
    if gmail[0].isalpha():
        if("@" in gmail) and (gmail.count("@") == 1):
            if(gmail[-4] == ".") ^ (gmail[-3] == "."):
                for i in gmail:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue 
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                    
                if k == 1 or j == 1 or d == 1:
                    print("Wrong gmail 5") 
                else:
                    print("Write gmail :") 
            else:
                print("Wrong gmail 4") 
        else:
            print("Wrong gmail 3")
    else:
        print("Wrong gmail 2:")

else:
    print("Wrong gmail 1:") 




# This program work for check you gmail is valid or not if your gmail valid and all condition check so it give Write gmail otherwise Wrong gmail