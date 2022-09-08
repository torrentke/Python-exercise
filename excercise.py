#  age = 2022 - int(input("Mikor születtél?"))

# print(f"Ezek alapján te ", {age}, " éves vagy!")
#  print("Ezek alapján te",age,"éves vagy!")




mixed_dict = {'apples' : 45}

mixed_dict['orange'] = 55


#  print(mixed_dict)

mixed_dict["apricot"] = 77

sorted(mixed_dict, reverse=True)

mixed_dict.pop('apricot')

mixed_dict.pop('orange')
sorted(mixed_dict, reverse=True)

print(mixed_dict)

print(len(mixed_dict))

mixed_dict2 = mixed_dict.copy()

print(mixed_dict2)

len(mixed_dict2)

old_list = [0, 1, 2, 3]

print(old_list)
new_list = old_list

print(new_list)
new_list[1] = 55
print(new_list)

print(old_list)
import copy

newest_list = copy.copy(old_list)

newest_list[0] = 1000
print(newest_list)
print(old_list)
