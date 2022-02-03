import argparse

def calculate(lines):
    l = [{},{},{},{},{}]
    for i in lines:
        for j in range(5):
            if i[j] in l[j]:
                l[j][i[j]] += 1
            else:
                l[j][i[j]] = 1
    d = {}
    for i in lines:
        d[i] = 0
        for j in range(5):
            d[i] += l[j][i[j]]
    a = max(d, key=d.get)
    xd = list({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})
    xd = xd[-9:]
    for i in xd:
        print(i)
    print("------------------")
    print(a)
    print("Type !q to quit")
    return a

def cheat(lines, a, word):
    lines.remove(a)
    l2 = {}
    for i in word:
        if i.isalpha() and i.isupper():
            if i.lower() in l2:
                l2[i.lower()] += 1
            else:
                l2[i.lower()] = 1
    l3 = set()
    l4 = []
    for i in a:
        if i not in l2 and i in word:
            l4.append(i)
        if i not in l2 and i not in word:
            l3.add(i)
    for i in range(5):
        del_list = set()
        for j in lines:
            if word[i] != j[i] and word[i] != "_" and word[i].islower():
                del_list.add(j)
            elif word[i].isupper() and word[i].lower() == j[i]:
                del_list.add(j)
        for i in del_list:
            lines.remove(i)

    del_list = set()
    for j in lines:
        for n in l2:
            if word.count(n) + l2[n] > j.count(n):
                del_list.add(j)
        for n in l3:
            if n in j:
                del_list.add(j)
        for n in l4:
            if word.count(n) > j.count(n):
                del_list.add(j)
    for i in del_list:
        lines.remove(i)

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True)
    args = parser.parse_args()
    f = open(args.input, 'r')

    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    lines = set(lines)
    copy = lines.copy()

    while True:
        a = calculate(lines)
        for i in range(6,0,-1):
            word = input(f'{i}: ')
            if word == "":
                lines = copy.copy()
                break
            elif word == "!q":
                exit(0)
            try:
                cheat(lines, a, word)
                print(len(lines))
                a = calculate(lines)
            except:
                lines = copy.copy()
                break

if __name__ == '__main__':
    main()
