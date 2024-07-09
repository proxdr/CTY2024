# file input output

filepath='yapNotes.txt'
with open(filepath, 'r') as fileReader:
    content= fileReader.readlines()
    print(content, end='')

