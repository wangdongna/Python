from ToolsChest.datools import paramupdate

fromfile = 'userdata.csv'
tofile = 'user_set_data.txt'
names = ['电机额定电压', '电机额定电流', '变频器额定输入电压']
values = ['1000', '600', '50']

paramupdate.writevalues(fromfile, tofile, names, values, '10')

