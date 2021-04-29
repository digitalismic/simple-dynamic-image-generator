import sys
import uuid
from PIL import Image, ImageDraw
 
path = './images/'
char = sys.argv[-1]    
randomid = uuid.uuid4().hex
prefix = randomid[0:8]+'-'
img = Image.new('RGB', (100, 30), color = (73, 109, 137))
d = ImageDraw.Draw(img)

d.text((10,10), char+"", fill=(255,255,0))
img.save((path)+(prefix)+(char)+'.png')
