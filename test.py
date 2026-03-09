import torch
import time

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

# large tensor multiplication to stress GPU
for i in range(20):
    x = torch.randn(5000, 5000).to(device)
    y = torch.matmul(x, x)
    print("Iteration", i)
    time.sleep(0.5)
