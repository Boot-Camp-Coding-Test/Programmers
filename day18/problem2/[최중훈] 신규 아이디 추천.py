import re

def solution(new_id):
    # 1. to lowercase
    id = new_id.lower() 

    # 2. remove character not allowed
    id = re.sub('[^a-z0-9\-\_\.]', '', id)

    # 3. two more dot remove 
    id = re.sub('(\.)+', '.', id) 

    # 4. remove dot on the first and last
    id = id.strip('.') 
    
    # 5. check if id is None or not
    if not id: 
        id = 'a'

    # 6. cut to 15th characters
    id = id[:15] 
    id = id.rstrip('.')
    
    # 7. check if length > 2
    while len(id) <= 2:
        id = id + id[-1]

    return id
