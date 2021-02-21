import yaml
import functions as fct

# macro
PJ_PATH = "D:/WorkspaceMX/Python_PJ/KeyBox/"
F_CONFIG = PJ_PATH + "iof/box_rom.yml"

# say hello
print('==== ==== ===== ==== ====')
print('==== === Key_Box === ====')
print('==== ==== ===== ==== ====')

# load config
try:
    with open(F_CONFIG, 'r', encoding='utf-8') as f_config:
        rom = yaml.load(f_config, Loader=yaml.FullLoader)
except FileNotFoundError:
    rom = {'setting':None, 'notes':None}

if rom['setting']:
    setting = rom['setting']
else:
    print('[ERROR]Setting broken, reset.')
    setting = {'encoding':'utf-8', 'login_password':'password', 'note_content':
    ['WebName', 'URL', 'User', 'TEL', 'Email', 'Password', 'Remark', 'Local_Password']}
if rom['notes']:
    notes = rom['notes']
else:
    notes = {}

# login with password
# login_succ = True
if fct.password_check(setting['login_password']):
    print('Welcome to KeyBox 1.0')
    login_succ = True
else:
    print('Sorry. Bye.')
    login_succ = False

# get existing item index
existed_index = [0]
for k in notes:
    existed_index.append(k)

while login_succ:
    print('Notes:')
    maintain = True
    for k in notes:
        print('{:<2}:{:<16}-{:<24}-{:<16}'.format(k, notes[k][0], notes[k][1], notes[k][2]))
    opt0 = fct.option_button('[OPT0]---What do you want?', 1, 'Exit', 'Edit', 'New', 'Config')
    if opt0 == 0:
        break
    # edit -----------------------------------------------------
    if opt0 == 1:
        opt1_list = existed_index.copy()
        opt1_list[0] = 'Back'
        while True:
            opt1 = fct.option_button('[OPT1]Which one do you want to Edit?', 0, opt1_list)
            if opt1 == 0:
                break
            opt1_k = existed_index[opt1]
            if notes[opt1_k][7] != 'None':
                if fct.password_check(notes[opt1_k][7], 3):
                    print(f'No.{opt1_k}:')
                else:
                    continue
            opt2 = fct.option_button('[OPT2]--', 1, 'Back', 'Alter', 'Delete')
            if opt2 == 0:
                continue
            elif opt2 == 1:
                maintain = False
                fct.alter_item(notes[opt1_k])
            elif opt2 == 2:
                del notes[opt1_k]
                maintain = False
        print()
    # new ---------------------------------------------------------
    elif opt0 == 2:
        for i in range(len(existed_index)+1):
            if i not in existed_index:
                new_item_i = i
                print(f'[INFO ]Create new item No.{new_item_i}')
        new_item = 8*['None']
        fct.alter_item(new_item)
        if new_item[:2] == 2*['None']:
            print('[ERROR]Warnning! Both WebName and URL are empty. New item creation failed.')
        else:
            notes[new_item_i] = new_item
            existed_index.append(new_item_i)
            maintain = False
        print()
    # config ----------------------------------------------------
    elif opt0 == 3:
        opt1 = fct.option_button('[OPT1]Config', 1, 'Back', 'Login_Password')
        if opt1 == 0:
            break
        elif opt1 == 1:
            if fct.password_check(setting['login_password'], 3):
                scan_p = input('New Password for log-in >>> ')
                if scan_p:
                    setting['login_password'] = scan_p
                    maintain = False
        print()
    
    if not maintain:
        rom['setting'] = setting
        rom['notes'] = notes
        with open(F_CONFIG, 'w', encoding='utf-8') as f_config:
            yaml.dump(rom, f_config, default_flow_style=False)

    

