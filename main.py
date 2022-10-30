from service_modules.sys_service import load_env_variables, write_token
from service_modules.ya_service import upload_starter


if __name__ == '__main__':

    config = load_env_variables()

    print()
    print('Задача: Сохранение файла на Яндекс.Диск')

    write_token(config)

    upload_starter(config)

    print('Работа программы завершена')
    print()
