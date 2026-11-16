---
title: "Emulation, Inference & Uncertainty Quantification"
excerpt: "Research in emulation, inference & uncertainty quantification"
collection: portfolio
---

The frontier of scientific and engineering research is increasingly characterized by computationally intensive simulations, essential for understanding complex phenomena and optimizing intricate designs. However, the high computational cost associated with these high-fidelity models often hinders comprehensive parameter exploration, real-time analysis, and uncertainty quantification. This challenge has spurred significant innovation in the development of surrogate models, emulators, and reduced-order models (ROMs). These techniques are designed to approximate the behavior of complex systems with drastically reduced computational expense, thereby enabling efficient exploration of high-dimensional parameter spaces and accelerating discovery cycles across various disciplines.

A critical component of reliable scientific inquiry is the rigorous quantification of uncertainty. Beyond simply speeding up computations, it is imperative to understand the confidence associated with model predictions and the propagation of uncertainties from input data and model assumptions. Uncertainty Quantification (UQ) provides the framework for this, and its integration with modern machine learning and artificial intelligence methods is vital for developing trustworthy, interpretable predictive models. This ensures that scientific conclusions drawn from these models are robust, well-characterized, and supported by quantifiable measures of their reliability, particularly in data-rich fields like cosmology, high-energy physics, and fluid dynamics.

My research specifically focuses on developing and applying advanced probabilistic machine learning techniques to address these grand challenges in scientific computing. I have developed novel frameworks for emulation and inference, leveraging Probabilistic Neural Networks (PNNs) and Gaussian Process emulation to build highly accurate and computationally efficient surrogate models. A significant contribution involves the creation of reduced-order surrogates for complex fluid flows, where PNNs not only accelerate simulations but also inherently quantify uncertainty in their predictions. This includes exploring latent-space time evolution for non-intrusive reduced-order models, enhancing their predictive capabilities for dynamic systems.

I have applied these methodologies to critical problems across various scientific disciplines. In cosmology, my work includes emulator-based inference of cosmological subgrid models and the development of matter power spectrum emulators for modified gravity theories, enabling more efficient exploration of alternative universe models and refining our understanding of large-scale structure formation. Furthermore, I have contributed to interpretable uncertainty quantification in AI for High Energy Physics, ensuring robust and reliable scientific discovery from vast experimental datasets. My research also extends to using PNNs for fluid flow surrogate modeling and data recovery, demonstrating the robustness of these probabilistic approaches in handling sparse or incomplete data while providing essential uncertainty estimates, thereby advancing both the efficiency and trustworthiness of scientific computation.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/emulator-based-inference-of-cosmological-subgrid-m_plot_1_9c094db3.png" alt="Figure from Emulator-Based Inference of Cosmological Subgrid Models" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Emulator-Based Inference of Cosmological Subgrid Models</div>
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
