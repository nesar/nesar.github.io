---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The field of scientific discovery is increasingly reliant on complex numerical simulations across disciplines such as astrophysics, cosmology, and fluid dynamics. While these simulations provide invaluable insights, they are often computationally prohibitive, demanding significant resources and time to execute. This computational burden severely limits the ability of researchers to thoroughly explore vast parameter spaces, perform robust uncertainty quantification, or conduct real-time inference from observational data, thereby slowing the pace of scientific progress.

To overcome these challenges, machine learning (ML) has emerged as a transformative paradigm, particularly through the development of emulators and surrogate models. These data-driven models are designed to learn the input-output relationships of complex simulations, providing fast, accurate approximations that can be queried orders of magnitude faster than the original code. This acceleration enables comprehensive exploration of high-dimensional parameter spaces, facilitates Bayesian inference, and allows for the integration of theoretical models with observational data on unprecedented timescales, opening new avenues for discovery.

My research extensively leverages advanced machine learning techniques, including deep neural networks and Gaussian processes, to develop sophisticated emulation and inference frameworks. I have focused on creating surrogate models that not only provide rapid predictions but also rigorously quantify uncertainty, a critical aspect for scientific applications. For instance, I developed methods for "Differentiable Predictions for Large Scale Structure with SHAMNet," providing a differentiable emulator for subhalo abundance matching, and contributed to "Emulator-Based Inference of Cosmological Subgrid Models" to accelerate the exploration of complex astrophysical processes. My work also includes a "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies," enabling efficient exploration of alternative gravity theories.

A core aspect of my methodology involves the development of probabilistic neural networks and Gaussian process emulators, as demonstrated in "Probabilistic neural network-based reduced-order surrogate for fluid flows" and "Probabilistic neural networks for fluid flow surrogate modeling and data recovery." These methods are crucial for robust uncertainty quantification and for constructing non-intrusive reduced-order models, as explored in "Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation." Furthermore, I have applied these techniques to critical astrophysical problems such as "Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" and "Peculiar Velocity Estimation from Kinetic SZ Effect using Deep Neural Networks." Through these contributions, my work significantly accelerates scientific discovery, makes previously intractable inference problems feasible, and provides robust tools for understanding complex physical phenomena in cosmology and fluid dynamics.

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
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
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
