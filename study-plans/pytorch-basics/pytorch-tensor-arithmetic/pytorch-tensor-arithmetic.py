import torch

def tensor_op(x, y, op):
    x = torch.tensor(x)
    y = torch.tensor(y)

    if op == "add":
        return torch.add(x, y).tolist()
    elif op == "multiply":
        return torch.mul(x, y).tolist()
    elif op == "matmul":
        return torch.matmul(x, y).tolist()
    elif op == "power":
        return torch.pow(x, y).tolist()
    else:
        return torch.max(x,y).tolist()