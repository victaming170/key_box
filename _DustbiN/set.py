import re


# 恢复初始配置
def fct_init_config():
    init_word = 'password'
    with open('iof/setting.pf', 'r') as f1:
        lines = f1.readlines()
    for i in range(len(lines)):
        match1 = re.match('uevi.login_password=', lines[i])
        if match1:
            lines[i] = re.sub('uevi.login_password=([@$\\w]+);', 'uevi.login_password={};'.format(init_word), lines[i])
            break
    with open('iof/setting.pf', 'w') as f1:
        for line in lines:
            f1.write(line)


# 更改并记录密码
def fct_set_password():
    # 交互-获取新密码:
    new_word = ''
    while True:
        scan_word = input("设置新密码:")
        if scan_word == '\t':
            break
        elif re.search('([^@$\\w]+)', scan_word):
            print("密码只能包含@ $ _ 以及字母数字，所以请重新")
        else:
            new_word = scan_word
            print("设置成功！")
            break
    # 将新密码替换进文件:
    try:
        with open('iof/setting.pf', 'r') as f1:
            lines = f1.readlines()
        for i in range(len(lines)):
            match1 = re.match('uevi.login_password=', lines[i])
            if match1:
                lines[i] = re.sub('uevi.login_password=([@$\\w]+);', 'uevi.login_password={};'.format(new_word), lines[i])
                break
        with open('iof/setting.pf', 'w') as f1:
            for line in lines:
                f1.write(line)
    except NameError:
        print("按下Tab键已退出密码设置，未设置新密码。")
