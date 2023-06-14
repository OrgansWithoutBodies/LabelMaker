from PIL import Image,ImageDraw,ImageFont
import math
numSections=[1,4]
numDivisions=[dim-1 for dim in numSections]
dividerPix=5
pageSizeInch=[
    8.5,
    11,
    ]

pixPerInch=300
img=Image.new("L", [math.floor(dim*pixPerInch) for dim in pageSizeInch],color=255)
labelSize=[2,1]
draw=ImageDraw.Draw(img)
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf", 
    math.floor(20*pixPerInch/50)
    )
textOffset=0.5*pixPerInch
xSectionSize=(img.size[0]-numDivisions[0]*dividerPix)/numSections[0]
ySectionSize=(img.size[1]-numDivisions[1]*dividerPix)/numSections[1]
for ii in range(numDivisions[0]):
    dividerPos=xSectionSize*(ii+1)+(ii+0.5)*dividerPix
    dividerStart=[dividerPos,0]
    dividerEnd=[dividerPos,img.size[1]]
    
    draw.line(dividerStart+dividerEnd, fill=0,width=dividerPix)
    
for jj in range(numSections[1]):
    dividerPos=ySectionSize*(jj+1)+(jj+0.5)*dividerPix
    dividerStart=[0,dividerPos]
    dividerEnd=[img.size[0],dividerPos]
    prevDividerPos=ySectionSize*(jj)+(jj-0.5)*dividerPix

    draw.line(dividerStart+dividerEnd, fill=0,width=dividerPix)
    text='Cubby {}'.format(jj+1)
    textPos=(prevDividerPos+dividerPos)/2-font.getsize(text)[1]/2-textOffset
    draw.text([math.floor(0.1*pixPerInch),textPos], text,font=font)
    
    rectPos=textPos+font.getsize(text)[1]+10
    draw.rectangle([
                    math.floor(0.1*pixPerInch),
                    rectPos,
                    math.floor((0.1+labelSize[0])*pixPerInch),
                    rectPos+math.floor(labelSize[1]*pixPerInch)
                    ],width=dividerPix)
img.show()
