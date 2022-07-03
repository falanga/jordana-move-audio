import torch

from gpu_test import test

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print("Using", device, " device")


test(device)
