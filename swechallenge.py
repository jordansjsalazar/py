def travel(num):
    def helper(num, gas, index, stops):
        print("index: " + str(index) + ", gas: " + str(gas) + ", stops: " + str(stops))
        if gas<=0:
            return -1
        if index==len(num)-1:
            return stops+1
        a = helper(num, gas, index+1, stops) + helper(num, gas+num[index], index+1, stops+1)
        return a
    return helper(num, num[0], 1, 0)
    
print(travel([2, 3, 1, 1, 4]))
print(travel([1, 1]))
print(travel([0, 3, 2]))
print(travel([1, 1, 1, 1]))
print(travel([1, 2, 2, 1, 0, 1]))