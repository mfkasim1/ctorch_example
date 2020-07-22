import torch
import example
import example.csrc

print(example.csrc.add(1,2))
print(example.csrc.add_tensor(torch.tensor([1.]),torch.tensor([2.])))
print(example.sub_tensor(torch.tensor([1.]),torch.tensor([2.])))
