from thispersondoesnotexist import get_online_person
from  PIL import Image
import asyncio as a
import io
import base64

a.set_event_loop_policy(a.WindowsSelectorEventLoopPolicy())#get_event_loop()
loop=a.new_event_loop()

def Make_new_Face():
    bytedata = loop.run_until_complete(get_online_person())

    img=Image.open(io.BytesIO(bytedata))
    return img.show()
# def facegen():
#     img= loop.run_until_complete(get_online_person())#.close()

#     img=Image.frombytes(img)
#     img=Image.imshow(img)
    

# facegen()
loop.close()
