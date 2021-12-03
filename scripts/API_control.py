from os import walk, remove
from scripts.faceAPI import detect
from scripts.imgur_uploader import upload
from scripts.telegram_bot import send_intruder
from config import OUTPUTPATH, FKEY, ENDPOINT, TOKEN,  CHAT_ID, CLIENT_ID

 
def api_controller():
    path = OUTPUTPATH
    while True:

        if "" in [FKEY, ENDPOINT, ENDPOINT, TOKEN, CHAT_ID, CLIENT_ID]:
            print("\n\nNo keys provided\n\n")
            break

        f = []
        for (dirpath, dirnames, filenames) in walk(path):
            f.extend(filenames)
            break
        
        if f:
            file_name = f[len(f)-1]
            file_dir = path+"/"+file_name


            info = detect(file_dir)

            f.pop(len(f)-1)


            if info:
                link = upload(file_dir)

                date = file_name.replace(".jpg", "")
                send_intruder(date, info, link)
                    
            remove(file_dir)


                

