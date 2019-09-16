#!/usr/bin/env python3

from time import sleep
from RPi import GPIO as g


g.setmode(g.BCM)
g.setwarnings(False)

pin = 26
g.setup(pin,g.OUT)

letter = {
            ' ':' ',
            'a':'sl',
            'b':'lsss',
            'c':'lsls',
            'd':'lss',
            'e':'s',
            'f':'ssls',
            'g':'lls',
            'h':'ssss',
            'i':'ss',
            'j':'slll',
            'k':'lsl',
            'l':'slss',
            'm':'ll',
            'n':'ls',
            'o':'lll',
            'p':'slls',
            'q':'llsl',
            'r':'sls',
            's':'sss',
            't':'l',
            'u':'ssl',
            'v':'sssl',
            'w':'sll',
            'x':'lssl',
            'y':'lsll',
            'z':'llss',
            '1':'sllll',
            '2':'sslll',
            '3':'sssll',
            '4':'ssssl',
            '5':'sssss',
            '6':'lssss',
            '7':'llsss',
            '8':'lllss',
            '9':'lllls',
            '0':'lllll'
            }


def chirp():
    g.output(pin, 1)

def zzz():
    g.output(pin, 0)



def main():
    try:
        while 1:
            # message list
            message = []
            
            # ask for message
            print('\n\tEnter word for Mores Code Translation')
            tap = input('\t[ctrl- C to exit]\n\n\tMessage >>> ')
            
            
            what_to_tap = list(tap)

            for x in what_to_tap:
                
                tapping = letter[str(x)]

                message.append(tapping)
            
                for ch in message: 
                    for i in ch:
                        if i == 's':
                            chirp()
                            sleep(0.09)
                            zzz()
                            sleep(0.09)
                        
                        elif i == 'l':
                            chirp()
                            sleep(.25)
                            zzz()
                            sleep(0.09)
                        
                        elif i != ' ':
                            chirp()
                            sleep(0.09)
                            zzz()
                            sleep(0.09)
                    
                    # spacebar    
                        else:        
                            zzz()
                            sleep(0.2509)
                message = []    
            

    except KeyboardInterrupt:
        g.cleanup()
        exit()


if __name__ == '__main__':
    main()
    g.cleanup()


