---
title: "Searching the Pareto Front: Multi-Objective Retrieval for Heterogeneous Scientific Modalities"
collection: publications
permalink: /publication/2026-searching-the-pareto-front-multi-objective-retriev
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2611.23639v1)'
date: 2026-11-18
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2611.23639v1'
citation: 'Song Young Oh, Nesar Ramachandra, Bin Xia, Ian Foster, Kyle Chard (2026). \"Searching the Pareto Front: Multi-Objective Retrieval for Heterogeneous Scientific Modalities\". arXiv preprint.'
---

In cosmology, surveys span different sky regions and wavelength ranges, resulting in uneven modality coverage across observational datasets. Such heterogeneity can be addressed through either multimodal foundation models (FMs), which learn shared embedding spaces, or independently learned modality embeddings combined via late fusion. We investigate whether the latter provides an adaptive alternative to FM-based scientific retrieval. We evaluate this approach on a galaxy retrieval task spanning diverse modalities--history of star formation, spectra of light emitted, and multi-wavelength observations from two telescopes--comparing an FM baseline with separately trained embeddings fused through multi-objective optimization based on Pareto optimality. We find that the FM baseline achieves strong embedding-space proximity, but our method preserves modality-specific distance structure that allows scientists to inspect which physical signals drive similarity. Our method also achieves improved fidelity in raw-data space: across six measured properties, its nearest neighbor is 8% closer to the query on average than that retrieved by kNN in the FM embedding space (spread 0.128 vs. 0.139). These results suggest that multi-objective retrieval can surface astrophysically coherent candidates that single-objective search alone may overlook.
