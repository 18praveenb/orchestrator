# Week 2 Meeting Resources

First, read an [overview](https://medium.com/@devnag/seq2seq-the-clown-car-of-deep-learning-f88e1204dac3) of seq2seq if you haven't already.

## Notes on Seq2Seq

- [Link to original paper](https://arxiv.org/pdf/1409.3215.pdf) (optional)

### [Autoregressive models](https://www.investopedia.com/terms/a/autoregressive.asp)

- For time series data $f(x)$, predicting $f(x + 1)$ using $f(1)$ ... $f(x)$.

### Why learn Seq2Seq?

- It's a (relatively) simple model using RNNs.
- It's a good case study for sequence to sequence problems like machine translation.
- ToneNet uses Seq2Seq!

### RNNs

Essentially, a recurrent neural network takes in an input and past state. Then it emits an output and a new state. So it's able to carry "memory" of previous inputs via the state variable.

LSTMs are a sophisticated type of RNN that are designed to have better gradient backpropagation.

GRUs are a weird variant of LSMs where the output and hidden state are the same. They should not work well, but for some reason they do.

### How Seq2Seq works

It takes in a sentence in one language, which is passed through a series of RNN cells that update a state. Then, at the end of the sentence, the state is used to generate a translation of the sentence. Its "input" is just the last word, and it continues until hitting an end-of-sentence.

For some reason, it worked better when translating a sentence input backwards.

### Attention

Attention is calculated over the input, then pointwise multiplied with the input. It allows the network to weight some features more heavily than others.

## [Seq2Seq tutorial](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)

This is just to get started with Pytorch. Recommend using Google Colab.

Make sure to read over the code and understand what it's doing. Some of the coding standards used aren't ideal. For instance, at one point `torch.bmm` is used, where `torch.matmul` is the most general way of multiplying tensors (works with vectors, 2d and batched 3d tensors etc.).
