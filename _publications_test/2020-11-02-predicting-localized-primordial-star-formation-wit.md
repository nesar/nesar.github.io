---
title: "Predicting Localized Primordial Star Formation with Deep Convolutional Neural Networks"
collection: publications
permalink: /publication/2020-predicting-localized-primordial-star-formation-wit
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2011.01358v2)'
date: 2020-11-02
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2011.01358v2'
citation: 'Azton I. Wells, Michael L. Norman (2020). \"Predicting Localized Primordial Star Formation with Deep Convolutional Neural Networks\". arXiv preprint.'
---

We investigate applying 3D deep convolutional neural networks as fast surrogate models of the formation and feedback effects of primordial stars in hydrodynamic cosmological simulations of the first galaxies. Here, we present the surrogate model to predict localized primordial star formation; the feedback model will be presented in a subsequent paper. The star formation prediction model consists of two sub-models: the first is a 3D volume classifier that predicts which (10 comoving kpc)$^3$ volumes will host star formation, followed by a 3D Inception-based U-net voxel segmentation model that predicts which voxels will form primordial stars. We find that the combined model predicts primordial star forming volumes with high skill, with $F_1 >0.995$ and true skill score $>0.994$. The star formation is localized within the volume to $\lesssim5^3$~voxels ($\sim1.6$~comoving kpc$^3$) with $F_1>0.399$ and true skill score $>0.857$. Applied to simulations with low spatial resolution, the model predicts star forming regions in the same locations and at similar redshifts as sites in resolved full-physics simulations that explicitly model primordial star formation and feedback. When applied to simulations with lower mass resolution, we find that the model predicts star forming regions at later redshift due to delayed structure formation resulting from lower mass resolution. Our model predicts primordial star formation without halo finding, so will be useful in spatially under-resolved simulations that cannot resolve primordial star forming halos. To our knowledge, this is the first model that can predict primordial star forming regions that match highly-resolved cosmological simulations.
