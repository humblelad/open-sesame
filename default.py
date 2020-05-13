
#!/usr/bin/python3

print('''
   ___                     ___                            
  / _ \  _ __  ___  _ _   / __| ___  ___ __ _  _ __   ___ 
 | (_) || '_ \/ -_)| ' \  \__ \/ -_)(_-</ _` || '  \ / -_)
  \___/ | .__/\___||_||_| |___/\___|/__/\__,_||_|_|_|\___|
        |_| by twitter.com/CircleNinja                                              
            ''')
import load
import refresh

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--custom', action='store_true',
                    help="Shows writeups from custom wordlist. ")

parser.add_argument('--refresh', action='store_true',
                    help="Refresh the h1 writeups.(Try running it once in  5-10 days)")

args = parser.parse_args()

if args.custom:

    load.cute()
    exit()


if args.refresh:
    refresh.refresh()
    exit()



import webbrowser
import csv
import random
with open('final.txt') as f:
    reader = csv.reader(f,delimiter='\n')

    chosen_row = random.choice(list(reader))

    print("Opening the Magic URL \n"+chosen_row[0])
    webbrowser.open(chosen_row[0])



