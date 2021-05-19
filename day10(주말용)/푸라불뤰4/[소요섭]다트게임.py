import re

def solution(dartResult):
    sdt = {'S':1,'D':2,'T':3}
    option = {'*':2,'#':-1}
    match_regex = re.compile('[0-9]{1,2}[SDT]{0,1}[*#]{0,1}').finditer(dartResult)
    points = []
    for n,i in enumerate(match_regex):
        point = re.compile('[0-9]{1,2}').findall(i.group())
        squrt = re.compile('[SDT]').findall(i.group())
        opt = re.compile('[*#]').findall(i.group())
        
        if len(opt)>0:
            op = option[opt[0]]
        else : op=1
        points.append(  ( int(point[0])**int(sdt[squrt[0]]) ) * op )
        if n > 0 and len(opt)>0 and opt[0] == '*':
            points[n-1] = points[n-1] * 2

    answer = sum(points)
    return answer
