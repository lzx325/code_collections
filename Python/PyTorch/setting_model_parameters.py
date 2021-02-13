import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class DualBranchNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.branch1=nn.Linear(20,10)
        self.branch2=nn.Linear(20,10)
        self.initialize()
    def forward(self,inp,branch):
        if branch == 1:
            out=self.branch1(inp)
        elif branch ==2:
            out=self.branch2(inp)
        else:
            assert False
        return out
    def initialize(self):
        self.branch1.weight.data=torch.ones_like(self.branch1.weight)
        self.branch2.weight.data=torch.ones_like(self.branch2.weight)*2
        self.branch1.bias.data.zero_()
        self.branch2.bias.data.zero_()
    def copy_params_ref(self):
        self.branch2.weight.data=self.branch1.weight
    def copy_params_val(self):
        self.branch2.weight.data[:]=self.branch1.weight
    def mutate_params(self):
        self.branch1.weight.data[:]=self.branch1.weight.data*3
        
print("value")
dbn=DualBranchNetwork()
X=torch.arange(20).float()
print(dbn(X,1))
print(dbn(X,2))
dbn.copy_params_val()
print(dbn(X,1))
print(dbn(X,2))
dbn.mutate_params()
print(dbn(X,1))
print(dbn(X,2))

print("reference")
dbn=DualBranchNetwork()
X=torch.arange(20).float()
print(dbn(X,1))
print(dbn(X,2))
dbn.copy_params_ref()
print(dbn(X,1))
print(dbn(X,2))
dbn.mutate_params()
print(dbn(X,1))
print(dbn(X,2))
