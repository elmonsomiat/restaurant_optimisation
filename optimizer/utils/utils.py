def resize_rectangles(list_rectangles, safety_dist):
    return [[item + safety_dist for item in rectangle]  for rectangle in list_rectangles]


def repeat_rectangles(list_rectangles, box):
    output_list = []
    for rectangle in list_rectangles:
        rep = int(max(box)//min(rectangle)+1)*int(max(box)//max(rectangle)+1)
        [output_list.append(tuple(rectangle)) for i in range(rep)]
        inv_rectangle = [rectangle[1], rectangle[0]]
        [output_list.append(tuple(inv_rectangle)) for i in range(rep)]
    return output_list


def calculate_rectangles(room_size, security_distance, table_sizes):
    options = resize_rectangles(table_sizes, security_distance)
    rectangles = repeat_rectangles(options, room_size)[0:-3]
    return rectangles
    

def get_room_dims(loop):
    while True:
        try:
            _len = input(f'What is the lenght of space {loop}?: ')
            _wid = input(f'What is the width of space {loop}?: ')
            return [float(_len), float(_wid)]
        except ValueError:
            print('Dimensions should be numbers! Try again...')
        else:
            break
    

def get_security_dist():
    while True:
        try:
            security = input('What is the security distance?: ')
            return float(security)
        except ValueError:
            print('Dimensions should be numbers! Try again...')
        else:
            break

def get_table_dims():
    while True:
        try:
            _len = input('What is the lenght of the table?: ')
            _wid = input('What is the width of the table?: ')
            return [float(_len), float(_wid)]
        except ValueError:
            print('Dimensions should be numbers! Try again...')
        else:
            break