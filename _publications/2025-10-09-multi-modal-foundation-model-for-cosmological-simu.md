---
title: "Multi-modal Foundation Model for Cosmological Simulation Data"
collection: publications
permalink: /publication/2025-multi-modal-foundation-model-for-cosmological-simu
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2510.07684v1)'
date: 2025-10-09
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2510.07684v1'
citation: 'Bin Xia, Nesar Ramachandra, Azton I. Wells, Salman Habib, John Wise (2025). \"Multi-modal Foundation Model for Cosmological Simulation Data\". arXiv preprint.'
---

We present a multi-modal foundation model for astrophysical galaxy data, designed to map between simulation- and observation-based galactic features. Our encoder-only transformer flexibly ingests scalar quantities (e.g., redshifts, galaxy masses) and vectors (e.g., star formation histories, spectra), supporting multi-task training that includes within-modality reconstruction and cross-modality prediction. With a dynamic masking strategy, the model can query arbitrary galaxy properties from partial inputs -- including predicting spectra from redshift and mass, or estimating photometric redshifts from broadband magnitudes -- while also recovering missing segments within a modality. Trained on 185,000 simulated galaxies from a gigaparsec-scale Cosmology simulation, the model yields a 50% improvement in redshift estimation when combining LSST and SPHEREx photometry over LSST photometry alone, and a 63% improvement in stellar mass inference when combining late-time SFH with LSST photometry over early-time SFH with LSST photometry. The model demonstrates strong generalization across multi-modal tasks and lays the groundwork for future integration of higher-dimensional and structured data such as images, merger trees, and 3D fields. This approach provides a unified framework for connecting simulations and observations, advancing the development of generalizable astrophysical foundation models.
