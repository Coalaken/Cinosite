import json


def pars(file):
    with open(file, 'rb') as file:
        count = 1
        ans = []
        a = file.readline()
        new_dict = json.loads(a.decode())
        # print(new_dict)
        ans.append({new_dict['level']: new_dict['message']})
        print(ans)
        # !!! Добавить статус модуля в JSON logger
        
pars('src/django_info.log')
print("End")
        