---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The intersection of scientific computing and artificial intelligence has opened new frontiers in addressing computationally intensive problems across various scientific disciplines. In fields such as cosmology, fluid dynamics, and materials science, high-fidelity simulations are indispensable for understanding complex phenomena. However, these simulations are often prohibitively expensive, consuming vast computational resources and time. This bottleneck impedes comprehensive parameter space exploration, robust uncertainty quantification, and real-time analysis, thereby slowing the pace of scientific discovery and predictive model development.

To overcome these limitations, the research area of emulation and inference leverages advanced machine learning techniques to develop fast, accurate, and robust surrogate models. These "emulators" learn complex input-output relationships of high-dimensional systems, effectively replacing computationally demanding simulations with lightweight, data-driven approximations. Key methodologies include deep neural networks, Gaussian processes, and reduced-order modeling. By embedding physical principles and probabilistic frameworks, researchers can accelerate forward predictions, enable efficient inverse problem solving, and provide rigorous uncertainty quantification, all crucial for reliable scientific conclusions.

My research in Emulation & Inference focuses on developing innovative machine learning and statistical methods to accelerate scientific discovery and enhance our ability to draw meaningful conclusions from complex data. I have concentrated on creating robust, interpretable, and computationally efficient surrogate models for challenging problems in cosmology and fluid dynamics. For instance, I developed SHAMNet, a differentiable neural network designed for large-scale structure predictions in cosmology. This work significantly improves the efficiency of cosmological inference by enabling direct gradient-based optimization through the prediction pipeline.

Furthermore, my contributions include the development of probabilistic neural networks for fluid flow surrogate modeling, providing rapid predictions while inherently quantifying uncertainty—critical for reliable engineering and scientific applications, including data recovery. In cosmology, I created a highly accurate matter power spectrum emulator for f(R) modified gravity cosmologies, enabling rapid exploration of alternative gravity theories. My work also explores novel reduced-order modeling approaches, such as using Gaussian process emulation in latent spaces for the time evolution of non-intrusive models, offering efficient ways to simulate complex, time-dependent systems. Collectively, these efforts provide powerful tools that transform our ability to analyze and understand complex scientific systems, pushing the boundaries of what is computationally feasible.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_2_68f5e3f1.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/matter-power-spectrum-emulator-for-fr-modified-gra_plot_1_d6154d54.png" alt="Figure from Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/latent-space-time-evolution-of-non-intrusive-reduc_plot_3_698663be.png" alt="Figure from Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation</div>
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
