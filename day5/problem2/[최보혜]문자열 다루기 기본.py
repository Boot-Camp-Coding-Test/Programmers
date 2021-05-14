import re
def solution(s):
    check = re.search('[^0-9]', s)
    if (len(s)==4 or len(s)==6) and check == None:
        return True
    return False
