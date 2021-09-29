from os import walk, remove
from scripts.faceAPI import detect
from scripts.imgur_uploader import upload
from scripts.telegram_bot import send_intruder





def api_controller():
    path = './shots'
    while True:

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
                print(link)
                send_intruder(file_name, info, link)
                    
            remove(file_dir)


                

