from thispersondoesnotexist import get_online_person
import cv2 
import numpy as np
import asyncio as a

loop=a.get_event_loop()
def facegen():
    img= loop.run_until_complete(get_online_person())#.close()

    imgar=np.array(bytearray(img),dtype=np.uint8)
    img=cv2.imdecode(imgar,1)
    cv2.imshow('image',img)
    cv2.waitKey(0)

facegen()
loop.close()
