import torch.nn as nn
class NeuralNet(nn.Module):
    """
  Preparing 3 layers of neural networks, 
  There is only one hidden layer created while respecting the complexity of the problem

 
  
  This class is basically taking three types of inputes and fusing them into one
  this is similar to what our brain does , it takes stimulas from sensory organs and then provides an command or an ouput
    """
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet,self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) #input layer
        self.l2 = nn.Linear(hidden_size, hidden_size) #single hidden layer
        self.l3 = nn.Linear(hidden_size, num_classes) # Output layer
        self.relu = nn.ReLU()
    def forward(self, x):      #Forward propagation
        out = self.l1(x) 
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out
class BERT_Model(nn.Module):
   def __init__(self, bert, no_intents):      
       super(BERT_Model, self).__init__()
       self.bert = bert 
      
       # dropout layer
       self.dropout = nn.Dropout(0.2)
       # relu activation function
       self.relu =  nn.ReLU()
       # dense layer
       self.fc1 = nn.Linear(768,512)
       self.fc2 = nn.Linear(512,256)
       self.fc3 = nn.Linear(256,no_intents)
       #softmax activation function
       self.softmax = nn.LogSoftmax(dim=1)
       #define the forward pass
   def forward(self, sent_id, mask):
      #pass the inputs to the model  
      cls_hs = self.bert(sent_id, attention_mask=mask)[0][:,0]
      
      x = self.fc1(cls_hs)
      x = self.relu(x)
      x = self.dropout(x)
      
      x = self.fc2(x)
      x = self.relu(x)
      x = self.dropout(x)
      # output layer
      x = self.fc3(x)
   
      # apply softmax activation
      x = self.softmax(x)
      return x
  
  
  