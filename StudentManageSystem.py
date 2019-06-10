#以列表的方式储存学生信息，列表元素是三元组(name,sex,number)
from ChangeDatas import *
from inPut import *
#思路：一次性将数据读入一个二维列表，对二维列表进行修改，最后写入程序
while True:
#读入数据
    data = readFile()
#用户操作选项
    showMeau()
#Connention
    option = input("Please select:")
    flag = option[0]
    if flag == '1':
        data = insertStu(data)
        writeFile(data)
    elif flag == '2':
        data = editStu(data)
        writeFile(data)
    elif flag == '3':
        data = deletStu(data)
        writeFile(data)
    elif flag == '4':
        display(data)
    elif flag == '5':
        break
    else:
        print("Wrong!,please select again.")
    