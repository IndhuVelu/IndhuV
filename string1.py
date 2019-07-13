MAX_CHARS = 100002
def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)
    if m != n:
        return False
    marked = [False] * MAX_CHARS
    map = [-1] * MAX_CHARS
    for i in range(n):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                return False
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            return False
    return True

word1,word2=input().split(" ")
if areIsomorphic(word1,word2):
    print("yes")
else:
    print("no")

