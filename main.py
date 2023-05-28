import os
import xml.etree.ElementTree as ET

Type_List = []
RoundDesimal = 4

def Convert_2_Normalized(bndbox, img_width, img_height):
    output = {}

    xmin = int(bndbox.find('xmin').text) / img_width
    ymin = int(bndbox.find('ymin').text) / img_height
    xmax = int(bndbox.find('xmax').text) / img_width
    ymax = int(bndbox.find('ymax').text) / img_height

    center = {"x" : round((xmax + xmin) / 2, RoundDesimal) , "y" :round ((ymax + ymin) / 2, RoundDesimal)}
    height = round(abs(ymax - center['y']), RoundDesimal)
    width = round(abs(xmax - center['x']), RoundDesimal)

    output['center'] = center
    output['height'] = height
    output['width'] = width

    return output

def get_cord(file):

    file_obj = []

    tree = ET.parse(os.path.join(path, file))
    root = tree.getroot()

    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    for res in root.findall('object'):
        name = res.find('name')

        if not name.text in Type_List:
            Type_List.append(name.text)

        bndbox = res.find('bndbox')

        Normalized = Convert_2_Normalized(bndbox, width, height)
        Normalized['name'] = file
        Normalized['Type'] = Type_List.index(name.text)

        file_obj.append(Normalized)

    return file_obj


def Create_TXT_File(file_obj):
    New_Name = file.split('.')[0] + '.txt'

    New_File = open(os.path.join(path, New_Name), 'x')

    for Obj in file_obj:
        text = str(Obj['Type']) + ' ' + str(Obj['center']['x']) + ' ' + str(Obj['center']['y']) + ' ' + str(
            Obj['width']) + ' ' + str(Obj['height']) + '\n'
        New_File.write(text)

#Main

# Path to annotation folder
path = r'C:\Users\sorou\Documents\PlateRecognition\PlateDataset\test'

files = os.listdir(path)

for file in files:
    if ".xml" in file:
        file_obj = get_cord(file)
        Create_TXT_File(file_obj)

