from PIL import Image

image = Image.open('pet02.gif')
photo= image.convert('RGB')

photoAry = []
h = photo.height
w = photo.width
for i in range(h):
    for k in range(w):
        r,g,b = photo.getpixel((i,k))
        value = (r+g+b)//3
        photoAry.append(value)

dataAry = photoAry[:]
dataAry.sort()
midValue = dataAry[h*w//2]
q1 = dataAry[h*w//8]
q2 = dataAry[h*w*2//8]
q3 = dataAry[h*w*3//8]
q4 = dataAry[h*w*5//8]
q5 = dataAry[h*w*3//4]
q6 = dataAry[h*w*7//8]

for i in range(len(photoAry)):
    if photoAry[i]<=q1:
        photoAry[i]=0
    elif photoAry[i]<=q2:
        photoAry[i]=255//7 
    elif photoAry[i]<=q3:
        photoAry[i]=255//7 *2
    elif photoAry[i]<=midValue:
        photoAry[i]=255//7 *3
    elif photoAry[i]<=q4:
        photoAry[i]=255//7 *4
    elif photoAry[i]<=q5:
        photoAry[i]=255//7 *5
    elif photoAry[i]<=q6:
        photoAry[i]=255//7 *6
    else:
        photoAry[i] = 255
        
pos = 0
px = photo.load()
for i in range(h):
    for k in range(w):
        r=g=b=photoAry[pos]
        pos+=1
        px[i,k] = (r,g,b)
    
photo.show()