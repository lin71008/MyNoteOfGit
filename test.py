import os

common_unit = {'unit':1, 'rare_stack':16, 'stack':64, 'shulker_box':1728, 'double_box':3456}
def cuu(count, unit=None):
	if unit != None:
		return int(count)*common_unit[str(unit)]
	else:
		return int(count)
def cuu_list(item_list):
	counter = 0
	for item in item_list:
		counter += cuu(item[0], item[1])
	return counter

print(cuu(16))
print(cuu(1,'stack'))
print(cuu_list([[3,'stack'],[1,'stack']]))