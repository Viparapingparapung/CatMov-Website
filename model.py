import torch
import torch.nn as nn

class reccom(nn.Module):
  def __init__(self):
    super().__init__()
    
    

    # embeding
    self.user = nn.Embedding(138493,32)
    self.movie = nn.Embedding(27278,32)
    # nn
    self.relu = nn.ReLU()
    self.linear_1 = nn.Linear(64,32)
    self.linear_2 = nn.Linear(32,12)
    self.linear_3 = nn.Linear(12,1,bias=False)
  def forward(self, data):
    # matrix multiplication
    data_users, data_movie= data[:,0], data[:,1]
    inp_user = self.user(data_users)
    inp_mov = self.movie(data_movie)
    input_layer1 = torch.cat((inp_user,inp_mov),-1)
    # nn
    input_layer1 = self.linear_1(input_layer1)
    activation1 = self.relu(input_layer1)

    input_layer2 = self.linear_2(activation1)
    activation2 = self.relu(input_layer2)

    input_layer3 = self.linear_3(activation2)
    return input_layer3 # คูณกันแบบ metrix