---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The simulation and analysis of complex physical phenomena, ranging from the large-scale structure of the universe to intricate fluid dynamics, often rely on computationally intensive, high-fidelity numerical models. These simulations are crucial for advancing scientific understanding, but their exorbitant computational cost severely limits the ability to explore vast parameter spaces, perform comprehensive uncertainty quantification, or conduct rapid inference for inverse problems. This bottleneck necessitates the development of more efficient computational paradigms.

Emulation and surrogate modeling represent a powerful approach to address these challenges. These techniques involve training data-driven models, often based on a small number of high-fidelity simulations, to learn the complex input-output relationships of the underlying physical system. Once trained, these "emulators" can predict outcomes orders of magnitude faster than the original simulations, enabling swift exploration of parameter spaces, accelerated design optimization, and robust statistical inference. The integration of such models, including those incorporating uncertainty quantification, is transformative for fields where quick, accurate predictions are essential for scientific discovery and engineering innovation.

My research focuses on developing and applying advanced emulation and inference techniques to accelerate scientific discovery in cosmology and fluid mechanics. I have developed novel methodologies utilizing probabilistic neural networks, differentiable surrogates, and reduced-order models to address the computational bottlenecks associated with complex physical systems. For instance, my work includes developing emulator-based inference frameworks for cosmological subgrid models, allowing for rapid parameter estimation from observational data.

Specifically, I have contributed to the creation of SHAMNet, a framework for differentiable predictions of large scale structure, which facilitates gradient-based inference and optimization within cosmological models. Furthermore, I have developed matter power spectrum emulators for f(R) modified gravity cosmologies, significantly speeding up the exploration of alternative gravity theories. In the realm of fluid dynamics, I have advanced probabilistic neural network-based reduced-order surrogates, enabling efficient prediction of fluid flows with intrinsic uncertainty quantification. My contributions also extend to the latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, and leveraging probabilistic neural networks for effective fluid flow data recovery, providing robust solutions for complex, data-sparse scenarios. These innovations collectively aim to democratize access to high-fidelity simulations, foster robust inference under uncertainty, and accelerate the pace of scientific and engineering research.

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
