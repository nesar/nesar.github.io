---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The intersection of machine learning, high-performance computing, and fundamental physics has catalyzed the development of sophisticated surrogate models, often referred to as emulators. These models are crucial for accelerating scientific discovery by providing rapid, yet accurate, predictions for complex physical systems that are otherwise computationally prohibitive to simulate directly. This research area is particularly vital in fields like cosmology, astrophysics, and fluid dynamics, where traditional simulations can take days or weeks on supercomputers, making extensive parameter exploration, real-time inference, or robust uncertainty quantification unfeasible.

The core challenge in this domain lies in constructing models that not only mimic the underlying physics accurately but also robustly quantify the uncertainty associated with their predictions. This uncertainty quantification is paramount for scientific applications, enabling reliable parameter estimation, robust decision-making, and credible hypothesis testing. Methodologies frequently employed include various forms of neural networks, Gaussian processes, and techniques for reduced-order modeling, all tailored to capture the intricate, non-linear dependencies inherent in complex physical phenomena while explicitly propagating uncertainties through the modeling pipeline.

My research significantly contributes to this domain by developing and applying advanced machine learning techniques to address critical challenges in scientific modeling and inference. I have developed novel emulator-based inference frameworks, such as those applied to cosmological subgrid models and f(R) modified gravity cosmologies, drastically reducing the computational cost of exploring vast parameter spaces. For large-scale structure analysis, I introduced SHAMNet for differentiable predictions, enabling gradient-based optimization in complex simulations. In the realm of uncertainty quantification, I pioneered the use of probabilistic neural networks (PNNs) for fluid flow surrogate modeling and data recovery, and for providing interpretable uncertainty in high-energy physics applications.

Furthermore, my work extends to innovative applications across astrophysics and engineering. I have developed machine learning models, like SYTH-Z, for probabilistic redshift estimation from synthetic spectra, and deep neural networks for peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect, enhancing our ability to extract cosmological information from observational data. In fluid dynamics, my contributions include probabilistic neural network-based reduced-order surrogates and latent-space time evolution using Gaussian process emulation, which provide efficient and accurate predictions for complex flow dynamics. Additionally, I have demonstrated methods for reducing model error in weak lensing cluster mass estimation through optimized galaxy selection, showcasing the broad applicability and impact of these data-driven approaches in accelerating scientific understanding and improving the robustness of scientific inference.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/emulator-based-inference-of-cosmological-subgrid-m_plot_1_9c094db3.png" alt="Figure from Emulator-Based Inference of Cosmological Subgrid Models" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Emulator-Based Inference of Cosmological Subgrid Models</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
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
