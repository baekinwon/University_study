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
q = dataAry[h*w//4]
t = dataAry[h*w*3//4]

for i in range(len(photoAry)):
    if photoAry[i]<=q:
        photoAry[i]=0
    elif photoAry[i] <=midValue:
        photoAry[i]=85
    elif photoAry[i]<=t:
        photoAry[i]=170
    else:
        photoAry[i]=255
        
pos = 0
px = photo.load()
for i in range(h):
    for k in range(w):
        r=g=b=photoAry[pos]
        pos+=1
        px[i,k] = (r,g,b)
    
photo.show()