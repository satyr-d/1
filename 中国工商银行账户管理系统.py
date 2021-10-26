import os
import random
main = '''
****************************
*    中国工商银行            *
*    账户管理系统            *
*       v1.0              *
****************************

*1、开户                    *
*2、存钱                    *
*3、取钱                    *
*4、转账                    *
*5、查询                    *
*6、Bye!                   *
****************************
'''
print(main)

#初始化银行
bank={}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'street': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="中国工商银行"

#定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(account,name,password,country,province,street,door):
    if len(bank)>=100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[account] = {
            "name":name,
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1

#定义用户入参
def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入您的名称")
    password=input("请输入您的密码")
    print("请输入你的详细信息")
    country=input("\t\t请输入您的国籍")#\t ==tab
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,street,door)
    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，一下是您的相信信息")
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：*****
                   国籍：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province, street, door, bank[account]["money"], bank_name))

def add_money(account, money):
    if account in bank:
        bank[account]["money"] = money
        print("存钱成功")
        return True
    else:
        print("账号不存在")
        return False

def take_money(account, password, money):
    if account in bank:
        if password == bank[account]["password"]:
            if bank[account]["money"] >= money:
                bank[account]["money"] -= money
                print("取钱成功")
                return 0
            else:
                print("余额不足")
                return 3
        else:
            print("密码不对")
            return 2
    else:
        print("账号不存在")
        return 1

def out_money(out_account, in_account, out_password, out_money):
    if out_account in bank:
        if in_account in bank:
            if out_password == bank[out_account]["password"]:
                if bank[out_account]["money"] >= out_money:
                    bank[out_account]["money"] -= out_money
                    bank[in_account]["money"] += out_money
                    print("转账成功")
                    return 0
                else:
                    print("余额不足")
                    return 3
            else:
                print("密码不对")
                return 2
        else:
            print("转入账号不存在")
            return 1
    else:
        print("转出账号不存在")
        return 1

def search(account, password):
    if account in bank:
        if password == bank[account]["password"]:
            info = '''
                               ------------用户信息------------
                               用户名:%s
                               当前账号：%s
                               密码：*****
                               国籍：%s
                               省份：%s
                               街道：%s
                               门牌号：%s
                               余额：%s
                               当前账户的开户行：%s
                           '''
            # 每个元素都可传入%
            print(info % (bank[account]["name"], bank[account]["account"], bank[account]["country"], bank[account]["province"], bank[account]["street"], bank[account]["door"], bank[account]["money"], bank[account]["bank_name"]))

        else:
            print("密码不对")
    else:
        print("账号不存在")

while False==0:
    index=input("请输入您需要的业务")
    if index.isdigit() == True:
        index = int(index)
        if index ==1:
            print("开户")
            useradd()
            print(bank)
        elif index ==2:
            print("存钱")
            add_money(int(input("请输入账号：")), int(input("请输入存入金额：")))
            print(bank)
        elif index ==3:
            print("取钱")
            take_money(int(input("请输入账号：")), input("请输入密码："), int(input("请输入取出金额：")))
            print(bank)
        elif index ==4:
            print("转账")
            out_money(int(input("请输入转出账号：")), int(input("请输入转入账号：")), input("请输入转出账号密码："), int(input("请输入转出金额：")))
            print(bank)
        elif index ==5:
            print("查询")
            search(int(input("请输入账号：")), input("请输入密码："))
        elif index ==6:
            print("下次光临")
            break
    else:
        pass
