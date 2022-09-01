import string
import random
if __name__ == '__main__':
    s1= string.ascii_lowercase
    # print(s1)
    s2= string.ascii_uppercase
    # print(s2)
    s3= string.digits
    s4= string.punctuation
 #   print(s3,s4)
    plen= int(input("enter the length of password\n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print(s)
    random.shuffle(s)
    print(s)
    print("your password is")
    print("".join(s[:plen]))
