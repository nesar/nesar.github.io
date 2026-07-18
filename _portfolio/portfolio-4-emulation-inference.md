---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific research increasingly relies on complex computational simulations to model phenomena across diverse fields, from the formation of structures in the universe to the intricate dynamics of fluid flows. While these simulations provide unparalleled fidelity, their immense computational cost often limits the scope of scientific inquiry, hindering comprehensive parameter exploration, uncertainty quantification, and real-time analysis. The development of efficient data-driven approximations, known as emulators or surrogate models, has emerged as a critical strategy to overcome these computational bottlenecks, enabling accelerated scientific discovery and engineering design.

Emulation and surrogate modeling involve leveraging machine learning techniques, such as neural networks and Gaussian processes, to learn the complex input-output relationships of high-fidelity simulations. By training on a judiciously sampled set of simulation outputs, these models create fast, accurate data-driven representations that can be evaluated orders of magnitude faster than their full-scale counterparts. This approach facilitates rapid exploration of vast parameter spaces, precise inference of underlying physical parameters, and robust uncertainty quantification, all of which are essential for advancing understanding in fields characterized by high-dimensional data and computationally intensive models. Reduced-order modeling further complements this by simplifying complex dynamic systems into lower-dimensional representations, capturing essential physics while significantly reducing computational overhead.

My research extensively leverages and extends these cutting-edge methodologies to address critical challenges in both cosmology and fluid dynamics. In cosmology, I have developed high-fidelity emulators for the "Matter Power Spectrum in f(R) Modified Gravity Cosmologies," accelerating parameter inference and enabling the exploration of alternative gravitational theories. Additionally, my work on "Emulator-Based Inference of Cosmological Subgrid Models" provides efficient tools for understanding galaxy formation processes. Furthermore, I have pioneered "Differentiable Predictions for Large Scale Structure with SHAMNet," where specialized neural network architectures provide gradients necessary for efficient inverse problems and parameter optimization, marking a significant step towards more robust and interpretable cosmological inference.

In the realm of fluid dynamics, my contributions focus on developing advanced probabilistic surrogate models to handle inherent uncertainties and provide robust predictions. I have introduced "Probabilistic neural network-based reduced-order surrogates for fluid flows," alongside their application in "Probabilistic neural networks for fluid flow surrogate modeling and data recovery," offering powerful tools for efficient simulation and intelligent data imputation in complex flow scenarios. My work also explores the "Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation," demonstrating how to effectively capture the dynamic behavior of complex systems in a low-dimensional space, leading to highly efficient and accurate predictions for time-evolving fluid phenomena. These developments are crucial for enabling real-time analysis, optimization, and uncertainty quantification in a wide range of scientific and engineering applications.

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
