---
title: "Probabilistic neural networks for fluid flow surrogate modeling and data recovery"
collection: publications
permalink: /publication/2020-probabilistic-neural-networks-for-fluid-flow-surro
excerpt: '[<u><span style='color:blue'>arXiv</span></u>](http://arxiv.org/pdf/2005.04271v3.pdf)'
date: 2020-05-08
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/pdf/2005.04271v3.pdf'
citation: 'Romit Maulik, Kai Fukami, Nesar Ramachandra, Koji Fukagata, Kunihiko Taira (2020). \"Probabilistic neural networks for fluid flow surrogate modeling and data recovery\". arXiv preprint.'
---

We consider the use of probabilistic neural networks for fluid flow {surrogate modeling} and data recovery. This framework is constructed by assuming that the target variables are sampled from a Gaussian distribution conditioned on the inputs. Consequently, the overall formulation sets up a procedure to predict the hyperparameters of this distribution which are then used to compute an objective function given training data. We demonstrate that this framework has the ability to provide for prediction confidence intervals based on the assumption of a probabilistic posterior, given an appropriate model architecture and adequate training data. The applicability of the present framework to cases with noisy measurements and limited observations is also assessed. To demonstrate the capabilities of this framework, we consider canonical regression problems of fluid dynamics from the viewpoint of reduced-order modeling and spatial data recovery for four canonical data sets. The examples considered in this study arise from (1) the shallow water equations, (2) a two-dimensional cylinder flow, (3) the wake of NACA0012 airfoil with a Gurney flap, and (4) the NOAA sea surface temperature data set. The present results indicate that the probabilistic neural network not only produces a machine-learning-based fluid flow {surrogate} model but also systematically quantifies the uncertainty therein to assist with model interpretability.
