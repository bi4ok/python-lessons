from PIL import Image, ImageDraw, ImageColor
import os


def restyle(ras1, ras2, path=os.getcwd()):
    for files in os.listdir(str(path)):
        if len(files.split('.')) > 1:
            if files.split('.')[1] == ras1:
                x = Image.open(files)
                draw = ImageDraw.Draw(x)
                l = x.size
                draw.rectangle([l[0]/2-30, l[1]/2-30, l[0]/2+30, l[1]/2+30])
                draw.multiline_text((l[0]/2-15, l[1]/2-15), 'Hello,\nWorld!')
                if x.mode == 'RGBA':
                    x = x.convert("RGB")
                x.save(files.split('.')[0] + '.' + ras2)
                del draw


restyle('png', 'jpg')