#imports of libarys
import numpy as np
import json
#Standard values:

#Value of input for the neural network use to calc math.
iValue = None

#Value of dataSet for the neural network traing
tValue = None

#control Value: decide who the network will process.
#snapshots import dataset.json to here
snapshot = []
snapshot2 = []

#Data list: usage for data of input.
dataList = []

#State: where the model check if the sistem is idle or working
state = {}

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

#z1: output value for response.
z1 = None

#z2: output value for traing.
z2 = None

#start to due TF-IDF
def Vectorizer(dataList):
        from sklearn.feature_extraction.text import TfidfVectorizer

        vectorize = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")

        result = vectorize.fit_transform(dataList).toarray()
        result = result[0][:2]


        """
          nota: tambem revisar essa parte depois pois você leon vai precisar explicar
          isso pro recutador cara :/
        """
        for i in range(5 - len(result)):
             result = np.append(result, 0)
        
        result = np.expand_dims(result, axis=0)
        return result


#control center for neural Network and the loss
def checkState(state):
    if state == {}:
         pass
    
    elif state == {"system":(True, "idle")}:
         pass
    
    elif state == {"system": (True, "Working")}: 
        global iValue
        iValue = Vectorizer([dataList[-1]])

        startNeural()



class NeuralNetwork():
    def __init__(self):


        self.b = np.random.rand(1, 10)
        self.w = np.random.rand(5, 10)

        self.b2 = np.random.rand(1, 3)
        self.w2 = np.random.rand(10, 3)



          #nota: EU REALMENTE PRECISO REVISAR ESSA PARTE MAIS VEZES :/
    def __call__(self, inputer):

        def relu(inputer):
             return np.maximum(0, inputer)
        
        def softmax(x):
            exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
            return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


        
        x = relu(np.dot(inputer, self.w  ) + self.b)
        z = softmax(np.dot(x, self.w2) + self.b2 )
        
        print("entrada:", inputer)
        print("pesos:", self.w, self.w2)
        print("bias:", self.b, self.b2)
        print("saida:", z)
        #print("Cross-Entropy: ", t)
        return self.w, self.w2, self.b, self.b2, z


#NeuralIns: create the neuralNetwork and save the Network.
neuralIns = NeuralNetwork()

#start the neural network using neuralIns
def startNeural():
     if iValue is None:
          pass

     elif isinstance(iValue, np.ndarray) and iValue.ndim == 2 :
        
        print("iValue:", iValue)
        print("tipo:", type(iValue))
        print("dimensão:", iValue.shape)

        inputC(tValue, iValue)

def inputC(tValue, iValue):
     global z1, z2
     w, w2, b, b2, z  = neuralIns(iValue)

     """
     Bloco 1: RESPONSE
     """
     z1 = z.copy()
     z1.setflags(write=False)
          

#___ TEMPORARY ___
#This is for train the ia but it will be move to training.py
        
#Import of dataset.json
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

     

     l = -np.sum(ramV["target"] * np.log(z)) 
     print("target: ", ramV["target"])
     print("loss", l) 

def trainingN():
     w, w2, b, b2, z = neuralIns()


     """
     REVISAR ESSA PARTE.. QUANTAS VEZES TENHO QUE REPETIR???
     """
     for indice, (target, text) in enumerate(zip(targetY, snapshot2)):
          ramV["indice"] = indice
          ramV["target"] = target
          global tValue
          tValue = Vectorizer([text])
          Hvalue = calcLoss(z)

     
     




