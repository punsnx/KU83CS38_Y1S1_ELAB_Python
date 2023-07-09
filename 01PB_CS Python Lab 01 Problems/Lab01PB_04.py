def testPointInput(pointName ,min, max) :
    while(True):
        point = float(input())
        if (point >= min and point <= max):
            return point
        else :
            print(f"invalid {pointName} value, must be between {min} and {max}")
    
midterm = testPointInput("Midterm",0,60)
final = testPointInput("Final",0,60)
total = midterm+final
print(f"Total: {total}\nAverage: {total/2}")