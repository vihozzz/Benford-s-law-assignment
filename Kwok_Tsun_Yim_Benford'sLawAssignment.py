import matplotlib.pyplot as plt
import csv
''' 
    This function is to open the sales data
    after open the file and read it
    sales data is a list for  postal code and sales data
    line.split with comma to make postal code and sales data into 2 items
    [1] means that I only want to get the index 1 item which is sales data
    after file.close(), del salesData to make the output only show the sales data
'''
def checkSalesData():
    salesData = []
    file = open("sales.csv", "r")
    for line in file:
        salesData.append(line.split(",")[1])
    file.close()
    del salesData[0]
    return salesData

'''  
    This function is to get the total number of how many times 
    first digit nubmer 1-9 appeared
    count is list
    fd_list have 9 zero to represent number 1 to 9
    salesData is used to call the function checkSalesData()
    for i in range of the lenght of salesdata I got from the checkSalesData()
    use append to get the salesData's item first digit
    for j in count, use num to represent j turn into integer 
    fd_list[num-1] +=1 means that j = number 1-9 minus 1 turn into 0-8
    which are same as fd_list's index
    after that use += 1 to make the number plus one 
    for example, 123456's first digit is 1, then it will add to the first item of the list
    which it will become [1,.......,0]
'''
def firstDigitCounter():
    i = 0
    j = 0
    count = [] #list
    fd_list = [0,0,0,0,0,0,0,0,0] #list
    salesData = checkSalesData() # call back function
    for i in range(len(salesData)): # for loop
        count.append(salesData[i][0])
    for j in count:#for loop
        num = int(j)
        fd_list[num-1] +=1
    return fd_list   

'''This function is to get the percentage for number 1-9
    m is how many times number 1-9 appeared
    use m to represent number 1-9 and divided 1621 which is the total of the line and then multiply by 100 
    to get the percentage of how many times 1-9 appeared
'''
def firstDigitPercent(fd_list):
    fd_percent = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0] # list
    for m in range(len(fd_list)): # for loop
        fd_percent[m] = float(fd_list[m])/1621 * 100  # get percentage
        print(fd_percent)    
    return fd_percent

first_digit_list = firstDigitCounter()  # use first_digit_lits to represent firstDigitCounter
first_digit_percent = firstDigitPercent(first_digit_list)
for k in range(len(first_digit_percent)): # for loop
    if (first_digit_percent[k] < 29) or (first_digit_percent[k] > 32): # if and else statement
        print("The fraud did not occur")
    else:
        print("The fraud occurs")


# matplotlib 
fig = plt.figure(figsize = (10, 5))
x = ["1","2","3","4","5","6","7","8","9",]
y = first_digit_percent

plt.bar(x, y, color ='blue',width = 0.5)
 
plt.xlabel("number") # x-axis label
plt.ylabel("percentage")  # y-axis label
plt.title("Benford's law graph") # title of the graph
plt.show() # show command

#open file and write
file = open('result.csv', 'w', newline = '')
# use write to represent csv.write(file)
writer = csv.writer(file)
# writerow for number 1-9 and the result of precentage
writer.writerow(["firstDigit", "percentage"])
writer.writerow([1, 31.46206045650833])
writer.writerow([2, 13.818630475015423])
writer.writerow([3, 12.70820481184454])
writer.writerow([4, 11.042566317088218])
writer.writerow([5, 9.006785934608267])
writer.writerow([6, 6.785934608266501])
writer.writerow([7, 5.67550894509562])
writer.writerow([8, 4.256631708821715])
writer.writerow([9, 5.1819864281307835])
#close the file 
file.close()    










    

    







