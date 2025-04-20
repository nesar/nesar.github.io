---
title: "Anomaly detection in astronomical images with generative adversarial networks"
collection: publications
permalink: /publication/2020-anomaly-detection-in-astronomical-images-with-gene
excerpt: '[<u><span style="color:blue">Google Scholar</span></u>](https://scholar.google.com/scholar?q=Anomaly+detection+in+astronomical+images+with+generative+adversarial+networks)'
date: 2020-01-01
venue: 'arXiv preprint arXiv:2012.08082'
paperurl: 'https://arxiv.org/abs/2012.08082'
citation: 'Kate Storey-Fisher and Marc Huertas-Company and Nesar Ramachandra and Francois Lanusse and Alexie Leauthaud and Yifei Luo and Song Huang (2020). "Anomaly detection in astronomical images with generative adversarial networks". arXiv preprint arXiv:2012.08082.'
---

Summary: We present an anomaly detection method using Wasserstein generative adversarial networks (WGANs) on optical galaxy images from the wide-field survey conducted with the Hyper Suprime-Cam (HSC) on the Subaru Telescope in Hawai'i. The WGAN is trained on the entire sample, and learns to generate realistic HSC-like images that follow the distribution of the training data. We identify images which are less well-represented in the generator's latent space, and which the discriminator flags as less realistic; these are thus anomalous with respect to the rest of the data. We propose a new approach to characterize these anomalies based on a convolutional autoencoder (CAE) to reduce the dimensionality of the residual differences between the real and WGAN-reconstructed images. We construct a subsample of ~9,000 highly anomalous images from our nearly million object sample, and further identify interesting anomalies within these; these include galaxy mergers, tidal features, and extreme star-forming galaxies. The proposed approach could boost unsupervised discovery in the era of big data astrophysics.
