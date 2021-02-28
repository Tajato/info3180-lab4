import os

path = 'uploads'

folder = os.fsencode(path)


def get_uploaded_images():
    filenames = []
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.jpeg', '.png', '.jpg') ): # whatever file types you're using...
            filenames.append(filename)
            return filenames 

#filenames.sort()  now you have the filenames and can do something with them