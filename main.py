from PIL import Image
from PIL import ImageFilter

with Image.open('sobaka.jpg') as pic_original:
    pic_original.show()
    
    pic_gray = pic_original.convert("L")
    pic_gray.save("sobaka1.jpg")
    
    pic_up = pic_gray.transpose(Image.ROTATE_90)
    pic_up.save("sobaka2.jpg")
    
    pic_blur = pic_original.filter(ImageFilter.BLUR)
    pic_blur.save("sobaka3.jpg")
    
    print("Розмір:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Тип:", pic_original.mode)