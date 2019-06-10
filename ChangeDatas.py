import csv
def readFile():
    try:
        fo = open('data.csv','r')
        data = []
        for line in fo:
            line = line.replace("\n","")
            data.append(line.split(","))
        fo.close()
    except:
        fo = open('data.csv','w')
        data = []
    return data
def writeFile(data):
    f = open('data.csv','w',newline='')
    fi = csv.writer(f)
    for line in data:
        fi.writerow(line)
    print("Write over!")
    f.close()
# ls = [name,studentnumber,sex,phonenumber]
def is_not_Chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return False
    else:
        return True
def Compare(INp,other):
    flag = 1
    if other[0]=='':
        return True
    for i in range(len(INp)):
        if INp[i] != other[i]:
            flag = 0
    if flag:
        return True
    else:
        return False
def not_Continue():
    flag = 'Y'
    flag = input("Do you want to continue?:(Y/n)")
    if flag =='N' or flag =='n':
        return True
    else:
        return False
def getName():
    name = input("Please enter the student's name:")
    while True:
        flag = 0
        for i in range(len(name)):
            if is_not_Chinese(name[i]):
                flag = 1
                break
        if flag == 1:
            name = input("Wrong! Please enter again:")
        else:
            break
    return name
def getStuID():
    stuID  = input("Please enter the student's ID:")
    while True:
        flag = 0
        for i in range(len(stuID)):
            if stuID[i].isdigit():
                flag = 0
            else:
                flag = 1
                break
        if flag == 1:
            stuID = input("Wrong!,Please enter again:")
        else:
            break
    return stuID
def getSex():
    sex = input("Please enter the student's sex(男/女):")
    #print(sex)
    #print(sex !='男' and sex != '女')
    while True:
       if(sex !='男' and sex != '女'):
            sex = input("Wrong!,Please enter again(男/女):")
       else:
            break
    return sex
def getPhNumber():
    phoneNumber  = input("Please enter the student's phonenumber:")
    while True:
        flag = 0
        for i in range(len(phoneNumber)):
            if phoneNumber[i].isdigit():
                flag = 0
            else:
                flag = 1
                break
        if flag == 1:
            phoneNumber = input("Wrong!,Please enter again:")
        else:
            break
    return phoneNumber
def Get():
    name = getName()
    StuID = getStuID()
    Sex = getSex()
    number = getPhNumber()
    k = [name,StuID,Sex,number]
    return k
def insertStu(data):
    print("\nInsert informatiom!\n")
    while True:
        datas = Get()
        flag = 1
        for i in range(len(data)):
            if Compare(datas,data[i]):
                flag = 0
        if flag:
            data += [datas]
            print("{},{},{},{},The student's information writes successfully!".format(datas[0],datas[1],datas[2],datas[3]))
        else:
            print("the information is already exists!")
        if not_Continue():
            break
    return data
def deletStu(data):
    print("\nDelet student's information\n")
    while True:
        k = Get()
        flag = 1
        j = 0
        for i in range(len(data)):
            if Compare(k,data[i]):
                j = i
                flag = 0
                break
        del data[i]
        if flag:
            print("Can't find the information!")
        else:
            print("{},{},{},{},The student's information deletes successfully!".format(k[0],k[1],k[2],k[3]))
        if not_Continue():
            break
    return data
# ls = [name,studentnumber,sex,phonenumber]
def Edit(data,j):
    print("which data do you want to modify?\n1)name\n2)Student'ID\n3)Sex\n4)Phonenumber\n")
    option = input("Your choose:")
    while True:
        chose = option[0]
        if chose == '1':
            data[j][0] = getName()
        elif chose == '2':
            data[j][1] = getStuID()
        elif chose == '3':
            data[j][2] = getSex()
        elif chose == '4':
            data[j][3] = getPhNumber()
        else:
            option = input("Wrong!,Please select again:")
        if not_Continue:
            break
    return data
def editStu(data):
    print("\nEdit the information!\n")
    while True:
        datas = Get()
        flag = 1
        j = 0
        for i in range(len(data)):
            if Compare(datas,data[i]):
                flag = 0
                j = i
        if flag:
            print("Can't find the information!")
        else:
            data = Edit(data,j)
            print("{},{},{},{},The student's information deletes successfully!".format(datas[0],datas[1],datas[2],datas[3]))
            print("{},{},{},{}".format(data[j][0],data[j][1],data[j][2],data[j][3]))
        if not_Continue():
            break
    return data                    
def display(data):
    for line in data:
        print("姓名：{}".format(line[0]))
        print("学号：{}".format(line[1]))
        print("性别：{}".format(line[2]))
        print("电话：{}".format(line[3]))
        print("----------")
    return data
