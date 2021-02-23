import json


def choose_key(obj, previous_obj=[]):
    print(f'Current path: {len(previous_obj)}')
    if isinstance(obj, dict):
        keys = obj.keys()
        print(f'Keys found: {", ".join(keys)}')
        while True:
            selected_key = input('Navigate to (type _back_ to go back): ')
            if selected_key == '_back_':
                choose_key(previous_obj.pop(), previous_obj)
                break
            try:
                next_obj = obj[selected_key]
                previous_obj.append(obj)
                choose_key(next_obj, previous_obj)
                break
            except KeyError:
                print(f'The key is invalid. Try a valid one')
    else:
        print(f'Here is your value: {obj}')
        input('Type anything to go back\n')
        choose_key(previous_obj.pop(), previous_obj)


if __name__ == '__main__':
    file_name = input('Enter file to open (default: to_parse.json): ')
    if not file_name:
        file_name = 'to_parse.json'

    with open(file_name) as file:
        json_obj = json.load(file)

    choose_key(json_obj)
