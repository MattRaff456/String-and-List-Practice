#String %
text = ( #Python usually cannot have text on different lines
    "%d little pigs come out, " #This method allows for that as well as the
    "or I'll %s, and I'll %s, " #spacing of the text
    "and I'll blow your %s down."
    % (3, 'huff', 'puff', 'house') #%d is the number, %s is huff, %s is puff, %s is house
    #%d stands for int, %s stands for string
)

print(text)

#String format
value = 2.89939821983
print(f'Rounded = {value:.2f}') #It does not truncate like how most languages would, it actually rounds
big = [{'name':'Bill', 'addr':'15 Jones', 'bonus':'1'},
       {'name':'John', 'addr':'199 Road', 'bonus': '8'}]
for person in big: #For loop to print every name in big
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')
    #Prints out spaces before each entry by the specified number.

#String slices
mean = 'Meeaann'
print(mean[0], mean[1:3], mean[-1])
#Index 0 is at M, index 1-3 excludes 3 but includes 1, index -1 is n

#List slices
list = ['a', 'b', 'c', 'd']
list[0:2] = 'z' #The values at list[0:2] will be assigned z. That excludes 2, so a & b change.
print(list)

#FOR and IN for list
squares = [1,4,9,16]
sum = 0
for num in squares: #Iterate through every value in the list and add it to the sum
    sum += num
print(sum)
list2 = ['Alpha', 'Centuri', 'Stellaris']
if 'Stellaris' in list2: #Checks if Stellaris is in list2
    print('Cool')

#List methods
list3 = ['Machine', 'Intelligence', 'Empire']
list3.append('Stellaris') #Append Stellaris to the list
list3.insert(2, 'Civics') #Insert Civics at index 2 which is after Empire
list3.extend(['Learning', 'Curve']) #Add these 2 elements at the end
print(list3)
print(list3.index('Stellaris')) #The index where Stellaris is at
list3.remove('Machine') #Remove machine from the list
list3.pop(1) #Delete the value at index 1 which is civics
print(list3)