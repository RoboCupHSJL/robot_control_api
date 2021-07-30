from gcreceiver import ThreadedGameStateReceiver
import msvcrt

import time

""" This is a simple test program for the threaded GC receiver.
Usage instrunctions:
Once ThreadedGameStateReceiver object created, call .start() to start UDP rx/tx
You can acess ThreadedGameStateReceiver.team_state or ThreadedGameStateReceiver.player_state at any time to get fresh data
Don't forget to set proper team and player numbers before start to filter proper data from GC,
and to echo correct keepalive status as an answer (corresponding player icon in GC will switch to green). 
Team number is a worldwide accepted number of the team (from game.json in case of simulation), 
Player number is an number of a player in GC (so starts from 1 for player 1 and so on) 
"""
team = 8
player = 1
is_goalkeeper = True

receiver = ThreadedGameStateReceiver(team, player, is_goalkeeper)    
receiver.start() # Strat receiving and answering

while True:
    if receiver.state != None: # ask for a data any time you want, but don't forget to check for None in case of GC is not preset or any other connection error         
        receive_time = time.ctime(receiver.time)
        print(f'\n----- Whole game state, received at {receive_time}:')
        print(receiver.state)
        print(f'\n----- Whole team state, received at {receive_time}:')
        print(receiver.team_state)
        print(f'\n----- This player state, received at {receive_time}:')
        print(receiver.player_state)
    else:
        print('None')
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        if ch == b'e':
            print('Calling stop()')
            receiver.stop()
        if ch == b'b':
            print('Calling start()')
            receiver.start()
    time.sleep(1)