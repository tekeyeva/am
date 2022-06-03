def find(dict, value):
    ans = []
    for key in dict:
        if dict[key] == value:
            ans.append(key)
    return ans

	
print(find({1:2, 2:3, 3:2, 5:2, 6:5},2))
