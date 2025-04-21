---
title: "Deconvolution of Astronomical Images with Deep Neural Networks"
collection: publications
permalink: /publication/2025-deconvolution-of-astronomical-images-with-deep-neu
excerpt: '[<u><span style="color:blue">Google Scholar</span></u>](https://scholar.google.com/scholar?q=Deconvolution+of+Astronomical+Images+with+Deep+Neural+Networks)'
date: 2025-01-01
venue: 'Preprint'
paperurl: 'https://openreview.net/forum?id=wduF2lfW30'
citation: 'Hong Wang and Sreevarsha Sreejith and Yuewei Lin and Nesar Soorve Ramachandra and Anže Slosar and Shinjae Yoo (2025). "Deconvolution of Astronomical Images with Deep Neural Networks". Preprint.'
---

Optical astronomical images are strongly affected by the point spread function (PSF) of the optical system and the atmosphere (seeing) which blurs the observed image. The amount of blurring depends on both the observed band, and more crucially, on the atmospheric conditions during observation. A typical astronomical image will therefore have a unique PSF that is non-circular and different in different bands. Observations of known stars give us an estimation of this PSF. Any serious candidate for production analysis of astronomical images must take the known PSF into account during image analysis. So far the majority of applications of neural networks (NN) to astronomical image analysis have ignored this problem by assuming a fixed PSF in training and validation. We present a neural network architecture based on Deep Wiener Deconvolution Network (DWDN) that takes the PSF shape into account when performing deconvolution, a possible approach of leveraging PSF information in neural networks. We study the performance of this algorithm under realistic observational conditions. We employ two regularization schemes and study custom loss functions that are optimized for quantities of interest to astronomers.  We show that our algorithm can successfully recover unbiased image properties such as colors, ellipticities and orientations for sufficiently high signal-to-noise. This study represents a comprehensive application of AI in astronomy, where the experimental design, model construction, optimization criteria, error estimation and metrics of benchmarks are all meticulously tailored to the domain problem.
