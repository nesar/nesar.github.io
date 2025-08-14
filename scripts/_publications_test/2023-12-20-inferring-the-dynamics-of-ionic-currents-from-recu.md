---
title: "Inferring the dynamics of ionic currents from recursive piecewise data assimilation of approximate neuron models"
collection: publications
permalink: /publication/2023-inferring-the-dynamics-of-ionic-currents-from-recu
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2312.12888v1)'
date: 2023-12-20
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2312.12888v1'
citation: 'Stephen A. Wells, Joseph D. Taylor, Paul G. Morris, Alain Nogaret (2023). \"Inferring the dynamics of ionic currents from recursive piecewise data assimilation of approximate neuron models\". arXiv preprint.'
---

We construct neuron models from data by transferring information from an observed time series to the state variables and parameters of Hodgkin-Huxley models. When the learning period completes, the model will predict additional observations and its parameters uniquely characterise the complement of ion channels. However, the assimilation of biological data, as opposed to model data, is complicated by the lack of knowledge of the true neuron equations. Reliance on guessed conductance models is plagued with multi-valued parameter solutions. Here, we report on the distributions of parameters and currents predicted with intentionally erroneous models, over-specified models, and an approximate model fitting hippocampal neuron data. We introduce a recursive piecewise data assimilation (RPDA) algorithm that converges with near-perfect reliability when the model is known. When the model is unknown, we show model error introduces correlations between certain parameters. The ionic currents reconstructed from these parameters are excellent predictors of true currents and carry a higher degree of confidence, >95.5%, than underlying parameters, >53%. Unexpressed ionic currents are correctly filtered out even in the presence of mild model error. When the model is unknown, the covariance eigenvalues of parameter estimates are found to be a good gauge of model error. Our results suggest that biological information may be retrieved from data by focussing on current estimates rather than parameters.
