def solution(s):
    if not(len(s) == 4 or len(s) == 6):
        return False
    
    if not(s.isdigit()):
        return False
    return True