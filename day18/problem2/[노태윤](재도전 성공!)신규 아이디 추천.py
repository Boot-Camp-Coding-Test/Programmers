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

# ===============================================
# 재도전

import re

def solution(new_id):
    text = new_id.lower() # 1단계 -- 소문자로 변환
    text = re.sub("[^a-z0-9\.\_\-]+","",text) # 2단계 -- 소문자, 숫자, '-' , '_', '.' 를 제외하고 나머지 문자 제거
    text = re.sub("\.+",".",text) # 3단계 -- '.' 반복으로 나오는 것 하나로 만들기
    text = re.sub("^\.|\.$","",text) # 4단계 -- 맨 앞 또는 맨 뒤에 '.' 있으면 제거하기
    
    if text == '' : # 5단계 -- 빈 문자열이면 'a' 로 추가하기
        text='a'

    if len(text) >= 16 : # 6단계 -- 16자 이상면 처음 15개만 추출
        text = text[:15]

    text = re.sub('\.$','',text) # 이 때 마지막이 '.' 이면 제거하기

    if len(text) <=2 : # 7단계 -- 총 길이가 2 이하이면 이 때 마지막 문자를 총 길이가 3 이 될 때까지 뒤에 추가하기
        text = text.ljust(3,text[-1])

    return text

# Key points
    # 2단계에서 실수 함
        text = re.sub("[^a-z1-9\.\_\-]+","",text) # ==> 숫자 1 부터 9 를 제외하고 나머지 다 제거하게끔 코딩함 ==> 0 은 제거됨...
        
         text = re.sub("[^a-z0-9\.\_\-]+","",text) # ==> 이렇게 해야함
