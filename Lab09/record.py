#! /user/local/bin/python3.4

from institute import *

def loadHistory(fileName):
    ins = Institute()
    with open(fileName, 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines[3:]:
            split_line = line.split("|")
            name = split_line[0].strip()
            split_name = name.split()
            namefirst = split_name[0]
            namelast = split_name[1]
            account = split_line[1].strip()
            trans = split_line[2].strip()
            if account not in ins.accounts:
                ins.createNew(namefirst, namelast, account)

def getTotalBy(institute, client):
    summ = 0
    for account in institute.accounts:
        if account.client is client:
           summ = summ + account.amount
    summ = round(summ, 2)
    return summ

def getLendingPower(institute):
    perfect = {}
    for account in institute.accounts:
        if str(account.client) not in perfect:
            perfect[str(account.client)] = getTotalBy(institute, account.client)
        else:
            pass

