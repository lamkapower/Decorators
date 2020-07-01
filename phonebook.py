import os
import datetime

PHONEBOOK = {
    'book_name': '',
    'contacts': []
    }  

class Logger:
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

class Contact:
    def __init__(self, firstname, secondname, telnum, favorite_contact=False, *args, **kwargs):
        self.firstname = firstname
        self.secondname = secondname
        self.telnum = telnum
        self.favorite_contact = favorite_contact      
        self.args = args
        self.kwargs = kwargs

    def print_user_info(self):
        print('Имя: ', self.firstname)
        print('Фамилия: ', self.secondname)
        print('Телефон: ', self.telnum)
        if self.favorite_contact == False:
            print('В избранных: нет')
        else:
            print('В избранных: ', self.favorite_contact)
        print('Дополнительная информация:')
        for arg1, arg2 in self.args:
            print('\t', arg1, ' :', arg2)
        for kwarg1, kwarg2 in self.kwargs.items():
            print('\t', kwarg1, ' :', kwarg2)

    def __str__(self):
        result = str(self.print_user_info())
        result = result.rpartition('\n')[0]
        return result
    
class Phonebook:

    def book_name(self, phonebook_name):
        global PHONEBOOK
        PHONEBOOK['book_name'] = phonebook_name
        return PHONEBOOK
    
    def add_contact(self, contact_name):
        global PHONEBOOK
        PHONEBOOK['contacts'].append(contact_name)
        return PHONEBOOK

    def execute_contacts(self):
        global PHONEBOOK
        for number , value in enumerate(PHONEBOOK['contacts']):
            print(PHONEBOOK['contacts'][number])
        return PHONEBOOK

    def del_contact_by_number(self, telnumber):
        global PHONEBOOK
        for index, value in enumerate(PHONEBOOK['contacts']):
            if value.telnum == telnumber:
                del(PHONEBOOK['contacts'][index])
        return PHONEBOOK

    def search_favorite_telnum(self):
        global PHONEBOOK
        for value in PHONEBOOK['contacts']:
            if value.favorite_contact == True:
                print(value.telnum)
        return PHONEBOOK
    
    @Logger.log_path('log/')
    def search_contact_by_first_and_second_name(self, firstname, secondname):
        global PHONEBOOK
        for index, value in enumerate(PHONEBOOK['contacts']):
            if value.firstname == firstname and value.secondname == secondname:
                print(PHONEBOOK['contacts'][index])
        return PHONEBOOK


if __name__ == "__main__":
    
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    karl = Contact('Karl', 'Hasbro', '+71236549890', True, telegram='@karl', email='karl@gmail.com')
    PHONEBOOK = Phonebook().book_name('My_testbook')
    PHONEBOOK = Phonebook().add_contact(karl)
    PHONEBOOK = Phonebook().add_contact(jhon)
    PHONEBOOK = Phonebook().search_contact_by_first_and_second_name('Karl', 'Hasbro')

