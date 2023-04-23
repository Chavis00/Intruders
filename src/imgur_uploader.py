from pyimgur import Imgur
from config import CLIENT_ID


def upload(PATH):    
    im = Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Chavis333")
    return str(uploaded_image.link)