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

db, st, un = 1, 2, 3

print(cuu_list([[db,'double_box'],[st,'stack'],[un,'unit']]))