---
title: "For SALE: State-Action Representation Learning for Deep Reinforcement Learning"
collection: publications
permalink: /publication/2023-for-sale-state-action-representation-learning-for-
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2306.02451v2)'
date: 2023-06-04
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2306.02451v2'
citation: 'Scott Fujimoto, Wei-Di Chang, Edward J. Smith, Shixiang Shane Gu, Doina Precup, David Meger (2023). \"For SALE: State-Action Representation Learning for Deep Reinforcement Learning\". arXiv preprint.'
---

In the field of reinforcement learning (RL), representation learning is a proven tool for complex image-based tasks, but is often overlooked for environments with low-level states, such as physical control problems. This paper introduces SALE, a novel approach for learning embeddings that model the nuanced interaction between state and action, enabling effective representation learning from low-level states. We extensively study the design space of these embeddings and highlight important design considerations. We integrate SALE and an adaptation of checkpoints for RL into TD3 to form the TD7 algorithm, which significantly outperforms existing continuous control algorithms. On OpenAI gym benchmark tasks, TD7 has an average performance gain of 276.7% and 50.7% over TD3 at 300k and 5M time steps, respectively, and works in both the online and offline settings.
