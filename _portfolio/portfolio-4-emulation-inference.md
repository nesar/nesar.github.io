---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The simulation of complex physical systems, ranging from astrophysical phenomena to intricate fluid dynamics, presents significant computational challenges. High-fidelity simulations, while crucial for scientific discovery and engineering design, often demand vast computational resources and execution times, rendering tasks like comprehensive parameter space exploration, robust uncertainty quantification, and efficient inverse problem solving prohibitively expensive. This computational bottleneck severely limits the pace of scientific advancement and the development of optimal engineering solutions.

To overcome these limitations, the fields of emulation, surrogate modeling, and reduced-order modeling have emerged as powerful paradigms. These techniques involve constructing fast, data-driven or statistical approximations that accurately mimic the behavior of complex simulators at a fraction of the computational cost. Methodologies frequently leverage advanced machine learning techniques, such as neural networks, probabilistic neural networks, and Gaussian processes, to build these "digital twins." The objective is to provide high-fidelity predictions rapidly, enabling efficient parameter inference, real-time control, and robust exploration of system behaviors under varying conditions, thereby accelerating discovery and design cycles across diverse scientific and engineering disciplines.

My research in this domain focuses on developing and applying innovative emulation and inference techniques to complex physical systems, particularly in cosmology and fluid dynamics. I have pioneered the use of probabilistic neural networks (PNNs) for constructing reduced-order surrogates for fluid flows, demonstrating their capability not only in accurately predicting dynamic system behavior but also in robustly recovering missing or sparse data, a critical challenge in experimental fluid mechanics. Extending this, I have also developed non-intrusive reduced-order models that utilize Gaussian process emulation for precise latent-space time evolution, providing a flexible framework for modeling complex time-dependent phenomena with quantified uncertainty.

In cosmology, my contributions include developing specialized emulators for critical components of the universe's large-scale structure. I have created a Matter Power Spectrum Emulator specifically for f(R) modified gravity cosmologies, which allows for rapid exploration and inference in theories beyond standard general relativity. Furthermore, I developed SHAMNet, a framework for differentiable predictions for large-scale structure, enabling efficient, gradient-based inference of subgrid astrophysical models from observational data. My work has also addressed the challenges of cosmological subgrid models through an emulator-based inference approach, significantly accelerating the process of connecting theoretical galaxy formation models with astronomical observations. These methodologies collectively accelerate scientific discovery by transforming intractable simulation challenges into tractable inference problems, providing the tools for deeper understanding and more robust predictions.

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
