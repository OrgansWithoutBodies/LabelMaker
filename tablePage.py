import math
from typing import List
from PIL import Image, ImageDraw

from tools import drawTextAtMaxInMiddle

dpi = 203

pageWid = int(20.5*dpi)
pageHei = int(11*dpi)

labWid = int(1*dpi)
labHei = int(.5*dpi)


def dashedLine(pos: List[int], drawer, dashLen, spaceLen):
    x0, y0 = pos[0], pos[1]
    x1, y1 = pos[2], pos[3]
    dashSize = dashLen+spaceLen
    diffX, diffY = x1-x0, y1-y0
    lenDiff = math.sqrt(diffX**2+diffY**2)
    numDashes = int(lenDiff / dashSize)
    for ii in range(numDashes+1):
        perc = (ii*dashSize)/lenDiff
        percDash = (ii*dashSize+dashLen)/lenDiff
        startX, startY = x0+diffX*perc, y0+diffY*perc
        endX, endY = min(x0+diffX*percDash, x1), min(y0+diffY*percDash, y1)

        drawer.line([
            (startX, startY),
            (endX, endY)],
        )


def crossedCell(draw, wid, hei, posX, posY):
    draw.rectangle([(posX, posY), (posX+wid, posY+hei)])
    dashLen = 10
    spaceLen = 5

    dashedLine([posX+1/2*wid, posY, posX+1/2 * wid, posY+hei],
               draw,   dashLen, spaceLen)
    dashedLine([posX, posY+1/2*hei,  posX+wid, posY+1/2*hei],
               draw,   dashLen, spaceLen)

# TODO decrease text col wid


def tableCell(draw, txt, rowWid, rowHei, posX, posY, nCols):
    draw.rectangle([(posX, posY), (rowWid/nCols, rowHei)])
    cellWid = int(rowWid/nCols)
    drawTextAtMaxInMiddle(draw, txt, 10, 0, rowWid/nCols, rowHei, [posX, posY])
    for nn in range(nCols-1):
        crossedCell(draw, cellWid, rowHei,
                    int(posX+(nn+1)*rowWid/nCols), posY)


def tablePage():
    rowWid = labWid*4
    rowHei = labHei
    img = Image.new('L', (int(pageWid), pageHei), 'white')
    draw = ImageDraw.Draw(img)
    nRows = math.floor(pageHei/rowHei)
    nCols = math.floor(pageWid/rowWid)
    print(pageWid, rowWid, nCols, pageHei, rowHei, nRows)

    for n in range(nRows):
        print(n)
        tableCell(draw, str(n+1), rowWid, rowHei, 0, rowHei*n, nCols)
    img.show()
