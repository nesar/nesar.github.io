---
title: "AstroPT: Scaling Large Observation Models for Astronomy"
collection: publications
permalink: /publication/2024-astropt-scaling-large-observation-models-for-astro
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2405.14930v1)'
date: 2024-05-23
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2405.14930v1'
citation: 'Michael J. Smith, Ryan J. Roberts, Eirini Angeloudi, Marc Huertas-Company (2024). \"AstroPT: Scaling Large Observation Models for Astronomy\". arXiv preprint.'
---

This work presents AstroPT, an autoregressive pretrained transformer developed with astronomical use-cases in mind. The AstroPT models presented here have been pretrained on 8.6 million $512 \times 512$ pixel $grz$-band galaxy postage stamp observations from the DESI Legacy Survey DR8. We train a selection of foundation models of increasing size from 1 million to 2.1 billion parameters, and find that AstroPT follows a similar saturating log-log scaling law to textual models. We also find that the models' performances on downstream tasks as measured by linear probing improves with model size up to the model parameter saturation point. We believe that collaborative community development paves the best route towards realising an open source `Large Observation Model' -- a model trained on data taken from the observational sciences at the scale seen in natural language processing. To this end, we release the source code, weights, and dataset for AstroPT under the MIT license, and invite potential collaborators to join us in collectively building and researching these models.
