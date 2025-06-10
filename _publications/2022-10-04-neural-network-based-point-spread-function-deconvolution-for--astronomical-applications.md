---
title: "Neural Network Based Point Spread Function Deconvolution For
  Astronomical Applications"
collection: publications
permalink: /publication/2022neural-network-based-point-spread-function-deconvolution-for--astronomical-applications
excerpt: '[<u><span style="color:blue"> arXiv link </span></u>](http://arxiv.org/abs/2210.01666v2)'
date: 2022-10-04
venue: 'Preprint'
paperurl: 'http://dx.doi.org/10.21105/astro.2210.01666'
citation: 'Hong Wang; Sreevarsha Sreejith; Yuewei Lin; Nesar Ramachandra; Anže Slosar; Shinjae Yoo; Neural Network Based Point Spread Function Deconvolution For
  Astronomical Applications, Preprint'
---


Summary: Optical astronomical images are strongly affected by the point spread
function (PSF) of the optical system and the atmosphere (seeing) which blurs
the observed image. The amount of blurring depends both on the observed band,
and on the atmospheric conditions during observation. A typical astronomical
image will likely have a unique PSF, that is non-circular and different in
different bands. At the same time, observations of known stars also give us an
accurate determination of this PSF. Therefore, any serious candidate for
production analysis of astronomical images must take the known PSF into account
during the image analysis. So far, the majority of applications of neural
networks (NN) to astronomical image analysis have ignored this problem by
assuming a fixed PSF in training and validation. We present a neural-network
based deconvolution algorithm based on Deep Wiener Deconvolution Network
(DWDN). This algorithm belongs to a class of non-blind deconvolution
algorithms, since it assumes the PSF shape is known. We study the performance
of different versions of this algorithm under realistic observational
conditions in terms of the recovery of the most relevant astronomical
quantities such as colors, ellipticities and orientations. We investigate
custom loss functions that optimize the recovery of astronomical quantities
with mixed results.
