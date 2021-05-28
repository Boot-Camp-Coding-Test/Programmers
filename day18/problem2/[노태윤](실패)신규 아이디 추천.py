# 6, 18, 26 실패

import re

def solution(new_id):
    text = new_id.lower()
    text = re.sub("[^a-z1-9\.\_\-]+","",text)
    text = re.sub("\.+",".",text)
    text = re.sub("^\.","",text)
    
    if text == '' :
        text+='a'

    if len(text) >= 16 :
        text = text[:15]

    text = re.sub('\.$','',text)

    if len(text) <=2 :
        text = text.ljust(3,text[-1])

    return text
