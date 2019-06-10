def showMeau():
    print("{:*^41}".format("options"))
    print("|\t{:^20}\t|".format("欢迎使用学生信息系统"))
    print("| {:<20}\t\t|".format("1)添加学生信息"))
    print("| {:<20}\t\t|".format("2)修改学生信息"))
    print("| {:<20}\t\t|".format("3)删除学生信息"))
    print("| {:<20}\t\t|".format("4)查看全部信息"))
    print("| {:<20}\t\t|".format("5)退出程序"))
    print("{:*^41}".format("*******"))
#def Connection(data):
#    option = input("Please select:")
#    flag = option[0]
#    if flag == '1':
#        data = insertStu(data)
#        writeFile(data)
#    elif flag == '2':
#        data = editStu(data)
#        writeFile(data)
#    elif flag == '3':
#        data = deletStu(data)
#        writeFile(data)
#    elif flag == '4':
#        data = display(data)
#        writeFile(data)
#    elif flag == '5':
#        break
#    else:
#        print("Wrong!,please select again.")