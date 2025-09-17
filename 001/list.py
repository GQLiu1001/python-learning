# 列表 list
listZ = [1,2,3,4,5,"string"]
print(len(listZ))
listZ.pop(3)
listZ.append("oo")
print(listZ)
listZ.insert(0,"good")
print(listZ) # listZ.sort()
print(listZ)
liseZ = [1,3,5]
listZ.reverse()
print(liseZ)

# 元组 tuple
tuple1 = (1,2,3) #不可修改
print(len(tuple1))
list1 = list(tuple1) # 可以转为列表
list1.append(3)
print(list1)

# 字典 dict 键值对
dict1 = {"name":"zhangsan","age":18}
print(dict1["name"])
print(dict1.get("name"))
dict1["name"] = "lisi"
print(dict1)
dict1.pop("name")
print(dict1)
dict1.clear()
print(dict1)
dict1["good"] = 1
print(dict1)

# 集合 set 无重复元素 无顺序
set1 = {1,3,4,5,5} # 自动去重
print(set1)
# set1[0] 会报错
set1.add(6)
print(set1)
set1.remove(6)
print(set1)
set1.clear()
print(set1)
set1.add(1)
set1.add(2)
print(set1)
set2 = {1,2,3,4}
print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set2))

# 除了 数字 布尔 之外全是引用类型