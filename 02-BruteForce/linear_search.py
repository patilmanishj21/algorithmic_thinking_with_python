def linear_search(data,target):
    for id,val in enumerate(data):
        if val == target:
            return id
    # for i in range(len(data)):
    #     if data[i]==target:
    #         return i
    return -1



data=[4,5,6,7,8,4,4,4,4,4,4,4,4,4,4,4,4,4,1]
target=1

result=linear_search(data,target)

if result==-1:
    print("Not Found")
else:
    print(f"Item at position : {result} .")