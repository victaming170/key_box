import log
# 0编号 1平台 2网址 3账户名 4手机号 5邮箱 6密码	7备注 单项密码


# 读取文件，返回一个列表，其元素为文件每行切片得来的列表，称为记录列表
def fct_review_all_data():
    with open('iof/maindata.pf', 'r', encoding='gbk') as f1:
        lines = f1.readlines()
        all_them = [[]] * len(lines)
        for n in range(len(lines)):
            all_them[n] = lines[n].split()
    return all_them


# 输入从文件读到的所有记录列表，以更新记录
def fct_update(all_item_list):
    item_nums = set()
    for item in all_item_list:
        item_nums.add(item[0])
    print("共有%d条记录." % (len(item_nums)-1))
    while True:
        upmode = input("选项 0:返回\t1:显示\t2:新建\t3:修改\t4:删除 choice=")
        if upmode == '0':
            return False
        elif upmode == '1':		# 显示
            for h in all_item_list:
                item_name = h[1]
                if h[1] == '***':
                    item_name = h[2]
                print('No.{}: {}'.format(h[0], item_name))
            dp_index = fct_num2index(item_nums, all_item_list)
            if dp_index != 0:
                fct_display(all_item_list[dp_index])
        elif upmode == '2':		# 新建
            new_item = fct_create_new()
            if fct_alter_item(new_item):
                all_item_list.append(new_item)
            return True
        elif upmode == '3':		# 修改
            alter_index = fct_num2index(item_nums, all_item_list)
            if alter_index != 0:
                fct_alter_item(all_item_list[alter_index])
                return True
        elif upmode == '4':		# 删除
            del_index = fct_num2index(item_nums, all_item_list)
            if del_index != 0:
                del all_item_list[del_index]
                print("删除成功")
                return True
        else:
            print("不存在此选项，请重新选择")


# 显示
def fct_display(them):
    if them[8] != '***':
        if log.fct_pass_check(them[8]):
            print("编号={};\t网站/服务商={};\t网址={};".format(them[0], them[1], them[2]))
            print("账户名={};\t手机号={};\t邮箱={};".format(them[3], them[4], them[5]))
            print("密码={};\t备注={};".format(them[6], them[7]))
    else:
        print("编号={};\t网站/服务商={};\t网址={};".format(them[0], them[1], them[2]))
        print("账户名={};\t手机号={};\t邮箱={};".format(them[3], them[4], them[5]))
        print("密码={};\t备注={};".format(them[6], them[7]))


# 获得新建记录的编号
def fct_create_new():
    it_num = 0
    them = ['***'] * 9
    with open('iof/maindata.pf', 'r') as f1:
        lines = f1.readlines()
    existed_it_num = []
    for line in lines:
        line_it_num = (line.split())[0]
        existed_it_num.append(int(line_it_num))
    while it_num in existed_it_num:
        it_num += 1
    print("新记录No.%d已创建。" % it_num)
    them[0] = str(it_num)
    return them


# 记录修改，输入一条记录以修改其中的项
def fct_alter_item(them):
    it_sel = input("选项 0:返回\t1:网站/服务商\t2:网址\t3:账户名\t4:手机号码\t5:邮箱\t6:密码\t7:备注\t8:单项密码 choice=")
    while True:
        if it_sel == '0':
            if them[1] == '***' and them[2] == '***':
                print("[1.网站名]或[2.网址]至少填写一个。")
                cancel = input("选项 0:删除本条记录\t1:继续 =")
                if cancel == '0':
                    return False
            else:
                break
        elif it_sel == '1':
            print("当前为{}".format(them[1]), end=',')
            them[1] = input("网站/服务商名称:")
        elif it_sel == '2':
            print("当前为{}".format(them[2]), end=',')
            them[2] = input("网址:")
        elif it_sel == '3':
            print("当前为{}".format(them[3]), end=',')
            them[3] = input("账户名:")
        elif it_sel == '4':
            print("当前为{}".format(them[4]), end=',')
            them[4] = input("手机号码:")
        elif it_sel == '5':
            print("当前为{}".format(them[5]), end=',')
            them[5] = input("邮箱:")
        elif it_sel == '6':
            print("当前为{}".format(them[6]), end=',')
            them[6] = input("密码:")
        elif it_sel == '7':
            print("当前为{}".format(them[7]), end=',')
            them[7] = input("备注:")
        elif it_sel == '8':
            them[8] = input("单项记录密码:")
        else:
            print("请选择有效配置项！")
        it_sel = input("选项 0:返回\t1:网站/服务商\t2:网址\t3:账户名\t4:手机号码\t5:邮箱\t6:密码\t7:备注\t8:单项密码 choice=")
    print("记录No.{}修改完成。".format(them[0]))
    for n in range(len(them)):
        if them[n] == '':
            them[n] = '***'
    return True


# 由记录编号得到它在记录列表中的位置
def fct_num2index(num_set, all_them):
    while True:
        sel_num = input("要操作的记录编号:")
        if sel_num in num_set:
            break
        else:
            print("不存在此条，请重新输入")
    sel_index = 0
    if sel_num != '0':
        for item in all_them:
            if item[0] == sel_num:
                sel_index = all_them.index(item)
    return sel_index


# 输入更新后的记录列表，将其覆盖写入文件
def write_back(all_item_list):
    with open('iof/maindata.pf', 'w', encoding='gbk') as fd:
        # print(all_item_list)
        for item in all_item_list:
            item_ready = ''
            for it in item:
                item_ready += str(it) + '\t'
            item_ready = item_ready[:-1]
            fd.write(item_ready)
            if item != all_item_list[-1]:
                fd.write('\n')
