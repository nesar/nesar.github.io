---
title: "Scientific Emulation, Inference & Uncertainty Quantification"
excerpt: "Research in scientific emulation, inference & uncertainty quantification"
collection: portfolio
---

Scientific emulation, inference, and uncertainty quantification (UQ) are critical pillars in modern computational science, addressing the challenges posed by increasingly complex and computationally intensive physical models. Across diverse domains, from astrophysics and cosmology to fluid dynamics and high energy physics, researchers frequently encounter models that are too slow to run for extensive parameter exploration, statistical inference, or real-time prediction. This necessitates the development of sophisticated surrogate models, or emulators, capable of accurately mimicking high-fidelity simulations at a fraction of the computational cost.

Beyond mere speed, a crucial aspect of scientific prediction is understanding the reliability of results. Uncertainty quantification provides the rigorous framework to characterize and propagate uncertainties arising from model parameters, observational noise, and inherent model limitations. This involves developing methods to not only produce predictions but also to quantify the confidence in those predictions, often through probabilistic frameworks. Integrating machine learning and advanced statistical techniques into this process allows for the creation of interpretable and robust predictive tools that accelerate scientific discovery and enhance the trustworthiness of data-driven insights. Reduced-order modeling further contributes by simplifying high-dimensional systems, making complex simulations more tractable and amenable to emulation.

My research extensively contributes to this vital field by developing novel methodologies and applications for scientific emulation, inference, and uncertainty quantification. I have focused on leveraging advanced machine learning techniques, particularly neural networks and Gaussian processes, to build efficient and reliable surrogate models for complex scientific phenomena. For instance, I have developed SHAMNet for differentiable predictions of large scale structure, enabling more robust cosmological inference, and created a Matter Power Spectrum Emulator specifically for f(R) Modified Gravity Cosmologies, drastically accelerating predictions in alternative gravity theories. In astrophysics, I designed SYTH-Z, a machine learning approach for generating synthetic spectra and performing probabilistic redshift estimation, alongside methods for reducing model error in weak lensing cluster mass estimation through optimized galaxy selection.

A significant portion of my work is dedicated to integrating robust uncertainty quantification into these emulators and models. I have developed probabilistic neural network (PNN) based reduced-order surrogates for fluid flows, also extending these PNNs for effective data recovery and incorporating Gaussian process emulation for latent-space time evolution in non-intrusive reduced-order models. This allows for both efficient simulation and a clear understanding of predictive uncertainties in dynamic systems. Furthermore, I have focused on making AI models more transparent, exemplified by my work on interpretable uncertainty quantification in AI for High Energy Physics. Collectively, these contributions provide faster, more reliable, and transparent predictive tools, empowering deeper scientific inquiry and enabling breakthroughs in computationally challenging domains.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
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
