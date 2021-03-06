import random

especial = [".", "?", " ", "!", "\"", "-", "_", "ç", ","]
decoder = {}
encoder = {}

max_range = 10+26*2+len(especial)

def start_decoder():
    i = 0
    #numbers
    bot = ord("0")
    for j in range(10):
        decoder[ i ] = chr( bot+j )
        encoder[ chr( bot+j ) ] = i
        i+=1

    #capital
    bot = ord("A")
    for j in range(26):
        decoder[ i ] = chr( bot+j )
        encoder[ chr( bot+j ) ] = i
        i+=1

    #lower
    bot = ord("a")
    for j in range(26):
        decoder[ i ] = chr( bot+j )
        encoder[ chr( bot+j ) ] = i
        i+=1

    #especial
    for c in especial:
        decoder[i] = c
        encoder[c] = i
        i+=1

def create_disk():
    temp = list( range(max_range) )
    random.shuffle(temp)
    return temp

def to_disk( arr ):
    s = ""
    for i in arr:
        s += str(i) + " "
    return s


def to_plugboard(config):
    s = ""
    i = 0
    #numbers
    bot = ord("0")
    for j in range(10):
        s += chr( bot+j ) + "-" + decoder[config[i]] + '\n'
        i += 1

    #capital
    bot = ord("A")
    for j in range(26):
        s += chr( bot+j ) + "-" + decoder[config[i]] + '\n'
        i += 1

    #lower
    bot = ord("a")
    for j in range(26):
        s += chr( bot+j ) + "-" + decoder[config[i]] + '\n'
        i += 1

    #especial
    for c in especial:
        s += c + "-" + decoder[config[i]] + '\n'
        i += 1
    
    return s

def pick_disks ( disks ):
    random.shuffle(disks)
    temp = disks[0]
    disks = disks[1:]
    return temp

if __name__ == "__main__":

    start_decoder()

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
    disk1_trigerpoint = random.randint(0,max_range)
    disk2_trigerpoint = random.randint(0,max_range)

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

    print( "Chose disk trigerpoints: {disk1} {disk2}".format(
        disk1 = disk1_trigerpoint,
        disk2 = disk2_trigerpoint
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

        file.write( "disk_triger_points: {disk1} {disk2}\n".format(
            disk1 = disk1_trigerpoint,
            disk2 = disk2_trigerpoint,
        ))

        file.write( "disk_start: {disk1} {disk2} {disk3}\n".format(
            disk1 = disk1_start,
            disk2 = disk2_start,
            disk3 = disk3_start
        ))

        file.write("plug_board:\n")
        file.write(plug_board)

        file.write("reflector: ")
        file.write(reflector)
        file.write("\n")

        file.write("disks:\n")
        file.write(disk1 + "\n")
        file.write(disk2 + "\n")
        file.write(disk3 + "\n")
        file.write(disk4 + "\n")
        file.write(disk5 + "\n") 
        file.close()