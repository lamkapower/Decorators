import datetime
import os

def log_path(path):
    def logger(import_function):
        def log_action(*args, **kwargs):
            initial_date = datetime.datetime.now()
            initial_date = initial_date.strftime('%a-%H-%M-%S')
            result = import_function(*args, **kwargs)
            with open(os.path.join(f'{path}log.{initial_date}.txt'), 'w', encoding='utf-8') as f:
                f.write(f'''
                Имя вызываемой функции: {import_function}
                С аргументами: {args}, {kwargs}
                Результат выполнения функции:
                {result}
                ''')
            return result
        return log_action
    return logger