
def solution(text: str) -> str:
    # your solution here
    word=['abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    help=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    i=0
    while i<len(str):
        j=0
        while j<len(word[0]):
            if str[i]==word[0][j] or str[j]==word[1][j]:
                help[j]=help[j]+1
            j=j+1
        i=i+1
    print(word[0][searchIndex(help)])
    return word[0][searchIndex(help)]

def searchIndex(help):
    index=0;
    temp=0
    t=0
    while t<len(help):
        if help[t]>temp:
            temp=help[t]
            index=t
        t=t+1
    return index

