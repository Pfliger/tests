documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def search_by_number(documents, num_doc):
    for doc in documents:
        if doc['number'] == num_doc:
            print(f'\nДокумент пренадлежит: {doc["name"]}')
            res = doc['name']
            return res
    res = f'\nдокумента с номером: {num_doc} не зарегистрировано'
    return res


def shelf_search(dir_list, num_doc):
    for num_shelf in dir_list:
        if num_doc in dir_list.get(num_shelf):
            print(f'\nдокумент с номером: {num_doc} находится на полке номер {num_shelf}')
            res = num_shelf
            return res
    res = f'\nдокумент с номером {num_doc} не числится на полках'
    return res


def all_doc(doc_list):
    res = []
    for doc in doc_list:
        res.append({'type': doc['type'], 'number': doc['number'], 'name': doc['name']})
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}" ')
    return res


def add_doc(doc_list, dir_list):
    new_doc = {}
    new_doc["type"] = input('\nвведите тип документа: ')
    new_doc["number"] = input('\nвведите номер документа: ')
    new_doc["name"] = input('\nвведите имя владельца')
    shelf = input('\nвведите номер полки для хранения документа: ')
    if shelf in dir_list.keys():
        new_entry = dir_list.get(shelf)
        new_entry.append(new_doc['number'])
        dir_list[shelf] = new_entry
        doc_list.append(new_doc)

        print(doc_list)
        print(dir_list)
    else:
        print(f'\nполки с номером: {shelf} еще не существует')
    return doc_list, dir_list


def del_doc(doc_list, dir_list):
    doc_num = input('\nвведите номер документа: ')
    res = bool
    for i, doc in enumerate(doc_list):
        if doc_num == doc['number']:
            del (doc_list[i])
            for entry in dir_list.values():
                if doc_num in entry:
                    entry.remove(doc_num)
            res = True
            print(f'документ номер {doc_num} удален')
            print(doc_list)
            print(dir_list)
            break
        else:
            res = False
    if res == False:
        print(f'\nдокумента с номером: {doc_num} не зарегистрировано')
    return res


def move_doc(dir_list):
    doc_num = input('\nвведите номер документа: ')
    res_shelf = False
    res_doc = False
    for doc in dir_list.values():
        if doc_num in doc:
            res_doc = True
            shelf_num = input('\nвведите номер полки на которую переместить документ: ')
            for shelf in dir_list:
                if shelf_num == shelf:
                    res_shelf = True
                    doc.remove(doc_num)
                    break
            if res_shelf == False:
                print(f'\nполки с номером: {shelf_num} не существует')
                break
    if res_doc == True and res_shelf == True:
        dir_list[shelf].append(doc_num)
    if res_doc == False:
        print(f'\nдокумента c номером: {doc_num} не существует')
    return dir_list


def add_shelf(dir_list):
    new_shelf = input("\nвведите новый номер полки: ")
    res = False
    for shelf in dir_list:
        if new_shelf == shelf:
            res = True
            break
    if res == False:
        dir_list.setdefault(new_shelf, [])
    else:
        print(f'\nполка с номером: {new_shelf} уже существует')
    return dir_list


def main():
    help = f'СПИСОК КОМАНД: \np или people - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит. \n' \
           f's или shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится. \n' \
           f'l или list - команда, которая выведет список всех документов. \n' \
           f'a или add - команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. \n' \
           f'd или delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. \n' \
           f'm или move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. \n' \
           f'as или add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. \n' \
           f'h или help - команда для вызова справки \nq или quit - команда для выхода из приложения'
    print(help)
    while True:
        user_input = input('\nВведите команду: ')
        if user_input == 'p' or user_input == 'people':
            num_doc = input('\nвведите номер документа: ')
            search_by_number(documents, num_doc)
        elif user_input == 's' or user_input == 'shelf':
            num_doc = input('\nвведите номер документа: ')
            shelf_search(directories, num_doc)
        elif user_input == 'l' or user_input == 'list':
            all_doc(documents)
        elif user_input == 'a' or user_input == 'add':
            print(add_doc(documents, directories))
        elif user_input == 'd' or user_input == 'delete':
            print(del_doc(documents, directories))
        elif user_input == 'm' or user_input == 'move':
            print(move_doc(directories))
        elif user_input == 'as' or user_input == 'add shelf':
            print(add_shelf(directories))
        elif user_input == 'h' or user_input == 'help':
            print(help)
        elif user_input == 'q':
            print('\nДо свидания!')
            break
        else:
            print('\nтакой команды нет в списке.')


if __name__ == '__main__':
    main()
