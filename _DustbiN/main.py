import log
import set
import work

current_password = log.fct_get_current_password()
login = log.fct_pass_check(current_password)

if login:
    print("==== ==== ==== ====\n====   KeyBox   ====\n==== ==== ==== ====\n")
    # 选择设置或是更新记录
    while True:
        mode = input("选项 0:退出\t1:编辑记录\t2:设置 choice=")
        if mode == '0':
            break
        elif mode == '1':
            all_item = work.fct_review_all_data()
            while work.fct_update(all_item):
                work.write_back(all_item)
                all_item = work.fct_review_all_data()
        elif mode == '2':
            while True:
                mode0_x = input("选项 0:返回；\t1:修改登录密码 choice=")
                if mode0_x == '0':
                    break
                elif mode0_x == '1':
                    mode00_x = log.fct_pass_check(log.fct_get_current_password())
                    if mode00_x:
                        set.fct_set_password()
                    else:
                        print("身份核验未通过，退出密码修改")
                        break
                else:
                    print("暂时没有此设置项，请重新")
else:
    print("登录失败！")

end = input("按任意键关闭窗口退出")
print("= 退出程序 = end with {}".format(end))
