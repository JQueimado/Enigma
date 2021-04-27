# Consts 
CONFIG_FILE = "configuration.dk"
ESPECIAL = [".", "?", " ", "!", "\"", "-", "_", "ç", ","]
## lib ##
decoder = {}
encoder = {}

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
    for c in ESPECIAL:
        decoder[i] = c
        encoder[c] = i
        i+=1

max_range = 10+26*2+len(ESPECIAL)

## Disks ##
disks = []

start_pos = []

turn_point = []

## Reflector ##
reflector = []

## Cable board ##
plug_board = {}

def readConfig():
    diskNumber = []

    lines = []
    with open(CONFIG_FILE, "r") as file:
        lines = file.readlines()

    for i in range( len(lines) ):
        line = lines[i]

        if line.endswith("\n"):
            line = line[:-1]
        
        if line.startswith("disk_order:") and len(diskNumber) == 0:
            #process disk order
            temp = line.split(" ")
            temp = temp[1:]
            for c in temp:
                diskNumber.append( int(c) )
        
        elif line.startswith("disk_triger_points:") and len(turn_point) == 0:
            temp = line.split(" ")
            temp = temp[1:]
            for c in temp:
                turn_point.append( int(c) )

        elif line.startswith("disk_start:") and len(start_pos) == 0:
            temp = line.split(" ")
            temp = temp[1:]
            for c in temp:
                start_pos.append( int(c) )

        elif line.startswith("plug_board:") and len(plug_board) == 0:
            i += 1
            for j in range( max_range ):
                line = lines[i]
                if line.endswith("\n"):
                    line = line[:-1]
                
                temp = line.split("-")
                if( len(temp) == 3):
                    if( temp[2] != '' ):
                        plug_board[ encoder["-"] ] = encoder[ temp[2] ]
                    else:
                        plug_board[ encoder[ temp[0] ] ] = encoder["-"]
                else:
                    plug_board[ encoder[ temp[0] ] ] = encoder[ temp[1] ]
                i += 1

        elif line.startswith("reflector:") and len(reflector) == 0:
            if( line.endswith(" ") ):
                line = line[:-1]
            temp = line.split(" ")
            temp = temp[1:]
            for c in temp:
                reflector.append( int(c) )

        elif line.startswith("disks:") and len(disks) == 0:
            i += 1
            for j in diskNumber:
                line = lines[i + j]
                if line.endswith("\n"):
                    line = line[:-1]
                
                if( line.endswith(" ") ):
                    line = line[:-1]
                temp = line.split(" ")
                temp2 = []
                for c in temp:
                    temp2.append( int(c) )
                disks.append(temp2)

def diskOutput( inpt, disk ):
    
    pos = start_pos[disk] + inpt
    
    if( pos >= max_range ):
        pos = pos - max_range
    
    return disks[disk][pos]



def cypherChar( c ):
    if not ( c.isalpha() or (c in ESPECIAL) ):
        return chr(0)
    i = encoder[c]
    
    plug1res = plug_board[i] #plugboard
    
    diskres = diskOutput(plug1res,0) #disk1
    diskres = diskOutput(diskres,1) #disk2
    diskres = diskOutput(diskres,2) #disk3

    reflectorres = reflector[diskres] #reflector

    diskres = diskOutput(reflectorres,2) #disk1
    diskres = diskOutput(diskres,1) #disk2
    diskres = diskOutput(diskres,0) #disk3

if __name__ == "__main__":
    start_decoder()

    readConfig()
    cypherChar("c")
    cypherChar("c")
    cypherChar("c")
    cypherChar("c")
    pass