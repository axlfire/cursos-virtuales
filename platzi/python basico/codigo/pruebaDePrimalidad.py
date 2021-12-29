#------run()/main---
def run():
    for i in range(1001):
        isPrim(i)

#------functions----
def isPrim(inpt):
    prim=True
    for number in range(1001):
        if(number<=1 or number==inpt):
            if inpt<=1:
                prim=False
            continue
        elif(inpt%number==0):
            print(str(inpt)+" no es primo")
            prim=False
            break
    if prim:
        print(str(inpt)+" es primo")


#------config-------
if __name__ == '__main__':
    run()
