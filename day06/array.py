arr = [1,1,1,2,2,3,4,5,4,3]
# unique_set = set(arr)
# arr_list = list(unique_set)
# print(f"my unique value is {arr_list}", end=" ")
anwser = 0
for i in arr:
    anwser = anwser^i
    print(anwser)
    