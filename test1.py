
# x=[[1,2],[3,4],[4,5]]
# result=[[0,0,0],[0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i]=x[i][j]
# for r in result:
#     print(r)


# def max_elemt(arr,n):
#     max=arr[0]
#     for i in range(1,n):
#         if arr[i]> max:
#             max=arr[i]
#     return max
# arr=[1,3,5,2]
# n=len(arr)
def missing_value(arr,n,low,high):
    range_of_value=[False]*(high-low+1)
    for i in range(n):
        if(low<=arr[i] and arr[i]<=high):
            range_of_value[arr[i]-1]=True
    for x in range(high-low+1):
        if(range_of_value[x]==False):
            print(low+x, end = " ")
arr=[1,3,5,2]
n=len(arr)
low,high=1,5
print
# def __init__(self):
# x=lambda a,b:a*b
# print(x(1,2))




