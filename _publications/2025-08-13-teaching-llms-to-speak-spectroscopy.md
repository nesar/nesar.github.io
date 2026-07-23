---
title: "Teaching LLMs to Speak Spectroscopy"
collection: publications
permalink: /publication/2025-teaching-llms-to-speak-spectroscopy
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2508.10075v1)'
date: 2025-08-13
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2508.10075v1'
citation: 'Nesar Ramachandra, Yuan-Sen Ting, Zechang Sun, Azton Wells, Salman Habib (2025). \"Teaching LLMs to Speak Spectroscopy\". arXiv preprint.'
---

Pre-trained Large Language Models (LLMs) have revolutionized text processing, yet adapting Transformer-based neural networks to non-textual scientific modalities typically requires specialized architectures and extensive computational resources. We demonstrate that LLaMA-3.1-8B can be efficiently repurposed to predict galaxy redshifts from spectroscopic data through Low-Rank Adaptation (LoRA), achieving competitive performance while preserving its linguistic capabilities. Using only 16 GPU-hours and adapting 0.04% of model parameters, our approach achieves a mean absolute error of 0.04 in redshift prediction while retaining over 85% of performance on AstroBench and 89% on general QA tasks from eval-harness. This minimal-effort adaptation--requiring only simple standard fine-tuning APIs--lowers barriers to entry for domain scientists and enables integrated agentic workflows where a single model handles both spectroscopic data for quantitative analysis and natural language for reasoning.
