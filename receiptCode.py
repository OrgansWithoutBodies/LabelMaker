#!/usr/bin/env python3

import sys
from escpos.printer import Usb
import qrcode
import math
from PIL import Image, ImageDraw, ImageFont

pageSizeInch = [1, 2]
pixPerInch = 384


def findMaxFontSizeToFit(string, fontPath, fitSize, minimumFontSize):
    tryingSize = minimumFontSize
    trying = True
    while trying:
        font = ImageFont.truetype(fontPath,
                                  tryingSize
                                  )
        textSize = font.getsize(string)
        if textSize[0] >= fitSize[0] or textSize[1] >= fitSize[1]:
            trying = False
        tryingSize += 1
    return tryingSize


def groceryListImage(groceries,titleText="GROCERIES"):
    titleFontPath = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
    lineSpacing = 0.3*pixPerInch
    listSizePix = [math.floor(1*pixPerInch),
                   math.floor((len(groceries)+2)*lineSpacing)]
    img = Image.new("L", listSizePix, color=255)
    draw = ImageDraw.Draw(img)

    titleFont = ImageFont.truetype(titleFontPath,
                                   math.floor(8*pixPerInch/50)
                                   )
    sqrFont = ImageFont.truetype(
        titleFontPath,
        math.floor(10*pixPerInch/50)
    )
    lineSize = 0.5*pixPerInch
    headerSize = titleFont.getsize(titleText)
    draw.text([img.size[0]/2-headerSize[0]/2, headerSize[1]/2],
              titleText, font=titleFont)
    for ii in range(len(groceries)):
        listBullet = u"\u25A2"

        line = groceries[ii]
        lineFontSize = findMaxFontSizeToFit(
            line,
            titleFontPath,
            [0.6*dim for dim in listSizePix],
            1
        )

        lineFont = ImageFont.truetype(
            titleFontPath,
            lineFontSize
        )
        linePos = (ii+1)*lineSpacing
        draw.text(
            [10, linePos],
            listBullet,
            font=sqrFont
        )
        lineFont.getsize(line)[1]
        bulletSize = sqrFont.getsize(listBullet)
        lineTextSize = lineFont.getsize(line)
        draw.line([math.floor(0.1*listSizePix[0]), linePos,
                  math.floor(0.9*listSizePix[0]), linePos])
        draw.text(
            [10+1.5*bulletSize[0],
             linePos-lineTextSize[1]/2+bulletSize[1]/2],
            line, font=lineFont)
    img.save('testGroceryList.png')
# TODO multiple stores


def printGroceryList(groceries,titleText="GROCERIES"):
    # 0x416 and 0x5011 are the details we extracted from lsusb
    # 0x81 and 0x03 are the bEndpointAddress for input and output

    p = Usb(0x416, 0x5011, in_ep=0x81, out_ep=0x03, profile="POS-5890")

    # Create a QR code
    # qr = qrcode.make('https://arnon.dk')
    # qr.save('qrcode.png')
    # Print the image
    # p.text('HI MOM')
    groceryListImage([line.capitalize() for line in groceries],titleText)
    p.image('testGroceryList.png', fragment_height=500)
    p.close()
    # p.beep()


# printGroceryList(['test1', 'test2', 'test3'])
# groceryListImage(['test', 'test123', 'test213231'])
numArgs = len(sys.argv)
if __name__ == '__main__':
    if (numArgs > 1):
        printGroceryList(sys.argv[1:len(sys.argv)])
    else:
        print("Need Arguments")
