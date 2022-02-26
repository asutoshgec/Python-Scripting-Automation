#We can import the functions from script1 in script2.
#But we need to comment out the x and y value in script1, because python will run those values also.
import script1

def mult(a,b):
    print("Result is ",a*b)
    return None

def main():
    x = 10
    y = 20
    mult(x,y)
    script1.addition(x,y)
    return None
if __name__=="__main__":
     main()
    
#Now if I want to see only the value of script2 and do not want to see script1 output.
#import script1
#print("This is script2",__name__)
#value
#script1
#This is script2 __main__
#So if we are printing "__name__" on script1, instead of "__main__" we are getting only script1