---
title: "Predicting New Concept-Object Associations in Astronomy by Mining the Literature"
collection: publications
permalink: /publication/2026-predicting-new-concept-object-associations-in-astr
excerpt: '[<u><span style="color:blue">arXiv</span></u>](http://arxiv.org/abs/2602.14335v2)'
date: 2026-02-15
venue: 'arXiv preprint'
paperurl: 'http://arxiv.org/abs/2602.14335v2'
citation: 'Jinchu Li, Yuan-Sen Ting, Alberto Accomazzi, Tirthankar Ghosal, Nesar Ramachandra (2026). \"Predicting New Concept-Object Associations in Astronomy by Mining the Literature\". arXiv preprint.'
---

We construct a concept-object knowledge graph from the full astro-ph corpus through July 2025. Using an automated pipeline, we extract named astrophysical objects from OCR-processed papers, resolve them to SIMBAD identifiers, and link them to scientific concepts annotated in the source corpus. We then test whether historical graph structure can forecast new concept-object associations before they appear in print. Because the concepts are derived from clustering and therefore overlap semantically, we apply an inference-time concept-similarity smoothing step uniformly to all methods. Across four temporal cutoffs on a physically meaningful subset of concepts, an implicit-feedback matrix factorization model (alternating least squares, ALS) with smoothing outperforms the strongest neighborhood baseline (KNN using text-embedding concept similarity) by 16.8% on NDCG@100 (0.144 vs 0.123) and 19.8% on Recall@100 (0.175 vs 0.146), and exceeds the best recency heuristic by 96% and 88%, respectively. These results indicate that historical literature encodes predictive structure not captured by global heuristics or local neighborhood voting, suggesting a path toward tools that could help triage follow-up targets for scarce telescope time.
