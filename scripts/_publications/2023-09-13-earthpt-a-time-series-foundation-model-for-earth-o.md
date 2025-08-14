---
title: "EarthPT: a time series foundation model for Earth Observation"
collection: publications
permalink: /publication/2023-earthpt-a-time-series-foundation-model-for-earth-o
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2309.07207v2)'
date: 2023-09-13
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2309.07207v2'
citation: 'Michael J. Smith, Luke Fleming, James E. Geach (2023). \"EarthPT: a time series foundation model for Earth Observation\". arXiv preprint.'
---

We introduce EarthPT -- an Earth Observation (EO) pretrained transformer. EarthPT is a 700 million parameter decoding transformer foundation model trained in an autoregressive self-supervised manner and developed specifically with EO use-cases in mind. We demonstrate that EarthPT is an effective forecaster that can accurately predict future pixel-level surface reflectances across the 400-2300 nm range well into the future. For example, forecasts of the evolution of the Normalised Difference Vegetation Index (NDVI) have a typical error of approximately 0.05 (over a natural range of -1 -> 1) at the pixel level over a five month test set horizon, out-performing simple phase-folded models based on historical averaging. We also demonstrate that embeddings learnt by EarthPT hold semantically meaningful information and could be exploited for downstream tasks such as highly granular, dynamic land use classification. Excitingly, we note that the abundance of EO data provides us with -- in theory -- quadrillions of training tokens. Therefore, if we assume that EarthPT follows neural scaling laws akin to those derived for Large Language Models (LLMs), there is currently no data-imposed limit to scaling EarthPT and other similar `Large Observation Models.'
