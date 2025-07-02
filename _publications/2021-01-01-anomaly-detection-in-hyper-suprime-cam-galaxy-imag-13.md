---
title: "Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks"
collection: publications
permalink: /publication/2021-anomaly-detection-in-hyper-suprime-cam-galaxy-imag
excerpt: '[<u><span style='color:blue'>arXiv</span></u>](http://arxiv.org/pdf/2105.02434v2.pdf)'
date: 2021-01-01
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/pdf/2105.02434v2.pdf'
citation: 'Kate Storey-Fisher, Marc Huertas-Company, Nesar Ramachandra, Francois Lanusse, Alexie Leauthaud, Yifei Luo, Song Huang, J. Xavier Prochaska (2021). \"Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks\". arXiv preprint.'
---

The problem of anomaly detection in astronomical surveys is becoming increasingly important as data sets grow in size. We present the results of an unsupervised anomaly detection method using a Wasserstein generative adversarial network (WGAN) on nearly one million optical galaxy images in the Hyper Suprime-Cam (HSC) survey. The WGAN learns to generate realistic HSC-like galaxies that follow the distribution of the data set; anomalous images are defined based on a poor reconstruction by the generator and outlying features learned by the discriminator. We find that the discriminator is more attuned to potentially interesting anomalies compared to the generator, and compared to a simpler autoencoder-based anomaly detection approach, so we use the discriminator-selected images to construct a high-anomaly sample of $\sim$13,000 objects. We propose a new approach to further characterize these anomalous images: we use a convolutional autoencoder to reduce the dimensionality of the residual differences between the real and WGAN-reconstructed images and perform UMAP clustering on these. We report detected anomalies of interest including galaxy mergers, tidal features, and extreme star-forming galaxies. A follow-up spectroscopic analysis of one of these anomalies is detailed in the Appendix; we find that it is an unusual system most likely to be a metal-poor dwarf galaxy with an extremely blue, higher-metallicity HII region. We have released a catalog with the WGAN anomaly scores; the code and catalog are available at https://github.com/kstoreyf/anomalies-GAN-HSC, and our interactive visualization tool for exploring the clustered data is at https://weirdgalaxi.es.
