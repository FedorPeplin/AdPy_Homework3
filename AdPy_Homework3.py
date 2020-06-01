class Contact:
    def __init__(self, name, surname, number, selected=None, **kwargs):
        self.name=name
        self.surname=surname
        self.number=number
        self.selected=selected
        self.additional=kwargs

    def __str__(self):
        if self.selected==None:
            selected='Нет'
        else:
            selected='Да'
        # self.additional.values():
        return 'Имя: ' + self.name+'\n' + \
               'Фамилия: ' + self.surname+ '\n' + \
               'Телефон: ' + self.number + '\n' + \
               'В избранных: ' + selected + '\n' + \
               'Дополнительная информация: ' + '\n' + \
               '\n'.join(key+':'+value for key, value in self.additional.items())

class phonebook(Contact):

    def __init__(self, name, surname, number,bookname, selected=None, additionalcontact={}, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.selected = selected
        self.additional = kwargs
        self.additionalcontact=additionalcontact
        self.bookname=bookname

    def contact_output(self):
        try:
            if self.additionalcontact['name']!=None:
                secondcontact= self.additionalcontact['name'] + ' ' + self.additionalcontact['surname'] + ' имеет номер ' + self.additionalcontact['number']
                return '\nВ телефонной книге под названием "' + self.bookname + '" имеются следующие контакты:' + '\n' + \
                self.name +' ' + self.surname + ' имеет номер ' + self.number + '\n' + secondcontact +'\n'
        except KeyError:
            return '\nВ телефонной книге под названием "' + self.bookname + '" имеются следующие контакты:' + '\n' + \
               self.name + ' ' + self.surname + ' имеет номер ' + self.number

    def adding_contact(self):
        if self.selected==None:
            choice='Нет'
        else:
            choice='Да'
        print ('\nФункция добавления контактов ')
        add_name=input('Введите имя ')
        add_surname=input('\nВведите фамилию ')
        add_number=input('\nВведите номер ')
        add_selected=input('\nВведите, избранный ли контакт ')
        add_additional_names=input('\nВведите названия доп.соц.сетей ')
        add_additional_logins=input('\nВведите логины/адреса в доп.соц.сетях ')
        self.additionalcontact={'name': add_name,'surname': add_surname, 'number':add_number, 'selected':add_selected,
                                   'additional_networks_names':add_additional_names, 'additional_network_logins':add_additional_logins}
        return 'Имена пользователей - ' + self.name + ', ' + self.additionalcontact['name'] + '\n' + \
               'Фамилии пользователей - ' + self.surname + ', ' + self.additionalcontact['surname'] + '\n' + \
               'Номера пользователей - ' + self.number + ', ' + self.additionalcontact['number'] + '\n' + \
               '"Избранность" контакта - ' + choice + ', ' + self.additionalcontact['selected'] + '\n' + \
               'Дополнительные соц.сети первого контакта:\n' + \
               '\n'.join(key + ':' + value for key, value in self.additional.items()) + '\n' \
                'Дополнительные соц.сети только что добавленного контакта:' + '\n' + 'Названия: ' + self.additionalcontact['additional_networks_names'] + '\nЛогины/адреса: '+ self.additionalcontact['additional_network_logins']


    def deleting_contact_by_phone(self):
        fingingnumber=input('\nВведите номер, по которому хотите удалить контакт ')
        if fingingnumber==self.number:
            print('Первый изначальный контакт удалён')
            self.name = None
            self.surname = None
            self.number = None
            self.selected = None
            self.additional = None
        if fingingnumber==self.additionalcontact['number']:
            print('Второй добавленный контакт удалён')
            self.additionalcontact = None
        return 'Удаление завершено'


    def finding_selected(self):
        no='нет'
        if self.selected != None:
            print (self.number + ' номер первого контакта с именем ' + self.name + ' является избранным')
        if self.additionalcontact['selected'] != no:
            print (self.additionalcontact['number'] + ' номер второго добавленного контакта с именем ' + self.additionalcontact['name'] + ' является избранным')
        else:
            print ('Никто не является избранным контактом')
        return 'Поиск избранных контактов завершён'

    def searching_by_name_and_surname(self):
        print ('\n')
        searchname=input('Введите имя для поиска ')
        searchsurname=input('Введите фамилию для поиска ')
        if searchname == self.name:
            if searchsurname == self.surname:
                print ('У контакта '+ searchname + ' ' + searchsurname + ' номер ' + self.number)
        if searchname == self.additionalcontact['name']:
            if searchsurname == self.additionalcontact['surname']:
                print('У контакта ' + searchname + ' ' + searchsurname + ' номер ' + self.additionalcontact['number'])
        return 'Поиск номера по имени и фамилии завершён'

def main():
    if __name__=='__main__':
        jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
        print (jhon)
        john_b=phonebook('Jhon', 'Smith', '+71234567809','phonebook', telegram='@jhony', email='jhony@smith.com')
        print (john_b.contact_output())
        print (john_b.adding_contact())
        print(john_b.contact_output())
        print(john_b.finding_selected())
        print(john_b.searching_by_name_and_surname())
        print(john_b.deleting_contact_by_phone())
main()

