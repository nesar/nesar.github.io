---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The study of complex physical systems, ranging from cosmic evolution to fluid dynamics, often relies on computationally intensive simulations. These high-fidelity models, while accurate, pose significant challenges for rapid parameter space exploration, robust uncertainty quantification, and real-time analysis, which are crucial for scientific discovery and engineering design. The development of efficient surrogate models, often referred to as emulators or reduced-order models, has emerged as a vital strategy to overcome these computational bottlenecks.

These advanced modeling techniques leverage principles from machine learning and statistics to construct fast, yet accurate, approximations of the underlying physical simulations. By learning the input-output relationship of complex models, emulators can generate predictions orders of magnitude faster than their full-fidelity counterparts. This acceleration enables comprehensive exploration of vast parameter spaces, facilitating Bayesian inference, sensitivity analysis, and the identification of optimal system configurations. A key trend in this field involves incorporating probabilistic frameworks and differentiability into these surrogates, allowing for not only predictions but also the quantification of uncertainty and the efficient backpropagation of gradients for inverse problems and optimization.

My work specifically addresses these challenges by developing cutting-edge emulation and inference methodologies across diverse scientific domains. I have focused on building highly efficient and robust machine learning-based surrogates, particularly utilizing neural networks and Gaussian processes, to accelerate predictions and enable sophisticated inference. In cosmology, my contributions include developing emulator-based inference for cosmological subgrid models, enabling rapid parameter estimation for processes unresolved by large-scale simulations. I also pioneered SHAMNet, a framework for differentiable predictions of Large Scale Structure, which facilitates gradient-based optimization and inverse problem solving in the context of galaxy formation and evolution, and created emulators for the matter power spectrum in f(R) modified gravity cosmologies.

Furthermore, I have developed probabilistic neural network-based reduced-order surrogates for fluid flows, significantly improving the speed and robustness of predictions while providing crucial uncertainty estimates. This includes innovations in latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, which allows for efficient temporal forecasting of complex fluid dynamics. My research also extends to using probabilistic neural networks for fluid flow surrogate modeling and data recovery, demonstrating their utility in reconstructing missing data and providing robust predictions even from sparse observations. These methodologies collectively push the boundaries of computational efficiency and probabilistic inference in complex physical systems.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/emulator-based-inference-of-cosmological-subgrid-m_plot_1_9c094db3.png" alt="Figure from Emulator-Based Inference of Cosmological Subgrid Models" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Emulator-Based Inference of Cosmological Subgrid Models</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/matter-power-spectrum-emulator-for-fr-modified-gra_plot_1_d6154d54.png" alt="Figure from Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies</div>
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
