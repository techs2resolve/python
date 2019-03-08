# In this exercise we are finding common numbers from 2 list

#output = [1,2,3,4], [1,2,5,7]

def common_finder(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_finder([1,2,3,4], [1,2,5,7]))




