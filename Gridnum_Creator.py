def main(gridnum):

    startx = 295
    starty = 3735

    def addxFunc(startx):
        # add part to write startx to database
        # startx.addtocsv
        currentx = startx
        xlist = [startx]
        addTwo = True
        k = 0
        while k < 38:
            if addTwo == True:
                currentx += 2
                xlist.append(currentx)
                addTwo = False
                k += 1
            else:
                currentx += 1
                xlist.append(currentx)
                addTwo = True
                k += 1
        return xlist

    def addyFunc(starty):
        # add part to write startx to database
        # startx.addtocsv
        ylist = [starty]
        currenty = starty
        k = 0
        while k < 49:
            currenty += 15
            ylist.append(currenty)
            k += 1
        #ylist = ylist.reverse()
        return ylist
            
    def cellcreator(Gridnum):
        xlist = addxFunc(startx)
        ylist = addyFunc(starty)
        # print(xlist)
        # print(ylist)
        # takes apart Character and number
        ynum = ord(Gridnum[0])-65
        xnum = Gridnum[1:]
        xnum = int(xnum)-1


        x = (xnum*3)-1
        y = -ynum*3
        cell = str(xlist[(x)]) + str(ylist[y])

        gridlist = []

        xnew = x
        ynew = y
        i = 0
        l = 0
        while i < 3:
            while l < 3:
                xnew +=1
                cell = str(xlist[(xnew)]) + str(ylist[ynew])
                l +=1
                TorU = 'U'
                if xlist[(xnum*3)] < 300:
                    TorU = 'T'
                PorQ ='Q'
                if ylist[-ynum*3] < 4000:
                    PorQ = 'P'
                LiDARfile = "usgs16-70cm_15R" + TorU + PorQ + cell + ".laz"
                LiDARfile = str(LiDARfile)
                gridlist.append(LiDARfile)
            i +=1
            l = 0
            xnew = x
            ynew -= 1
        # print(gridlist)
        return gridlist




        # TorU = 'U'
        # if xlist[(xnum*3)] < 300:
        #     TorU = 'T'
        # PorQ ='Q'
        # if ylist[-ynum*3] < 4000:
        #     PorQ = 'P'
        # LiDARfile = "usgs16-70cm_15R" + TorU + PorQ + leftmost + ".laz"
        # print(LiDARfile)


    return cellcreator(gridnum)

    

if __name__ == '__main__':
    main(gridnum)