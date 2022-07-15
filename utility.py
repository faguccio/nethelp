# in all function ip is generally a list of 4 integers


# takes an ip as a string written like 11001.1011110. etc and return an array of int
def bitstring_to_array(addr):
    return [ int(x,2) for x in addr.split(".")]


def array_to_bitstring(addr):
    addr = [((8-len(str(bin(x)[2:])))*"0" + str(bin(x)[2:])) for x in addr]
    return ".".join(addr)


def mynot(addr):
    bit = array_to_bitstring(addr)
    res = ""
    
    for x in bit:
        a = x
        if (x == "0"):
            a = "1"
        if (x == "1"):
            a = "0"
        
        res += a
    
    res = bitstring_to_array(res)
    check_ip(res, "sono in mynot")
    return res


def add_one(addr):
    if (addr[3] < 255):
        addr[3] += 1
    elif (addr[2] < 255):
        addr[3] = 0
        addr[2] += 1
    elif (addr[1] < 255):
        addr[3] = 0
        addr[2] = 0
        addr[1] += 1
    else:
        addr[3] = 0
        addr[2] = 0
        addr[1] = 0
        addr[0] += 1
    
    return addr


def check_ip(addr, info="no info"):
    if (len(addr) > 4):
        raise Exception(f"IP {addr} has too many elements. Additional info: {info}")
    for x in addr:
        if (x > 255 or x < 0):
            raise Exception(f"Value {x} in {addr} is not 8bit")


def ip_to_array(x):
    tmp = [int(y) for y in x.split(".")]
    check_ip(tmp)
    return tmp


def array_to_ip(x):
    check_ip(x)
    return ".".join([str(a) for a in x])



# takes a mask expressed as an int and return the corresponding mask expressed as IP
def mask_to_ip(x):
    mask_bitstring = x*"1" + (32-x)*"0"
    res = ".".join([mask_bitstring[i:i+8] for i in range(0, len(mask_bitstring), 8)])
    res = bitstring_to_array(res)
    check_ip(res, "should be a mask (in mask_to_ip)")
    return res

# non controllo sia maschera valida
def ip_to_mask(addr):
    mask_bitstring = array_to_bitstring(addr)
    res = 0
    for x in mask_bitstring:
        if(x == "1"):
            res += 1
        if (x == "0"):
            return res
    return res

# I expect ip and mask as array of int
def find_net_ip(ip, mask):
    net = [a & b for (a,b) in zip(ip, mask)]
    check_ip(net, "Sto trovando il net address")
    
    print(f"{array_to_bitstring(ip)}    (ip)")
    print(f"{array_to_bitstring(mask)}    (mask)")
    print(f"{array_to_bitstring(net)}    (net ip)")    
    print(f"{array_to_ip(net)}    (net ip, cute)")



def find_hosttype(ip, mask, name="calcolo degli host"):
    net = [a & b for (a,b) in zip(ip, mask)]
    first = net.copy()
    first[3] += 1
    broadcast = [ (a + b) for (a,b) in zip(net, mynot(mask))] #imaskp + not(mask)
    router = broadcast.copy()
    router[3] -= 1
    last = router.copy()
    last[3] -= 1

    check_ip(first, "first addr in find_hosttype")
    check_ip(broadcast, "broadcast addr in find_hosttype")
    check_ip(last, "last addr in find_hosttype")
    check_ip(router, "router addr in find_hosttype")

    print(f"------{name}------")
    print(f"{array_to_bitstring(ip)}    (ip)")
    print(f"{array_to_bitstring(mask)}    (mask)")
    print(f"{array_to_bitstring(net)}    (net ip)")
    print(f"{array_to_ip(mask)}    (mask, cute)") 
    print(f"{array_to_ip(net)}/{ip_to_mask(mask)}    (net ip, cute)")
    print()
    print(f"{array_to_bitstring(first)}    (first)")
    print(f"{array_to_ip(first)}    (first, cute)")
    print()
    print(f"{array_to_bitstring(net)}    (net ip)")    
    print(f"{array_to_bitstring(mynot(mask))}    (mask inversa)")    
    print(f"{array_to_bitstring(broadcast)}    (broadcast ip)")    
    print(f"{array_to_ip(broadcast)}    (broadcast, cute)")
    print(f"{array_to_ip(router)}    (router, cute)")
    print(f"{array_to_ip(last)}    (last, cute)")
    print("--------------------------")
    return(router, net, broadcast)


def subnet(ip, mask, default):
    net = ip
    broadcast = 0
    if default == "non c'è":
        default, net, broadcast = find_hosttype(ip, mask, "bignet")
        

    n = int(input("Quante subnet? "))

    names = []
    for x in range(n):
        names.append(input("Nome rete? (parti dalla più big) "))
    
    last = net
    for name in names:
        MAX = int(input(f"Quanti host per la rete {name}? "))
        new_mask = 1
        while 2**new_mask < MAX + 3:    # 3 per net, broadcast e router
            new_mask += 1

        new_mask = mask_to_ip(32 - new_mask)

        defrouter, net_new, broadcast = find_hosttype(last, new_mask, name)
        print(f"{array_to_ip(default)}    (def router)" )
        print("--------------------")
        subnet(net_new, new_mask, defrouter)

        last = add_one(broadcast.copy())
        
    

def valid(ip, mask):
    net = [a & b for (a,b) in zip(ip, mask)]
    first = net.copy()
    first[3] += 1
    broadcast = [ (a + b) for (a,b) in zip(net, mynot(mask))] #imaskp + not(mask)
    router = broadcast.copy()
    router[3] -= 1
    last = router.copy()
    last[3] -= 1

    check_ip(first, "first addr in find_hosttype")
    check_ip(broadcast, "broadcast addr in find_hosttype")
    check_ip(last, "last addr in find_hosttype")
    check_ip(router, "router addr in find_hosttype")

    print(f"{array_to_bitstring(ip)}    (ip)")
    print(f"{array_to_bitstring(mask)}    (mask)")
    print(f"{array_to_bitstring(net)}    (net ip)")
    print(f"{array_to_ip(mask)}    (mask, cute)") 
    print(f"{array_to_ip(net)}/{ip_to_mask(mask)}    (net ip, cute)")
    print()
    print(f"{array_to_bitstring(first)}    (first)")
    print(f"{array_to_ip(first)}    (first, cute)")
    print()
    print(f"{array_to_bitstring(net)}    (net ip)")    
    print(f"{array_to_bitstring(mynot(mask))}    (mask inversa)")    
    print(f"{array_to_bitstring(broadcast)}    (broadcast ip)")    
    print(f"{array_to_ip(broadcast)}    (broadcast, cute)")
    print(f"{int(''.join((array_to_bitstring([a & b for (a,b) in zip(mynot(mask), ip)]).split('.'))), 2)}     nesimo host")
    print()
    print(f"{array_to_ip(router)}    (router, cute)")
    print(f"{array_to_ip(last)}    (last, cute)")
    print("--------------------------")
    return(router, net, broadcast)
