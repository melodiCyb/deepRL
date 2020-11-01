import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

def hidden_init(layer):
    fan_in = layer.weight.data.size()[0]
    lim = 1./np.sqrt(fan_in)
    return (-lim, lim)

class Actor(nn.Module):
    """Actor (Policy) Model"""
    
    def __init__(self, state_size, action_size, seed, leakiness=0.01):
        """
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed to use
            
        """
        
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, 400)
        self.bn1 = nn.BatchNorm1d(400)
        self.fc2 = nn.Linear(400, 300)
        self.fc3 = nn.Linear(300, action_size)
        self.leakiness = leakiness
        self.reset_parameters()
    
    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)
    
    def forward(self, state):
        "Build an actor network that maps states to actions"
        if state.dim()==1: state = torch.unsqueeze(state, 0)
        x = F.leaky_relu(self.fc1(state), self.leakiness)
        x = self.bn1(x)
        x = F.leaky_relu(self.fc2(x), self.leakiness)
        return torch.tanh(self.fc3(x))
    
class Critic(nn.Module):
    """Critic (Value) Model"""
    
    def __init__(self, state_size, action_size, seed, leakiness=0.01):
        """
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed to use
           
        """
        
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, 400)
        self.bn1 = nn.BatchNorm1d(400)
        self.fc2 = nn.Linear(400+action_size, 300)
        self.fc3 = nn.Linear(300, 1)
        self.leakiness = leakiness
        self.reset_parameters()
    
    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)
    
    def forward(self, state, action):
        "Build an actor network that maps states to actions"
        if state.dim()==1: state = torch.unsqueeze(state, 0)
        x = F.leaky_relu(self.fc1(state), self.leakiness)
        x = self.bn1(x)
        x = torch.cat((x, action), dim=1)
        x = F.leaky_relu(self.fc2(x), self.leakiness)
        return self.fc3(x)