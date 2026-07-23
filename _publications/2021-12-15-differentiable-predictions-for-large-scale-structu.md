---
title: "Differentiable Predictions for Large Scale Structure with SHAMNet"
collection: publications
permalink: /publication/2021-differentiable-predictions-for-large-scale-structu
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2112.08423v3)'
date: 2021-12-15
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2112.08423v3'
citation: 'Andrew P. Hearin, Nesar Ramachandra, Matthew R. Becker, Joseph DeRose (2021). \"Differentiable Predictions for Large Scale Structure with SHAMNet\". arXiv preprint.'
---

In simulation-based models of the galaxy-halo connection, theoretical predictions for galaxy clustering and lensing are typically made based on Monte Carlo realizations of a mock universe. In this paper, we use Subhalo Abundance Matching (SHAM) as a toy model to introduce an alternative to stochastic predictions based on mock population, demonstrating how to make simulation-based predictions for clustering and lensing that are both exact and differentiable with respect to the parameters of the model. Conventional implementations of SHAM are based on iterative algorithms such as Richardson-Lucy deconvolution; here we use the JAX library for automatic differentiation to train SHAMNet, a neural network that accurately approximates the stellar-to-halo mass relation (SMHM) defined by abundance matching. In our approach to making differentiable predictions for large scale structure, we map parameterized PDFs onto each simulated halo, and calculate gradients of summary statistics of the galaxy distribution by using autodiff to propagate the gradients of the SMHM through the statistical estimators used to measure one- and two-point functions. Our techniques are quite general, and we conclude with an overview of how they can be applied in tandem with more complex, higher-dimensional models, creating the capability to make differentiable predictions for the multi-wavelength universe of galaxies.
