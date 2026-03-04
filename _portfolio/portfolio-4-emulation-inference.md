---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Complex scientific and engineering domains, such as astrophysics, cosmology, and fluid dynamics, increasingly rely on high-fidelity numerical simulations to model intricate physical phenomena. These simulations, while providing unparalleled insight, are often prohibitively expensive computationally, making tasks like parameter estimation, uncertainty quantification, and design optimization extremely challenging or even impossible within practical timeframes. This computational bottleneck significantly impedes scientific discovery and the development of advanced technologies.

To overcome these limitations, the fields of emulation and surrogate modeling have emerged as critical tools. Emulators, also known as reduced-order models or surrogates, are fast, data-driven approximations of complex simulations. They are typically built using advanced machine learning techniques, including neural networks, Gaussian processes, and various dimensionality reduction methods, trained on a limited set of high-fidelity simulation outputs. These surrogate models enable rapid exploration of high-dimensional parameter spaces, facilitate efficient Bayesian inference, and provide crucial insights into system behavior in a fraction of the time required by direct simulation.

My research focuses on developing sophisticated emulation and inference frameworks to unlock the potential of computationally intensive simulations across diverse scientific applications. In cosmology, I have developed innovative approaches to accelerate the analysis of large-scale structure formation and the intricate physics of subgrid models. This includes creating highly accurate matter power spectrum emulators for f(R) modified gravity cosmologies, which are crucial for probing alternative theories of gravity. I have also pioneered differentiable methods, such as SHAMNet, to provide rapid and differentiable predictions for the distribution of large scale structure, enabling efficient gradient-based inference of cosmological parameters and astrophysical processes. A key aspect of this work involves building emulator-based inference pipelines for complex cosmological subgrid models, effectively transforming opaque simulation components into interpretable and statistically robust modules.

Beyond cosmology, my contributions extend to developing robust probabilistic neural network-based reduced-order surrogates for complex fluid flows. These models are capable of accurately capturing turbulent dynamics and enabling efficient analysis in engineering applications. I have advanced methods for the latent-space time evolution of non-intrusive reduced-order models, leveraging Gaussian process emulation to model system dynamics efficiently and accurately. Furthermore, my work has explored the use of probabilistic neural networks not only for surrogate modeling but also for data recovery in fluid flow scenarios, enhancing the utility of sparse or incomplete observational data. Throughout these efforts, a consistent theme is the integration of probabilistic frameworks to provide robust uncertainty quantification alongside predictions, moving beyond point estimates to provide a comprehensive understanding of model reliability.

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
