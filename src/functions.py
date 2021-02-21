

def password_check(pre_password_, max_fail_times_=3):
    permit = False
    scan = ''
    fail_times = 0
    last_fail = ''
    while True:
        scan = input('Password: >>> ')
        if scan == pre_password_:
            # print('Success.')
            permit = True
            break
        elif scan == last_fail:
            print('>Repeat the wrong password.')
        else:
            fail_times += 1
            if fail_times == max_fail_times_:
                print('>Wrong. Reaching the failure limit, exit.')
                break
            else:
                print(f'>[{fail_times}/{max_fail_times_}]Wrong. Try again, pls.')
    return permit


def get_legal_str(show_='Input:', ban_list_={'/', '\\', '@', '|', ':', '*', '<', '>', '?', '"'}):
    while True:
        scan = input(show_ + '\t>>>')
        check = set(scan) &ban_list_
        if check == set():
            return scan
        else:
            print("Don't contain the following characters: ", end='')
            for c in ban_list_:
                print(c, ' ', end='')
            print()


def alter_item(notes_):
    name = ['WebName', 'URL', 'User', 'TEL', 'Email', 'Password', 'Remark', 'LocalPassword']
    opt0_list = [name[i]+':'+notes_[i] for i in range(len(name))]
    opt0_list.insert(0, 'Exit')
    while True:
        opt0 = option_button('--alter--', 0, opt0_list)
        if opt0 == 0:
            break
        print(name[opt0-1], ':', notes_[opt0-1], ' -> ')
        scan0 = input()
        if scan0:
            notes_[opt0-1] = scan0
            opt0_list[opt0] = name[opt0-1] + ':' + notes_[opt0-1]


# show all options, get the choice of user. descrip_=[str], default_=[int], options_=n*[str] or 1*list
def option_button(descrip_, default_, *options_):
    # show the option description
    print(descrip_)
    if len(options_) == 1 and type(options_[0]) == list:
        options_ = options_[0]
    options_n = len(options_)
    # get default choice
    try:
        default_ = int(default_)
    except ValueError:
        default_ = 0
        print('>[ERROR-option_button]Invalid default option, reset to 0.')
    else:
        if default_ >= options_n:
            default_ = 0
            print('>[ERROR-option_button]Invalid default option, reset to 0.')
    # show options
    for n in range(options_n):
        if n != default_:
            print(f'({n}) {options_[n]}')
        else:
            print(f'[{n}] {options_[n]}')
    # get choice of user
    while True:
        button = input('>>> ')
        if not button:
            button = default_
            break
        elif button in [str(n) for n in range(options_n)]:
            break
        else:
            print('>Invalid option, try again pls.')
    return int(button)

