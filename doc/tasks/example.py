#!/usr/bin/python3

from __future__ import print_function
import sys

import random
import hashlib
from os.path import join

"""This is example external checker for Qoala server """

CATEGORY = 'random'
SCORE = 100
NAME = "Example guesser"

TIMEOUT = 120

HTML_EN = ''' Guess the number! It's integer greater than {} and less than {}'''
HTML_RU = ''' Угадай число! Это целое число больше чем {} и меньше чем {}'''

FILE = 'numbers'

# Force utf8 output
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

if len(sys.argv) < 2:
    print("You need to provide at least one argument", file=sys.stderr)
    exit(1)

action = sys.argv[1].lower()


def md5(mess):
    h = hashlib.md5()
    h.update(mess.encode())
    return h.hexdigest()


def crete_task(dump_dir):
    global HTML_EN, HTML_RU
    number = random.randint(0, 100000)
    quid = md5(str(number))
    HTML_EN = HTML_EN.format(number - 1000, number + 1000)
    HTML_RU = HTML_RU.format(number - 1000, number + 1000)

    fname = join(dump_dir, FILE)
    with open(fname, mode='a') as data:
        data.write('{} {}\n'.format(quid, number))

    return quid


def check_task(dump_dir, quid, answer):
    fname = join(dump_dir, FILE)
    with open(fname, mode='r') as data:
        for line in data:
            (quid_x, number) = line.strip().split()[:2]
            if quid == quid_x:
                break
    if quid_x == quid:
        if answer == number:
            print("You got it!")
            return True
        else:
            print("Your number is wrong")
            return False
    else:
        print("Hey! That's bug!")
        return False
    print("Default one")
    return False


if action == 'id':
    print("{}:{}".format(CATEGORY, SCORE))
elif action == 'series':
    print(CATEGORY)
elif action == 'name':
    print(NAME)
elif action == 'create':
    dump_dir = sys.argv[2]
    team_id = sys.argv[3]
    quid = crete_task(dump_dir)
    if quid is None:
        print("Can't create task")
        exit(1)
    else:
        print("ID:" + str(quid))
        print("html[en]:{}".format(HTML_EN))
        print("html[ru]:{}".format(HTML_RU))
        print("timeout:" + str(TIMEOUT))
elif action == 'user':
    dump_dir = sys.argv[2]
    quid = sys.argv[3]
    answer = sys.stdin.readline().strip()
    status = check_task(dump_dir, quid, answer)
    stat = 0 if status else 1
    print("Exiting with " + str(status))
    exit(stat)
else:
    print("No such action: '{}' available actions are: id, series, name, create, user".format(action), file=sys.stderr)
    exit(1)

exit(0)