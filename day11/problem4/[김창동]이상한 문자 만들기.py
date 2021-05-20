def solution(s):
    result = ''
    for word in s.split(' '):
        for i, v in enumerate(word):
            if i % 2:
                result += v.lower()
            else:
                result += v.upper()
        
        result += ' '
    return result[:-1]
