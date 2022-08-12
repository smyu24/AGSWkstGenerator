def reseed(seed, code):
    twoDarr = []
    oneDarr = []
    j=0
    for i in range(len(seed)):
        oneDarr.append(seed[i])
        if(len(oneDarr) == 5):
            twoDarr.append(oneDarr)
            twoDarr[j][0] = str(code) + "-" + str(twoDarr[j][0])
            j += 1
            oneDarr = []

    return twoDarr

def seedgem(reqeust, code):
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

                if "." in value:
                    farr.append(float(value))
                else:
                    farr.append(int(value))
                i += 1
                x += 1
                if(x == 5):
                    if(farr[i-2] >= farr[i-1]):
                        return False
                    x = 0
        else:
            auto -= 1
            x = 0
            continue
    if(go == False):
        return False
    else:
        return numsec, reseed(farr, code)
