#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# In[2]:


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output


# In[15]:


model=Net()
optimizer=optim.SGD(
    [
        {'params': model.conv1.parameters()},
        {'params': model.conv2.parameters(), 'lr': 1e-3}
            
    ], lr=1e-2, momentum=0)


# In[16]:


optimizer.zero_grad()
old_conv1_weight=model.conv1.weight.detach().clone()
old_conv2_weight=model.conv2.weight.detach().clone()
loss=(model.conv1.weight**2).sum()+(model.conv2.weight**2).sum()
loss.backward()
optimizer.step()


# In[18]:


print(-(model.conv1.weight-old_conv1_weight)/model.conv1.weight.grad)


# In[19]:


print(-(model.conv2.weight-old_conv2_weight)/model.conv2.weight.grad)

