from waveshare_epd import epd1in54_V2
from PIL import Image

# two functions for cropping images to square
# from: https://note.nkmk.me/en/python-pillow-square-circle-thumbnail/
def crop_center(img, crop_width, crop_height):
    img_width, img_height = img.size
    return img.crop(((img_width - crop_width) // 2,
                     (img_height - crop_height) // 2,
                     (img_width + crop_width) // 2,
                     (img_height + crop_height) // 2))

def crop_max_square(img):
    return crop_center(img, min(img.size), min(img.size))

def setup():
    global epd
    epd = epd1in54_V2.EPD()
    epd.init(0)
    epd.sleep()
    
def display_image(path):
    im = Image.open(path)
    # im.show() # for debugging
    im_cropped = crop_max_square(im)
    # im_cropped.show() # for debugging
    im_resized = im_cropped.resize((200, 200))
    # im_resized.show() # for debugging
    im_bw = im_resized.convert('1')
    # im_bw.show() for debugging
    
    global epd
    epd.init(0)
    epd.display(epd.getbuffer(im_bw))
    epd.sleep()


if __name__ == '__main__':
    setup()
    display_image('temp.jpg')
