---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine Learning (ML) has emerged as a transformative paradigm across numerous scientific disciplines, fundamentally altering how researchers approach complex data analysis, model building, and discovery. In fields ranging from astrophysics and cosmology to high energy physics and advanced engineering, ML tools are proving indispensable for extracting actionable insights from increasingly vast and intricate datasets, often involving processing terabytes of observational data, simulating physical phenomena, or optimizing experimental designs.

A central challenge in many scientific domains is to develop ML models that are not only performant but also interpretable, robust to noisy or sparse data, and capable of quantifying their inherent uncertainties. Research in this area explores advanced techniques such as deep neural networks for pattern recognition, generative models for data synthesis and anomaly detection, and probabilistic frameworks for robust inference. These methodologies are crucial for tackling problems like disentangling complex physical processes, identifying subtle anomalies, and making precise predictions in scenarios where data can be high-dimensional or incomplete.

My work extensively addresses these challenges by developing and applying cutting-edge machine learning methodologies to a diverse array of scientific problems. I have pioneered advanced deep learning architectures for tasks such as Neural Network Based Point Spread Function Deconvolution in astronomy and Peculiar Velocity Estimation from Kinetic SZ Effect. My research also leverages generative adversarial networks (GANs) for "Anomaly detection in Hyper Suprime-Cam galaxy images" and for generating scientific data to enable "Physical Benchmarking for AI-Generated Cosmic Web." A key focus is on enhancing interpretability and uncertainty quantification, exemplified by "Enhancing Interpretability in Generative Modeling" and "Interpretable Uncertainty Quantification in AI for HEP," often integrating probabilistic modeling for applications like high-dimensional stress field analysis. I have further explored multi-task learning for sparse engineering data and unsupervised methods to explore galaxy morphology "Beyond the Hubble Sequence."

These technical contributions have significant implications across multiple scientific fields. In cosmology, my work contributes to understanding dark energy by exploring "Opportunities in AI/ML for the Rubin LSST Dark Energy Science Collaboration," optimizing galaxy selection for "Weak Lensing Cluster Mass Estimation," and "Benchmarking AI-evolved cosmological structure formation." For galaxy studies, I have developed a "Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection and Modeling" and innovated "Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z." My methods also extend to problems like "Global field reconstruction from sparse sensors" and "Multi-task Modeling for Engineering Applications with Sparse Data." Overall, my research aims to accelerate scientific discovery by providing robust, interpretable, and high-performance machine learning tools that extract deeper insights, enhance observational capabilities, and validate theoretical models across complex scientific datasets.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
</div>


<style>
.research-figures {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.figure-item {
  text-align: center;
  background: #f8f9fa;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.figure-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.figure-item img {
  max-width: 100%;
  height: auto;
  max-height: 300px;
  object-fit: contain;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.figure-item img:hover {
  opacity: 0.9;
}

.figure-caption {
  font-size: 0.9em;
  color: #6c757d;
  margin-top: 1rem;
  line-height: 1.4;
  font-style: italic;
}

@media (max-width: 768px) {
  .research-figures {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .figure-item {
    padding: 1rem;
  }
}
</style>

<!-- Figure Modal -->
<div id="imageModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="modalImage">
</div>

<script>
function openModal(img) {
  var modal = document.getElementById('imageModal');
  var modalImg = document.getElementById('modalImage');
  modal.style.display = 'block';
  modalImg.src = img.src;
}

function closeModal() {
  document.getElementById('imageModal').style.display = 'none';
}

window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeModal();
  }
});
</script>
