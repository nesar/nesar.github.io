---
title: "Electronic specific heat capacities and entropies from density matrix quantum Monte Carlo using Gaussian process regression to find gradients of noisy data"
collection: publications
permalink: /publication/2023-electronic-specific-heat-capacities-and-entropies-
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2305.07081v1)'
date: 2023-05-11
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2305.07081v1'
citation: 'William Z. Van Benschoten, Laura Weiler, Gabriel J. Smith, Songhang Man, Taylor DeMello, James J. Shepherd (2023). \"Electronic specific heat capacities and entropies from density matrix quantum Monte Carlo using Gaussian process regression to find gradients of noisy data\". arXiv preprint.'
---

We present a machine learning approach to calculating electronic specific heat capacities for a variety of benchmark molecular systems. Our models are based on data from density matrix quantum Monte Carlo, which is a stochastic method that can calculate the electronic energy at finite temperature. As these energies typically have noise, numerical derivatives of the energy can be challenging to find reliably. In order to circumvent this problem, we use Gaussian process regression to model the energy and use analytical derivatives to produce the specific heat capacity. From there, we also calculate the entropy by numerical integration. We compare our results to cubic splines and finite differences in a variety of molecules whose Hamiltonians can be diagonalized exactly with full configuration interaction. We finally apply this method to look at larger molecules where exact diagonalization is not possible and make comparisons with more approximate ways to calculate the specific heat capacity and entropy.
