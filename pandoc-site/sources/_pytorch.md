# [Pytorch tutorial](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
- The tutorial has links to Jupyter notebooks and Google Colab notebooks!
- If running in Colab, be sure to enable the GPU (Runtime > Change runtime type)

## Summaries / key takeaways

### [What is Pytorch?](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py)
Make sure you know how to do the following:

- How to construct empty, random, all-ones, and all-zeros tensors
- How to specify tensor datatype
- Create a tensor with the same shape as another tensor, but a different datatype
- Look up tensor operations
- Add, subtract and [multiply](https://stackoverflow.com/questions/44524901/how-to-do-product-of-matrices-in-pytorch) tensors
- Convert between Numpy arrays and tensors
- Move tensors between CPU and GPU

### [Autograd](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html#sphx-glr-beginner-blitz-autograd-tutorial-py)
- Useful takeaways from this tutorial:
    - `with torch.no_grad()`
    - `requires_grad` determines whether the gradient is computed.
- Don't know how important the other stuff is. Part 3 will go into how weight updates etc. is done in practice.

### [Neural Networks](https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/neural_networks_tutorial.ipynb#scrollTo=pFyfk2z9r48d)
- Notice how they define the network as a class.
- Dense layers are called "Linear"
- What the network actually does is in "forward"
    - Layers that don't need weights (e.g. max_pool) aren't members of the class
    - E.g. `F.max_pool2d` is used in `forward` but not defined in `__init__`
- `.parameters()` gets weights
- Using `zero_grad` is important at the start of each training loop.
I copied the training loop from the end of the document, it's worth remembering.
```
optimizer.zero_grad() # Zero gradients
output = net(input)
loss = criterion(output, target) # Compute loss
loss.backward() # Backprop
optimizer.step() # Update step
```

### [Training a Classifier](https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/cifar10_tutorial.ipynb)
- Coming soon