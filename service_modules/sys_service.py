import dotenv
import os
import path

def load_env_variables():
    config = {}
    curr_dir = os.getcwd()
    hvost = (curr_dir[-1:-6:-1])[-1::-1]
    if hvost == 'tests':
        path_str = str(os.getcwd())[:-6]
        os.chdir(path_str)
    if os.path.isfile('prog_config.env'):
        config = dotenv.dotenv_values('prog_config.env')
    else:
        print('Prog_config.env пустой или не существует')
        print('Работа программы завершена')
        print()
        exit()
    return(config)

def write_token(config):
    if 'YA_TOKEN'not in config.keys():
        print()
        config['YA_TOKEN'] = input('Введите Ваш Яндекс.Токен: ')
        with open('prog_config.env', 'a') as pcf:
            pcf.write(f"YA_TOKEN={config['YA_TOKEN']}\n")
    return config
