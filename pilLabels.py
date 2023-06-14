
from PIL import Image, ImageDraw
from consts import dpi
from tools import getMaximumFontSize, drawTextAtMaxInMiddle


def zebraLabel(txt: str, padding: int = 0, wid: int = 2*dpi, hei: int = 1*dpi, tone: int = 0,) -> Image:
    img = Image.new('L', (wid, hei), 'white')
    draw = ImageDraw.Draw(img)
    fontSize = getMaximumFontSize(txt, (wid, hei), padding)
    minFontSize = 20
    txtArray = txt.split('\\n')
    nTexts = len(txtArray)
    if (fontSize < minFontSize):
        brknTxt = txt.replace(' ', '\n')
        drawTextAtMaxInMiddle(draw, brknTxt, padding, tone, wid, hei)
    else:
        for tt in range(nTexts):
            print(tt)
            drawTextAtMaxInMiddle(draw, txtArray[tt], padding, tone, wid, round(
                hei/nTexts), pos=[0, round(hei/nTexts*tt)])

    return img
