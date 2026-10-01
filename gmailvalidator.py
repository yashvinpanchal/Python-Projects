email = input("Enter Your Email :- ")
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-3] == ".") ^ (email[-4] == "."):
                for i in email:
                    if i == " ":
                        print("Email should not contain any spaces")
                    elif i.isalpha():
                        continue
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                            
                    else:
                        print("Email is valid")
            else:
                print("Email should contain a '.' at the appropriate position")            
        else:
            print("Email should contain '@' and it should not be more than one")                   
    else:
        print("Email should start with an alphabet")            
else:
    print("Email must be greater than 6 characters")
    