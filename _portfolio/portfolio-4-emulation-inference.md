---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific research and discovery across diverse fields, from astrophysics and cosmology to fluid dynamics, are increasingly reliant on complex numerical simulations and the analysis of vast datasets. These simulations, while powerful, are often computationally expensive, making extensive parameter space exploration, robust statistical inference, and real-time analysis prohibitive. This bottleneck necessitates the development of sophisticated computational tools capable of rapidly mimicking complex physical processes (emulation) and extracting meaningful insights from observational data (inference).

Emulation addresses this by constructing fast, accurate surrogate models, frequently employing advanced machine learning techniques, to reproduce the input-output behavior of high-fidelity simulations with significantly reduced computational cost. Concurrently, effective inference methodologies are crucial for interpreting noisy, high-dimensional datasets, enabling the accurate estimation of physical parameters and the reconstruction of underlying fields. A critical aspect permeating both emulation and inference is the rigorous quantification of uncertainty, providing interpretable confidence bounds on predictions, which is indispensable for validating scientific hypotheses and guiding future research.

My research focuses on developing advanced machine learning and statistical methodologies to address these challenges, primarily within the "Emulation & Inference" paradigm. I have engineered highly efficient emulators and reduced-order surrogate models for computationally intensive simulations, enabling rapid exploration of complex systems. For instance, I developed a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, facilitating efficient exploration of alternative gravity theories. My contributions also include probabilistic neural network-based reduced-order surrogates for fluid flows and their latent-space time evolution using Gaussian process emulation, significantly accelerating dynamic system predictions and data recovery.

Beyond emulation, my work extends to novel inference and reconstruction techniques. I have tackled critical problems in cosmology, such as reducing model error in Weak Lensing Cluster Mass Estimation through optimized galaxy selection and estimating Peculiar Velocities from the Kinetic Sunyaev-Zel'dovich (kSZ) effect using deep neural networks. Furthermore, I have innovated in global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning and developed Differentiable Predictions for Large Scale Structure with SHAMNet, providing powerful tools for cosmological inference.

A central tenet across my research is the provision of robust and interpretable uncertainty quantification. I have specifically focused on Interpretable Uncertainty Quantification in AI for High Energy Physics, and my deployment of probabilistic neural networks in areas like fluid flow modeling inherently provides rigorous uncertainty estimates. These integrated methodologies not only accelerate scientific discovery by making previously intractable simulations and analyses feasible, but also enhance the reliability and interpretability of data-driven predictions, pushing the boundaries of what is possible in fields ranging from fundamental cosmology to complex engineering applications.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/global-field-reconstruction-from-sparse-sensors-wi_plot_1_93ef286c.png" alt="Figure from Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning</div>
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
