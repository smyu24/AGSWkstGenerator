def seedgem(reqeust):
    farr = []
    i = 0
    x = 0
    auto = 0
    numsec = 0
    go = True
    for key in reqeust.keys():
        if(key[:4] == "auto"):
            farr.append(int(0))
            farr.append(int(0))
            auto = 3
        
        if(auto == 0):
            for value in reqeust.getlist(key):
                if(key[:5] == "level"):
                    numsec += 1
                farr.append(int(value))
                i += 1
                x += 1
                if(x == 4):
                    if(farr[i-2] >= farr[i-1]):
                        return False
                    x = 0
        else:
            auto -= 1
            x = 0
            continue
    farr.insert(0, numsec)
    if(go == False):
        return False
    else:
        return farr