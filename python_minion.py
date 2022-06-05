def minion_game(string):
    string = string.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    if kevin_score > stuart_score:
        print("Kevin {}".format(kevin_score))
    elif kevin_score < stuart_score:
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)