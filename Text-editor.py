def read_text_file(file):
    #file name is entered as 'file.txt'
    with open(file) as f:
        contents = f.read()
        return contents


def edit_text_file(file, new_text):
    #this function will overwrite the current txt file
    with open(file, mode = 'w') as f:
    #opens file as read and write option - any edits overwrites past files
        edited_file = f.write(new_text)

def add_to_file(file,add_text):
    #this function adds to text file
    with open(file, mode = 'a') as f:
        new_file = f.write(add_text)
        