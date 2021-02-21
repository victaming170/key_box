# 登录模块（函数）
import re


# 从文件获取当前登录密码
def fct_get_current_password():
    with open('iof/setting.pf', 'r') as f1:
        line = f1.readline()
        while line:
            match1 = re.match('uevi.login_password=', line)
            if match1:
                current_word = str(re.search('uevi.login_password=([@$\\w]+);', line).group())[20:-1]
                return current_word
            line = f1.readline()
        print('Error, not found previous password！')


# 登录密码检查
def fct_pass_check(pre_str):
    match = False
    fail_num = 0
    max_fail = 3
    last_failure = ''
    while True:
        scan_word = input("验证密码:")
        if scan_word == pre_str:
            print("密码正确，验证通过！")
            match = True
            break
        elif scan_word == last_failure:
            print("重复输入错误密码，请重新输入")
        else:
            fail_num += 1
            if fail_num == max_fail:
                print("({}/{}) 密码错误，验证失败！".format(fail_num, max_fail))
                break
            else:
                print("({}/{}) 密码错误，请重新输入".format(fail_num, max_fail))
            last_failure = scan_word
    return match


# print(fct_get_current_password())
# log_key = 'keyword'
# fct_log_check(log_key)
# print("==== ====end of module \'input\'==== ====")
