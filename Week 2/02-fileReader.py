file = open("movielist.txt", "r")
Lines= file.readlines()

# print (Lines)
count = 0

for line in Lines:
    count += 1
    # print("Line" + str(count)+":" +line.strip())
    print(f"Line {count}: {line.strip()}")
    
    # .format(count, line.strip())
    

# file.close()