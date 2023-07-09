s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
total_s = s1+s2
m = total_s//60
total_s -= m*60
h = m//60
m -= h*60
print(f'It is {h} hours {m} minutes and {total_s} seconds.')