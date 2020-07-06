from utils.utils import calculate_rectangles
from utils.draw_utils import create_diagram
from rectpack import newPacker



def run(room_size_split, security_distance, table_sizes, draw=True):
    
    for room_size in room_size_split:
        _opt_room_size = [dim + security_distance for dim in room_size]
        rectangles = calculate_rectangles(_opt_room_size, security_distance, table_sizes)
        packer = newPacker()
        for r in rectangles:
            packer.add_rect(*r)
        packer.add_bin(*_opt_room_size)
        packer.pack()
        if draw:
            create_diagram(packer[0], security_distance, room_size, 'diagram'+str(room_size))
        else:   
            for box in packer[0]:
                print(box)


def get_room_dims(loop):
    _len = input(f'What is the lenght of space {loop}?: ')
    _wid = input(f'What is the width of space {loop}?: ')
    try:
        return [float(_len), float(_wid)]
        restaurant_list.append([float(_len), float(_wid)])
    except ValueError:
        print('Dimensions should be numbers! Try again...')
        get_room_dims(loop)

def get_security_dist():
    try:
        security = input('What is the security distance?: ')
        return float(security)
    except ValueError:
        print('Dimensions should be numbers! Try again...')
        get_security_dist()


def get_table_dims():
    try:
        _len = input('What is the lenght of the table?: ')
        _wid = input('What is the width of the table?: ')
        return [float(_len), float(_wid)]
    except ValueError:
        print('Dimensions should be numbers! Try again...')
        get_table_dims()

if __name__=='__main__':
    print('Welcome to the restaurant optimiser!')
    print('Hope this can help you! Remember all units are in m.')

    restaurant_list = []
    i = 1
    while True:
        restaurant_list.append(get_room_dims(i))
        _continue = input('Are there any more spaces?(n/y): ')
        _continue = _continue or 'n'
        i += 1
        if _continue=='n':
            break
    security = get_security_dist()
    
    table_list = []
    while True:
        table_list.append(get_table_dims())
        _continue = input('Are there any more table sizes?(n/y): ')
        _continue = _continue or 'n'
        if _continue=='n':
            break
    _draw = input('Do you want to save the outcome as png images?(y/n): ')
    _draw = _draw or 'y'
   
    if _draw=='y':
        draw = True
        print('We are gonna save it in your current location.')
    elif _draw=='n':
        draw = False
        print('Here is your result!')
    run(restaurant_list, float(security), table_list, draw)