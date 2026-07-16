---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The simulation of complex physical phenomena, such as fluid dynamics and astrophysical processes, often presents significant computational challenges due to the high dimensionality and non-linearity of the underlying equations. These high-fidelity simulations are critical for scientific discovery, engineering design, and making predictions, but their immense computational cost can severely limit the scope of scientific inquiry, parameter space exploration, and the feasibility of inverse problems like parameter inference.

To overcome these limitations, the field of computational science has increasingly turned to surrogate modeling, reduced-order models (ROMs), and emulators. These techniques aim to create computationally inexpensive approximations of complex simulators, enabling rapid evaluation, sensitivity analysis, and uncertainty quantification. Methodologies often involve machine learning techniques, such as neural networks, and statistical methods like Gaussian process emulation, to learn the input-output mapping of a high-fidelity model or data-driven system. The primary goal is to accelerate the simulation pipeline while maintaining sufficient accuracy and providing a robust quantification of predictive uncertainty.

My research focuses on developing and applying advanced emulation and inference techniques to tackle these computational bottlenecks across diverse scientific domains. I have developed novel probabilistic neural network (PNN) architectures, which provide not only efficient surrogate models for complex systems like fluid flows but also robust quantification of their predictive uncertainties. This capability is crucial for reliable decision-making and for applications such as data recovery, where missing information in fluid dynamics can be probabilistically reconstructed. Furthermore, my work extends to innovative uses of Gaussian process emulation, particularly for modeling the latent-space time evolution of non-intrusive reduced-order models, offering efficient and accurate predictions for dynamic systems.

A significant part of my contributions lies in their application to high-impact areas. In cosmology, I have developed sophisticated emulators for inferring parameters of cosmological subgrid models, which are essential for understanding galaxy formation and evolution. This includes creating a highly accurate matter power spectrum emulator specifically tailored for f(R) modified gravity cosmologies, enabling rapid exploration of alternative gravity theories and their observational signatures. These emulators dramatically reduce the computational burden of analyzing large-scale cosmological simulations, facilitating more comprehensive parameter studies and robust astrophysical inference. Through these efforts, I strive to empower scientific discovery by making previously intractable problems accessible to rigorous, uncertainty-aware analysis.

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
  <div class="figure-item">
    <img src="/images/research/figures/latent-space-time-evolution-of-non-intrusive-reduc_plot_1_662d841c.png" alt="Figure from Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation" onclick="openModal(this)" loading="lazy" />
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
