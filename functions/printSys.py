from keyflow import kfprint, kfinput
isLoading = False
def printFuc(text, speed):
    if isLoading:
        kfinput(text, speed)
        return 
    else:
        print(text)
        return