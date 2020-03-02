## Universal Music Translation Network

### WaveNet Basics

- Model audio as a time series
- Predict the probability distribution of the next point using the previous points and a conditioning signal
- Uses stacked convolutions to incorporate information from recent and much earlier points
- NVIDIA has created some [GPU optimized code](https://github.com/NVIDIA/nv-wavenet) for WaveNet related things.

![](https://lh3.googleusercontent.com/Zy5xK_i2F8sNH5tFtRa0SjbLp_CU7QwzS2iB5nf2ijIf_OYm-Q5D0SgoW9SmfbDF97tNEF7CmxaL-o6oLC8sGIrJ5HxWNk79dL1r7Rc=w2048){.invert}

Learn more about WaveNet:

- DeepMind [blog post](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)
- [Paper](https://arxiv.org/pdf/1609.03499.pdf)

### UMTN Overview

![](https://github.com/facebookresearch/music-translation/blob/master/img/fig.png?raw=true){.invert}

- Inputs are audio files (e.g. WAV) which can be considered a [time series](https://en.wikipedia.org/wiki/Pulse-code_modulation)
- Encoder network encodes inputs into a representation that, theoretically, doesn't include any instrumentation details ("domain specific information")
- A decoder can convert the encoder output into an audio file with a specific instrumentation. Each instrumentation ("domain") has its own decoder.
- The whole network is really computationally expensive!

### Data Augmentation

- Detune the audio beforehand, to prevent overfitting.

### Losses

- Train a classifier to predict the domain from the encoded representation.
- Remember, the encoder is supposed to remove domain specific information!
- So, the loss for the encoder and decoders includes a reward (negative loss) for confusing the classifier!
- The other component of the encoder/decoder loss is that inputting a file and decoding it to the same domain should yield the same file.
- At runtime the decoder is conditioned on its previous output. But to help it learn at training time, it's conditioned on the previous ground truth output instead. This is called [teacher forcing](https://towardsdatascience.com/what-is-teacher-forcing-3da6217fed1c).
