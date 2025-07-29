---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

In numerous scientific and engineering disciplines, understanding and predicting the behavior of complex systems often necessitates computationally intensive simulations or analysis of vast, high-dimensional datasets. This challenge has driven the development of advanced computational paradigms, particularly in the realm of emulation and inference. Emulation refers to the creation of fast, accurate surrogate models that mimic the input-output behavior of expensive numerical simulations, enabling rapid exploration of vast parameter spaces, sensitivity analysis, and uncertainty quantification that would otherwise be infeasible.

Complementary to emulation, scientific inference focuses on extracting meaningful insights, parameters, or predictions from observational or simulated data. This often involves navigating noisy, incomplete, or high-dimensional information to robustly determine underlying physical properties or model parameters. The confluence of these two areas, often powered by state-of-the-art machine learning, deep learning, and statistical methods, is transforming the pace and scale of scientific discovery, accelerating research in fields ranging from astrophysics and cosmology to fluid dynamics and materials science.

My research portfolio centers on developing and applying cutting-edge machine learning and probabilistic modeling techniques to overcome the computational bottlenecks and data challenges inherent in complex scientific systems. I have developed and deployed robust emulators for computationally expensive simulations, such as a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, significantly accelerating the exploration of alternative cosmological models. My work extends to differentiable predictions for Large Scale Structure with SHAMNet, enabling faster and more accurate forward modeling crucial for cosmological parameter inference.

A core focus has been the development of probabilistic neural networks (PNNs) for fluid flow surrogate modeling and data recovery, and for constructing reduced-order surrogates that capture complex flow dynamics with high fidelity and quantified uncertainty. Furthermore, I have explored latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, enhancing the predictive power and efficiency of these surrogates. In the realm of astronomical inference, I have contributed to machine learning synthetic spectra for probabilistic redshift estimation (SYTH-Z) and developed deep neural networks for Peculiar Velocity Estimation from the Kinetic SZ Effect, crucial for understanding cosmic flows. My contributions also include applying probabilistic modeling and an automated machine learning framework for high-dimensional stress fields and optimizing galaxy selection for robust weak lensing cluster mass estimation, reducing model error in astrophysical observations.

Through these contributions, my work consistently aims to accelerate scientific discovery by providing robust, efficient, and uncertainty-aware computational tools. By transforming computationally prohibitive simulations into rapid emulators and enabling precise, data-driven inference, my research empowers scientists to explore new frontiers in complex physical systems, from the evolution of the universe to intricate fluid dynamics.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
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
