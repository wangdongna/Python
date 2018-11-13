#-*- coding:utf-8 -*

import pandas as pd

def getcsvdata(filename):
    data = pd.read_csv(filename)
    return data

def getallparamnames(filename):
    data = pd.read_csv(filename)
    names,values = (list(data['name']),list(data['id']))
    return (names,values)

# names is a array
def writevalues(fromfile, tofile, names, values, device, panel='255'):
    data = getcsvdata(fromfile)
    tmps = data[data['name'].isin(names)]
    lines = []

    for tname,tid,value in zip(tmps['name'], tmps['id'], values):
        tmpline = '#' + tname + '\n' + panel + '.' + device + '.' + tid + '=' + value + '\n'
        lines.append(tmpline)

    print(lines)
    writetofile(tofile, lines)
    return lines

#write lines to txt file
def writetofile(filename, lines):
    with open(filename, 'wb+') as f:
        for line in lines:
            f.write(line.encode('utf-8'))
        f.close()
        print("write file to:", filename)

if __name__ == '__main__':
    fromfile = 'userdata.csv'
    tofile = 'user_set_data.txt'
    names = ['电机额定电压','电机额定电流','变频器额定输入电压']
    values = ['1000', '600', '50']

    #writevalues(fromfile, tofile, names, values,'10')
    getallparamnames(fromfile)
