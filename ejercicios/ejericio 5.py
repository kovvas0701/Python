
num = int(input( ))

fact = 1 


while num > 1:
    
    if num < 0:
        print("ERROR")
        num = int(input( ))
    
    else:
        fact *= num
        num -= 1
        print(fact)
    
