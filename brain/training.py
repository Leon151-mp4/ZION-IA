#traingning where the neural network is trained
#imports
import model
import json

#standard values (s)
#snapshots import dataset.json to here
snapshot = []
snapshot2 = []

#ClassY: are the indice of right class
classY = []

#TargetY: the compative class.
targetY = []

#TargetX: is a temporary variable create for TargetY.
targetX = [0, 0, 0]

#ramV: that's dict is for amazen some  things important.
ramV = {
     "indice": None,
     "target": None
}


from pathlib import Path
current_file = Path(__file__).resolve()
dataset_path = current_file.parent.parent / "data" / "dataset.json"
with open(dataset_path, "r", encoding="utf-8") as f:
     dataJson = json.load(f)
     dataSet = dataJson["dataset"]


classMap = {
     'conversa': 0,
     'pergunta':  1,
     'despedida': 2
}


"""
da uma pequena revisada aqui.. DE NOVO TU VAI PRECISAR EXPLICAR ISSO PRO RECRUTADOR CARA
"""
for i in dataSet:
     snapshot.append(i["label"])
     snapshot2.append(i["text"])
for element in snapshot:
     classY.append(classMap[element])

for h in classY:
     targetX = [0, 0, 0]
     targetX[h] = 1
     targetY.append(targetX)









#CalcLoss: calculate the loss.
def calcLoss(z):

     import numpy as np

     l = -np.sum(ramV["target"] * np.log(z)) 
     print("target: ", ramV["target"])
     print("loss", l) 

def trainingN():
     w, w2, b, b2, z = model.neuralIns()


     """
     REVISAR ESSA PARTE.. QUANTAS VEZES TENHO QUE REPETIR???
     """
     for indice, (target, text) in enumerate(zip(targetY, snapshot2)):
          ramV["indice"] = indice
          ramV["target"] = target
          global tValue
          tValue = model.Vectorizer([text])
          Hvalue = calcLoss(z)

     
     



