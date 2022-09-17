# Python3 implementation to find the 
# count of leap years in given 
# range of the year 
  
# Function to calculate the number 
# of leap years in range of (1, year) 
def calNum(year) : 
  
    return (year // 4) - (year // 100) + (year // 400) 
  
# Function to calculate the number 
# of leap years in given range 
def leapNum(l, r) :
  
    l -= 1 
    num1 = calNum(r)
    num2 = calNum(l)
    print(num1 - num2)
  
# Driver Code 
if __name__ == "__main__" : 
  
    l1 = 2011
    r1 = 2013
    leapNum(l1, r1)
    ''.replace
    # l2 = 400
    # r2 = 2000 
    # leapNum(l2, r2)