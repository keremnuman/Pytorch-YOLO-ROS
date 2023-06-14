import torch
weight1 = torch.load("/home/keremnuman/Desktop/weights/best1.pt")
weight2 = torch.load("/home/keremnuman/Desktop/weights/best2.pt")

weights_dict = {"submodel1": weight1, "submodel2": weight2,}

torch.save(weights_dict, "/home/keremnuman/Desktop/merged_weights.pt")
