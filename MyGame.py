
import random
import time

def time_3():
    i = 0
    while i < 3:
        time.sleep(0.9)
        print('.', end='')
        i = i + 1


print('The world is in chaos, and only you can save it', end='')
time_3()
print()

print('Mayor: Welcome, dear knight. Before I explain, would you mind letting me know your name?')
print('Your name: ', end='')
playerName = input()
time.sleep(0.8)
print('Mayor: Knight ' + playerName + ', few days ago, there has been a war between gods. As the result of the war, there is lots of remaining monsters still. ')
time.sleep(1.5)
print('Mayor: Please kill the monster that is in the church.')
time.sleep(1.5)
print('Knight ' + playerName + ': It would be my honor.')
time.sleep(1.5)
print('Mayor: Oh, thank you so much, knight. I will for sure compensate for your help.')
print()
time.sleep(1.5)
print('Your mission: Eliminate the lizard man in church.')
print()
time.sleep(1)
print('Walking to church', end='')
time_3()
print()
time.sleep(1.5)
print('                  _|_')
print('                   |')
print('                  / \\')
print('                 //_\\\\')
print('                //(_)\\\\')
print('                 |/^\| ')
print('       ,%%%%     // \\\\    ,@@@@@@@,')
print('     ,%%%%/%%%  //   \\\\ ,@@@\@@@@/@@,')
print(' @@@%%%\%%//%%%// === \\\\ @@\@@@/@@@@@')
print('@@@@%%%%\%%%%%// =-=-= \\\\@@@@\@@@@@@;%#####,')
print('@@@@%%%\%%/%%//   ===   \\\\@@@@@@/@@@%%%######,')
print('@@@@@%%%%/%%//|         |\\\\@\\\\//@@%%%%%%#/####')
print('\'@@@@@%%\\\\/%~ |         | ~ @|| %\\\\//%%%#####;')
print('  @@\\\\//@||   |  __ __  |    || %%||%%\'######')
print('   \'@||  ||   | |  |  | |    ||   ||##\//####')
print('     ||  ||   | | -|- | |    ||   ||\'#||###\'')
print('     ||  ||   |_|__|__|_|    ||   ||  ||')
print('     ||  ||_/`  =======  `\__||_._||  ||')
print('   __||_/`      =======            `\_||___')


