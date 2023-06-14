from io import BytesIO
import subprocess
from typing import Tuple
from PIL import Image, ImageFont


def getMaximumFontSize(txt: str, size: Tuple[int, int], padding: int):
    fontTooSmall = True
    fontSize = 1

    unpaddedDims = (size[0]-padding, size[1]-padding)
    while (fontTooSmall):

        font = ImageFont.truetype(
            '/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', fontSize)
        txtSize = font.getsize_multiline(txt)

        fontTooSmall = (unpaddedDims[0] > txtSize[0]) & (
            unpaddedDims[1] > txtSize[1])

        # TODO better stepper
        fontSize = fontSize+1
    return fontSize


def drawTextInMiddle(drawer, txt, fontSize, tone, xMid, yMid, pos=[0, 0]):
    fnt = ImageFont.truetype(
        '/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', fontSize)

    txtSize = fnt.getsize_multiline(txt)
    drawer.text((pos[0]+xMid-txtSize[0]/2, pos[1]+yMid - txtSize[1]/2),
                txt, fill=tone, font=fnt)


def drawTextAtMaxInMiddle(drawer, txt, padding, tone, wid, hei, pos=[0, 0]):
    fontSize = getMaximumFontSize(txt, (wid, hei), padding)
    drawTextInMiddle(drawer, txt, fontSize, tone, wid/2, hei/2, pos)


def sendLabelToPrinter(label: Image):
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)

    byte_io = BytesIO()

    label.save(byte_io, 'PNG')

    lpr.stdin.write(byte_io.getvalue())
    lpr.stdin.close()
# class VDrawer extends ImageDraw
