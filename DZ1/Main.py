
def split(s):                           #returns tuple of 2 ints
    half, rem = divmod(len(s), 2)
    return code_num(s[:half + rem]), code_num(s[half + rem:])

def code_num(str):                      #translates set of chars to int
    num = 0
    i = 0
    while i < len(str):
        num += ord(str[i])
        i += 1
    return num

def Feistel(strTup, key, i):            #dunno, this supposed to be kind of Feistel block
    left = strTup[0] ^ (key * 256)
    
    if i % 2 == 0: 
        left = left >> 1
    else:
        left = left << 1
        
    right = left ^ strTup[1]
    return right, left


def start(Key, tickets_number):
    iterations = 15                      #work qite same at high values
    
    try: 
        f = open('Input.md', 'r')
    except IOError:
        print("File with data can not be found!")
        return 0
    
    for line in f:
        result = 0
        i = 0        
        line = line[:len(line) - 1]      #cutting off EOF
        tupleSplit = split(line)
        
        while i < iterations:           #generating some kind of hash from input line
            tupleSplit = Feistel(tupleSplit, Key, i)
            i += 1
        result = (tupleSplit[0] ^ tupleSplit[1])
        result = result // 10
        
        ticket = (result % tickets_number) + 1
        print("{0} - {1}.".format(line, ticket))
        
    f.close()   
    
#Execution from here
try:
    _Key = int(input("Введите ключ: "))
    tickets = int(input("Введите количество билетов: "))
except ValueError:
    print("Вводи нормально!")
else:
    start(_Key, tickets)

