import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
              'TrainLatitude',
              'TrainLongitude',
              'TrainCode',
              'TrainDate',
              'PublicMessage',
              'Direction'
              ]

url ="https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
#to print xml
#print (doc.toprettyxml())

#to store the xml in a file
with open("trainxml","w") as xmlfp:
      doc.writexml(xmlfp)
#to save in csv file
with open("week02_train.csv",mode="w", newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t',quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    dataList=[]
    for retriveTag in retrieveTags:
        datanode = objTrainPositionsNodes.getElementsByTagName(retriveTag).item(0)
        dataList.append(datanode.firstChild.nodeValue.strip())

    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()

        if traincode.startswith("E"):
            print (traincode)
            dataList = []
            for retriveTag in retrieveTags:
                datanode=objTrainPositionsNode.getElementsByTagName(retriveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
            train_writer.writerow(dataList)

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNodes in objTrainPositionsNodes:
    trainlatitudenode = objTrainPositionsNodes.getElementsByTagName("TrainLatitude").item(0)
    trainlatitude = trainlatitudenode.firstChild.nodeValue.strip()
    print (trainlatitude)
    
