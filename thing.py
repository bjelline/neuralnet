import cv2

def loadImage(path):
    im = cv2.imread(path)
    return flatten(im)

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


things = [loadImage('pic/image_1copy.png'),loadImage('pic/image_2copy.png'),
loadImage('pic/image_3copy.png'),loadImage('pic/face_2copy.png'),loadImage('pic/face_3copy.png')]

for thing in things:
    print len(thing)
   
