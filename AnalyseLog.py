#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def read_log(file):
        log = open(file, encoding='utf-8')

        ftext = ''
        for line in log:
            ftext += line
        log.close()
        return ftext

def empty(obj):
    return obj is None or len(obj) == 0

def findInText(regex, text, linesConf):
    '''
       return a list of maps, each map is a match to multilines,
              in a map, key is the line keyword
                         and value is the content corresponding to the key
    '''
    matched = regex.findall(text)
    if empty(matched):
        return []

    allMatched = []

    return allMatched



if __name__ == '__main__':
    linesConf=[['start:', 'action:'], ['finished:', 'action:']]
    text = read_log("case_log.txt")

    # compiledPattern = re.search(r'\d\d/\d\d\s(\d\d:\d\d:\d\d,\d\d\d).*ACTION\s(\w+)\s\[started\].*\d\d/\d\d\s(\d\d:\d\d:\d\d,\d\d\d).*ACTION\s(\w+)\s\[finished\].*', text, flags=re.DOTALL + re.MULTILINE)
    # print(compiledPattern.groups())
    compiledPattern = re.search(
        r'\d\d/\d\d\s(\d\d:\d\d:\d\d,\d\d\d).*ACTION\s(\w+)\s\[started\].*\d\d/\d\d\s(\d\d:\d\d:\d\d,\d\d\d).*ACTION\s(\w+)\s\[finished\].*',
        flags=re.DOTALL + re.MULTILINE)
    allMatched = findInText(compiledPattern, text, linesConf)