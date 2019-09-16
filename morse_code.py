#!/usr/bin/env python3
# by Jason Lohrey

## Mores code translator. Takes a audio device hooked to gpio pin of raspberrypi
## and allowes user to enter in letters / numbers / words and outputs an audio
## mores code translation


from time import sleep
from RPi import GPIO as g


g.setmode(g.BCM)
g.setwarnings(False)

## used 26 as its next to a grd pin making wiring easy
pin = 26
g.setup(pin,g.OUT)

## mores code dict, s - short ; l - long.
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

## make sound
def chirp():
    g.output(pin, 1)

## quit sound
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
            tap = tap.lower()

            # change message into a list
            what_to_tap = list(tap)

            for x in what_to_tap:
                # look up value for key of letter in message
                try:
                    tapping = letter[str(x)]
                
                # catch punctuation use errors
                except KeyError:
                    print('\tOOPs... no punctuation allowed') #yet
                    tapping = ' '

                # create a list of each lettres m_code value
                message.append(tapping)
                
                # play each character in message
                for character in message: 
                    for letters in character:
                        if letters == 's':
                            chirp()
                            sleep(0.09)
                            zzz()
                            sleep(0.09)
                        
                        elif letters == 'l':
                            chirp()
                            sleep(.25)
                            zzz()
                            sleep(0.09)
                        
                        elif letters != ' ':
                            chirp()
                            sleep(0.09)
                            zzz()
                            sleep(0.09)
                    
                        # spacebar    
                        else:        
                            zzz()
                            sleep(0.2509)

                # empty the list for next message to be added in main loop 
                message = []    
            
    
    except KeyboardInterrupt:
        # always clean up after yourself
        g.cleanup()
        exit()


if __name__ == '__main__':
    main()
    # cleanup if code breaks for some ODD reason (like not a num/letter)
    g.cleanup()


