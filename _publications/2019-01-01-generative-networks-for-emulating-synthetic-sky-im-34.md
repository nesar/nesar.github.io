---
title: "Generative networks for emulating synthetic sky images"
collection: publications
permalink: /publication/2019-generative-networks-for-emulating-synthetic-sky-im
excerpt: '[<u><span style="color:blue">Google Scholar</span></u>](https://scholar.google.com/scholar?q=Generative+networks+for+emulating+synthetic+sky+images)'
date: 2019-01-01
venue: 'Technical report, Kavli Summer Program in Astrophysics'
paperurl: 'https://kspa.soe.ucsc.edu/sites/default/files/Guilloteau.pdf'
citation: 'Claire Guilloteau and N Ramachandra and F Lanusse and S Hassan and Y-s Ting (2019). "Generative networks for emulating synthetic sky images". Technical report, Kavli Summer Program in Astrophysics.'
---

Summary: Robust generation of high-fidelity data is an essential component of large astronomical survey analysis. While expensive simulations are typically used for creating synthetic data, recent development of fast emulators using machine learning techniques like Generative models–Variational Autoencoders [1], Generative Adversarial Networks [2] or Gaussian Processes–have made high precision predictions of cosmological functions possible. This projects deals with a natural progression of the above for emulating astronomical images using Deep Generative models. The project involves creating training images using GalSim, a software library for generating images of stars and galaxies, tuning a relatively few number of physical parameters on a spacefilling scheme. A second dataset, made of real galaxy images from Cosmic Evolution Survey–COSMOS [3, 4]–, is also considered in this work. Ensemble of generative networks, Principal Component Analysis, Gaussian Processes, Variational Autoencoders and Masked Autoregressive Flow [5], is trained at interpolating values of input parameters. Independent measurement pipelines are applied to validate the emulated images beyond visual confirmation and hold-out tests. The network will be made more physics-aware based on this preliminary results and is extended to emulate realistic synthetic images tuned for other surveys and catalogs. Generative models designed in this work are compared at generating galaxy images and Deep generative models as Variational Autoencoders outperform machine learning techniques such as Principal Component Analysis for analytical and real images. An …
