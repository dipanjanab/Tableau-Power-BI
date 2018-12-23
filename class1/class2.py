mylist = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,1,1,1,1,1,1,4,4,4,4,5,5,5]

#outputstring = "Tell e a number :"

#num = int(input(outputstring))

frequency = {}

for num in mylist:
    if num in frequency:
        val = frequency[num]
        val = val+1
        frequency[num] = val
    else:
        frequency[num] = 1

print(frequency)

outputstring = "Tell me a number"

num =int(input(outputstring))

