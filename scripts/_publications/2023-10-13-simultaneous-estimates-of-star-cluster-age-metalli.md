---
title: "Simultaneous Estimates of Star-cluster Age, Metallicity, Mass, and Extinction (SESAMME) I: Presenting an MCMC Approach to Spectral Stellar Population Fitting"
collection: publications
permalink: /publication/2023-simultaneous-estimates-of-star-cluster-age-metalli
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2310.09365v1)'
date: 2023-10-13
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2310.09365v1'
citation: 'Logan H. Jones, Svea Hernandez, Linda J. Smith, Bethan L. James, Alessandra Aloisi, Søren Larsen (2023). \"Simultaneous Estimates of Star-cluster Age, Metallicity, Mass, and Extinction (SESAMME) I: Presenting an MCMC Approach to Spectral Stellar Population Fitting\". arXiv preprint.'
---

We present the first version release of SESAMME, a public, Python-based full spectrum fitting tool for Simultaneous Estimates of Star-cluster Age, Metallicity, Mass, and Extinction. SESAMME compares an input spectrum of a star cluster to a grid of stellar population models with an added nebular continuum component, using Markov chain Monte Carlo (MCMC) methods to sample the posterior probability distribution in four dimensions: cluster age, stellar metallicity $Z$, reddening $E(B-V)$, and a normalization parameter equivalent to a cluster mass. SESAMME is highly flexible in the stellar population models that it can use to model a spectrum; our testing and initial science applications use both BPASS and Starburst99. We illustrate the ability of SESAMME to recover accurate ages and metallicities even at a moderate signal-to-noise ratio (S/N ~3 - 5 per wavelength bin) using synthetic, noise-added model spectra of young star clusters. Finally, we test the consistency of SESAMME with other age and metallicity estimates from the literature using a sample of HST/COS far-UV spectra towards young, massive clusters in M83 and NGC 1313. We find that, on the whole, SESAMME infers star cluster properties that are consistent with the literature in both low- and high-metallicity environments.
