import os
import xml.etree.ElementTree as ET

Type_List = []

class Object:
    def __int__(self, name, type, center, height, width):
        self.name = name
        self.type = type
        self.center = center
        self.heightt = height
        self.width = width

def get_Cord(bndbox, img_width, img_height):
    xmin = bndbox.find('xmin').text / img_width
    ymin = bndbox.find('ymin').text / img_height
    xmax = bndbox.find('xmax').text / img_width
    ymax = bndbox.find('ymax').text / img_height

    center = {"x" : (xmax + xmin) / 2 , "y" : (ymax + ymin) / 2}
    height = abs(ymax - center['y'])
    width = abs(xmax - center['x'])

    return center, height, width


path = r'C:\Users\sorou\Documents\PlateRecognition\PlateRecognitionModel\PlateDataset\test'

files = os.listdir(path)


for file in files:
    if ".xml" in file:

        file_obj = []

        tree = ET.parse(os.path.join(path,file))
        root = tree.getroot()

        size = root.find('size')
        width = size.find('width').text
        height = size.find('height').text

        for res in root.findall('object'):
            name = res.find('name')

            if not name.text in Type_List:
                Type_List.append(name.text)

            bndbox = name.find('bndbox')

            O_center, O_height, O_width = get_Cord(bndbox, width, height)



print(files)