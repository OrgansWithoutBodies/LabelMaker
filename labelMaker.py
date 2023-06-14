
import sys
from tools import sendLabelToPrinter
from pilLabels import zebraLabel


def makeTestLabel():
    zebraLabel("HELLO\nWORLD").save("test.png")


def printTestLabel():
    sendLabelToPrinter(zebraLabel("HELLO\nWORLD", padding=30))


def printLabelList(txtList, padding, wid, hei):
    for txt in txtList:
        sendLabelToPrinter(zebraLabel(txt, padding, wid, hei))


if __name__ == "__main__":

    try:
        zebraLabel(sys.argv[1], padding=int(sys.argv[2]),
                   tone=int(sys.argv[3])).save("test.png")
    except:
        try:
            zebraLabel(txt=sys.argv[1], padding=int(
                sys.argv[2])).save("test.png")
        except:
            try:
                zebraLabel(sys.argv[1]).save("test.png")
            except:
                raise


"""
TODO
    QR Codes
    Barcodes
        reader
            "Where did i put this" book
    Web Interface
    multiples
    gridModules/lines
"""
