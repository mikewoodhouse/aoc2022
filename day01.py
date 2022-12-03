with open("input01.txt") as f:
    total = 0
    itm = 0
    highest = [0, 0, 0]
    while True:
        s = f.readline()
        if not s:
            break
        s = s.strip()
        cals = int(s) if s else 0
        if cals > 0:
            total += cals
        else:
            itm += 1
            print(itm, total)
            if total > highest[0]:
                highest[0] = total
                print(highest)
                highest.sort()
                print(itm, highest, total)
            total = 0
        # print(s, cals, total, highest)
    if total > highest[0]:
        highest = sorted(highest + [total])[1:]
    print(highest, sum(highest))
