'''
Project : Manage files in Folder
by		: Roshan Kumar Thapa
Date	: 29/05/2020 
This program create under my training peroid for practical projects
'''

import os #import os module in python

def createIfNotExit(folder): # create createIfNotExit function for create folders under do not repeat principal
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername,files): # create move function for move files in folder under do not repeat principal
    for file in files:
        os.replace(file, f"{foldername}/{file}")

files = os.listdir()
files.remove("main.py") # leave the file main.py

#folders create under createIfNotExit function
createIfNotExit('Images')
createIfNotExit('Docs')
createIfNotExit('Media')
createIfNotExit('Others')

#ext for files
imgExts =[".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
docExts =[".doc",".docx",".xls",".pdf",".txt"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
mediaExts =[".mp3",".mp4",".mkv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
others=[]
for file in files:
    ext =os.path.splitext(file)[1].lower()
    if(ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

#move files into folder using move function
move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Others", others)



