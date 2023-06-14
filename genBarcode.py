import sys
import os
import barcode
from barcode.writer import ImageWriter

stickerSizeIn = [2, 1]
mmPerIn = 25.4
stickerSizeMM = [mmPerIn*dim for dim in stickerSizeIn]
text_distance = 3
stickerPrinterDPI = 203


def makeBarcodeSticker(code):
    code39 = barcode.get_barcode_class('code39')
    options = {
        # 'module_width':stickerSizeMM[0],
        'module_height': stickerSizeMM[1]/2-5,
        'text_distance': text_distance}
    code = code39(code, writer=ImageWriter()).render(options)
    fileName = 'testbarcode.png'
    # code.write('loc',)
    code.save(fileName)

    os.system('lpr {}'.format(fileName))


numArgs = len(sys.argv)
if __name__ == '__main__':
    if (numArgs == 2):
        makeBarcodeSticker(sys.argv[1])
    elif (numArgs > 2):
        for ii in range(numArgs-1):
            makeBarcodeSticker(sys.argv[1+ii])
