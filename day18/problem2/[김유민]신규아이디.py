def solution(new_id):
    new_id = new_id.lower()
    puncs = '~!@#$%^&*()=+[{]}:?,<>/'
    mytable = str.maketrans('', '', '~!@#$%^&*()=+[{]}:?,<>/') # (바뀔문자(from), 바뀔문자(to), 삭제할 문자)
    new_id = new_id.translate(mytable)

    new_id = new_id.split('.')
    while 1 :
        try : 
            new_id.remove('')
        except :
            break

    new_id = '.'.join(new_id)

    if new_id == '' :
        new_id = 'aaa'
    
    if len(new_id) > 15 :
        new_id = list(new_id)[:15]
        new_id = ''.join(new_id)

    new_id = new_id.strip('.')

    while len(new_id) < 3 :
        new_id = list(new_id)
        new_id.append(new_id[-1])
        new_id = ''.join(new_id)

    return new_id
