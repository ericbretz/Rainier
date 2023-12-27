import random

def logoprint():
    colors = {
        'red': '\033[0;31m',
        'green': '\033[0;32m',
        'yellow': '\033[0;33m',
        'blue': '\033[0;34m',
        'purple': '\033[0;35m',
        'cyan': '\033[0;36m'
    }
    A = colors[random.choice(list(colors.keys()))]
    B = colors[random.choice(list(colors.keys()))]
    C = colors[random.choice(list(colors.keys()))]
    D = [A, B]
    W = f'\033[0;37m'

    rainier_logo =  f'''
{W} {random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W}   /{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W}  /{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W} /{random.choice(D)}█{random.choice(D)}█{W}   /{random.choice(D)}█{random.choice(D)}█{W} /{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W} /{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W} /{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W} 
 █{random.choice(D)}█{random.choice(D)}█{W}████{random.choice(D)}█{random.choice(D)}█{W} /{random.choice(D)}█{random.choice(D)}█{W}██  {random.choice(D)}█{random.choice(D)}█{W}|█  {random.choice(D)}█{random.choice(D)}█{W}█/| {random.choice(D)}█{random.choice(D)}█{random.choice(D)}█ {W}| {random.choice(D)}█{random.choice(D)}█{W}|█  {random.choice(D)}█{random.choice(D)}█{W}█/| {random.choice(D)}█{random.choice(D)}█{W}█████/| {random.choice(D)}█{random.choice(D)}█{W}██  {random.choice(D)}█{random.choice(D)}█{W}
 █{random.choice(D)}█{random.choice(D)}█  {W}\█{random.choice(D)}█{random.choice(D)}█{W}| {random.choice(D)}█{random.choice(D)}█{W}  \ {random.choice(D)}█{random.choice(D)}█{W}  | {random.choice(D)}█{random.choice(D)}█{W}  | {random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W}| {random.choice(D)}█{random.choice(D)}█{W}  | {random.choice(D)}█{random.choice(D)}█{W}  | {random.choice(D)}█{random.choice(D)}█{W}      | {random.choice(D)}█{random.choice(D)}█{W}  \ {random.choice(D)}█{random.choice(D)}█{W}
 █{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W}/| {random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W}  | {random.choice(D)}█{random.choice(D)}█{W}  | {random.choice(D)}█{random.choice(D)}█{W} {random.choice(D)}█{random.choice(D)}█{W} {random.choice(D)}█{random.choice(D)}█{W}  | {random.choice(D)}█{random.choice(D)}█{W}  | {random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W}   | {random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{random.choice(D)}█{W}/
 █{random.choice(D)}▓{random.choice(D)}▓{W}████{random.choice(D)}▓{random.choice(D)}▓{W}| {random.choice(D)}▓{random.choice(D)}▓{W}██  {random.choice(D)}▓{random.choice(D)}▓{W}  | {random.choice(D)}▓{random.choice(D)}▓{W}  | {random.choice(D)}▓{random.choice(D)}▓{W}  {random.choice(D)}▓{random.choice(D)}▓{random.choice(D)}▓{random.choice(D)}▓{W}  | {random.choice(D)}▓{random.choice(D)}▓{W}  | {random.choice(D)}▓{random.choice(D)}▓{W}██/   | {random.choice(D)}▓{random.choice(D)}▓{W}██  {random.choice(D)}▓{random.choice(D)}▓{W}
 █{random.choice(D)}▒{random.choice(D)}▒{W}  \█{random.choice(D)}▒{random.choice(D)}▒{W}| {random.choice(D)}▒{random.choice(D)}▒{W}  | {random.choice(D)}▒{random.choice(D)}▒{W}  | {random.choice(D)}▒{random.choice(D)}▒{W}  | {random.choice(D)}▒{random.choice(D)}▒{W}\  {random.choice(D)}▒{random.choice(D)}▒{random.choice(D)}▒{W}  | {random.choice(D)}▒{random.choice(D)}▒{W}  | {random.choice(D)}▒{random.choice(D)}▒{W}      | {random.choice(D)}▒{random.choice(D)}▒{W}  \ {random.choice(D)}▒{random.choice(D)}▒{W}
 █{random.choice(D)}░{random.choice(D)}░{W}   █{random.choice(D)}░{random.choice(D)}░{W}| {random.choice(D)}░{random.choice(D)}░{W}  | {random.choice(D)}░{random.choice(D)}░{W} /{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{W}| {random.choice(D)}░{random.choice(D)}░{W} \  {random.choice(D)}░{random.choice(D)}░{W} /{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{W}| {random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{random.choice(D)}░{W}| {random.choice(D)}░{random.choice(D)}░{W}  | {random.choice(D)}░{random.choice(D)}░{W}
 ██/   ██/  ██/ ██/██████/██/  \██/██████/████████/██/  ██/
'''


    print(rainier_logo)

logoprint()