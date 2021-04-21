import random

especial = [".", "?", " ", "!", "\"", "-", "_", "ç", ","]

def create_disk():
    used = []
    for i in range(26):
        used.append( chr(i+65) )
        used.append( chr( i+97 ) )

    for s in especial:
        used.append( s )

    random.shuffle(used)

    return used

def to_disk(used):
    s = ""
    for i in range(len(used)):
        s += str(ord( used[i] )) + " "
    return s

def to_plugboard(config):
    s = ""
    i = 0
    p = 0
    for i in range(26):
        s += chr(i+65) + "-" + config[p] + "\n"
        s += chr(i+97) + "-" + config[p+1] + "\n"
        p += 2

    for st in especial:
        s += st + "-" + config[i] + "\n"
        i+=1
    
    return s

def pick_disks ( disks ):
    random.shuffle(disk_choices)
    temp = disk_choices[0]
    disk_choices.append( temp )
    disk_choices.remove(temp)
    return temp

if __name__ == "__main__":

    #build disks
    disk1 = to_disk( create_disk() )
    print("Created disk\n", disk1)

    disk2 = to_disk( create_disk() )
    print("Created disk\n", disk2) 
    
    disk3 = to_disk( create_disk() )
    print("Created disk\n", disk3) 
    
    disk4 = to_disk( create_disk() )
    print("Created disk\n", disk4)
    
    disk5 = to_disk( create_disk() )
    print("Created disk\n", disk5)

    reflector = to_disk( create_disk() )
    print("Created a reflector\n", reflector)

    plug_board = to_plugboard( create_disk() )
    print("Created a plugboard:\n", plug_board)

    #chose trigerpoints
    max_range = 26*2+len(especial)
    disk1_trigerpoint = random.randint(0,max_range)
    disk2_trigerpoint = random.randint(0,max_range)
    disk3_trigerpoint = random.randint(0,max_range)

    #chose disks
    disk_choices = [0,1,2,3,4]
    disk1_pick = pick_disks(disk_choices)
    disk2_pick = pick_disks(disk_choices)
    disk3_pick = pick_disks(disk_choices)

    #chose start
    max_range = 26*2+len(especial)
    disk1_start = random.randint(0,max_range)
    disk2_start = random.randint(0,max_range)
    disk3_start = random.randint(0,max_range)

    print( "Chose disk trigerpoints: {disk1} {disk2} {disk3}".format(
        disk1 = disk1_trigerpoint,
        disk2 = disk2_trigerpoint,
        disk3 = disk3_trigerpoint
    ))

    print("Chose_disks: {disk1} {disk2} {disk3}".format(
            disk1 = disk1_pick,
            disk2 = disk2_pick,
            disk3 = disk3_pick
    ))

    print( "Chose disk start: {disk1} {disk2} {disk3}".format(
        disk1 = disk1_start,
        disk2 = disk2_start,
        disk3 = disk3_start
    ))

    #config file 
    with open("configuration.dk", "w") as file:
        file.write("disk_order: {disk1} {disk2} {disk3}\n".format(
            disk1 = disk1_pick,
            disk2 = disk2_pick,
            disk3 = disk3_pick
        ))

        file.write( "disk_triger_points: {disk1} {disk2} {disk3}\n".format(
            disk1 = disk1_trigerpoint,
            disk2 = disk2_trigerpoint,
            disk3 = disk3_trigerpoint
        ))

        file.write( "disk_start: {disk1} {disk2} {disk3}\n".format(
            disk1 = disk1_start,
            disk2 = disk2_start,
            disk3 = disk3_start
        ))

        file.write("plug_board:\n")
        file.write(plug_board)

        file.write("reflector:\n")
        file.write(reflector)
        pass

    with open("disks.dk", "w") as file:
        file.write(disk1 + "\n")
        file.write(disk2 + "\n")
        file.write(disk3 + "\n")
        file.write(disk4 + "\n")
        file.write(disk5 + "\n") 
        file.close()