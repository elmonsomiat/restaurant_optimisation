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

            
if __name__=='__main__':
    print('Welcome to the restaurant optimiser!')
    print('Hope this can help you! Remember all units are in m.')

    restaurant_list = []
    i = 1
    while True:
        _len = input(f'What is the lenght of space {1}?: ')
        _wid = input(f'What is the width of space {1}?: ')
        restaurant_list.append([float(_len), float(_wid)])
        _continue = input('Are there any more spaces?(y/n): ')
        i += 1
        if _continue=='n':
            break
        
    
    security = input('What is the security distance?:')
    
    table_list = []
    while True:
        _len = input('What is the lenght of the table?: ')
        _wid = input('What is the width of the table?: ')
        table_list.append([float(_len), float(_wid)])
        _continue = input('Are there any more table sizes?(y/n): ')
        if _continue=='n':
            break
    _draw = input('Do you want to save the outcome as png images?(y/n)')
   
    if _draw=='y':
        draw = True
        print('We are gonna save it in your current location.')
    elif _draw=='n':
        draw = False
        print('Here is your result!')
    run(restaurant_list, float(security), table_list, draw)