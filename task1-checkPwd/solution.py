def check(pwd,word):
    i=0
    while i<len(pwd):
        j=0
        while j<len(word):
            if pwd[i]==word[j]:
                return True
            j=j+1
        i=i+1
    return False
def solution(pwd):
    # your solution here
    arr=['abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ','0123456789']

    if len(pwd)<10:
        return False 
    t=0
    while t<3:
        if check(pwd,arr[t])==False:
            return False
        t=t+1
    return True
