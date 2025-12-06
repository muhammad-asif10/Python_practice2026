from PIL import image, ImageFilter

before =image.open("pen.jpg")
after =before.filter(ImageFilter.BoxBlur(5))
after.save("out.jpg")