---
title: "Application of probabilistic modeling and automated machine learning
  framework for high-dimensional stress field"
collection: publications
permalink: /publication/2023application-of-probabilistic-modeling-and-automated-machine-learning--framework-for-high-dimensional-stress-field
excerpt: '[<u><span style="color:blue"> arXiv link </span></u>](http://arxiv.org/abs/2303.16869v2)'
date: 2023-03-15
venue: 'Preprint'
paperurl: 'http://arxiv.org/abs/2303.16869v2'
citation: 'Lele Luan; Nesar Ramachandra; Sandipp Krishnan Ravi; Anindya Bhaduri; Piyush Pandita; Prasanna Balaprakash; Mihai Anitescu; Changjie Sun; Liping Wang; Application of probabilistic modeling and automated machine learning
  framework for high-dimensional stress field, Preprint'
---


Summary: Modern computational methods, involving highly sophisticated mathematical
formulations, enable several tasks like modeling complex physical phenomenon,
predicting key properties and design optimization. The higher fidelity in these
computer models makes it computationally intensive to query them hundreds of
times for optimization and one usually relies on a simplified model albeit at
the cost of losing predictive accuracy and precision. Towards this, data-driven
surrogate modeling methods have shown a lot of promise in emulating the
behavior of the expensive computer models. However, a major bottleneck in such
methods is the inability to deal with high input dimensionality and the need
for relatively large datasets. With such problems, the input and output
quantity of interest are tensors of high dimensionality. Commonly used
surrogate modeling methods for such problems, suffer from requirements like
high number of computational evaluations that precludes one from performing
other numerical tasks like uncertainty quantification and statistical analysis.
In this work, we propose an end-to-end approach that maps a high-dimensional
image like input to an output of high dimensionality or its key statistics. Our
approach uses two main framework that perform three steps: a) reduce the input
and output from a high-dimensional space to a reduced or low-dimensional space,
b) model the input-output relationship in the low-dimensional space, and c)
enable the incorporation of domain-specific physical constraints as masks. In
order to accomplish the task of reducing input dimensionality we leverage
principal component analysis, that is coupled with two surrogate modeling
methods namely: a) Bayesian hybrid modeling, and b) DeepHyper's deep neural
networks. We demonstrate the applicability of the approach on a problem of a
linear elastic stress field data.
