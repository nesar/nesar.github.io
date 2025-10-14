---
title: "Benchmarking AI-evolved cosmological structure formation"
collection: publications
permalink: /publication/2025-benchmarking-ai-evolved-cosmological-structure-for
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2510.06731v2)'
date: 2025-10-08
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2510.06731v2'
citation: 'Xiaofeng Dong, Nesar Ramachandra, Salman Habib, Katrin Heitmann (2025). \"Benchmarking AI-evolved cosmological structure formation\". arXiv preprint.'
---

The potential of deep learning-based image-to-image translations has recently attracted significant attention. One possible application of such a framework is as a fast, approximate alternative to cosmological simulations, which would be particularly useful in various contexts, including covariance studies, investigations of systematics, and cosmological parameter inference. To investigate different aspects of learning-based cosmological mappings, we choose two approaches for generating suitable cosmological matter fields as datasets: a simple analytical prescription provided by the Zel'dovich approximation, and a numerical N-body method using the Particle-Mesh approach. The evolution of structure formation is modeled using U-Net, a widely employed convolutional image translation framework. Because of the lack of a controlled methodology, validation of these learned mappings requires multiple benchmarks beyond simple visual comparisons and summary statistics. A comprehensive list of metrics is considered, including higher-order correlation functions, conservation laws, topological indicators, and statistical independence of density fields. We find that the U-Net approach performs well only for some of these physical metrics, and accuracy is worse at increasingly smaller scales, where the dynamic range in density is large. By introducing a custom density-weighted loss function during training, we demonstrate a significant improvement in the U-Net results at smaller scales. This study provides an example of how a family of physically motivated benchmarks can, in turn, be used to fine-tune optimization schemes -- such as the density-weighted loss used here -- to significantly enhance the accuracy of scientific machine learning approaches by focusing attention on relevant features.
