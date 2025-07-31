---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific inquiry in complex systems, ranging from astrophysical phenomena to fluid dynamics, often confronts computational bottlenecks. High-fidelity simulations, while crucial for capturing intricate physics, can be prohibitively time-consuming, hindering extensive parameter exploration, uncertainty quantification, and real-time analysis. This challenge necessitates the development of sophisticated methodologies for "Emulation & Inference," which aim to create rapid, accurate, and robust surrogate models (emulators) that can mimic complex simulations, thereby enabling efficient parameter estimation and discovery from observational data.

The core of emulation involves leveraging advanced machine learning and statistical techniques to learn the input-output relationships of a complex system, providing predictions orders of magnitude faster than direct simulation. Inference, conversely, utilizes these emulators to extract meaningful parameters and insights from high-dimensional datasets, often accompanied by significant uncertainties. Key challenges in this domain include maintaining predictive accuracy across vast parameter spaces, quantifying and interpreting model uncertainties, and developing differentiable models that can be seamlessly integrated into optimization and inverse problem frameworks. Applications span across various scientific disciplines, where accurate and rapid predictions are paramount for understanding fundamental processes and making reliable forecasts.

My research directly addresses these computational and inferential challenges, focusing on developing cutting-edge machine learning and probabilistic modeling frameworks for scientific emulation and inference. I have pioneered the creation of highly efficient emulators for computationally intensive simulations, such as the "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" and "Differentiable Predictions for Large Scale Structure with SHAMNet," enabling rapid exploration of complex cosmological models. Beyond cosmology, my work extends to complex fluid dynamics, where I have developed "Probabilistic neural network-based reduced-order surrogate for fluid flows" and explored "Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation," significantly accelerating the simulation and analysis of intricate flow patterns. These contributions demonstrate a commitment to building fast, accurate, and versatile surrogate models across diverse scientific domains.

A central theme throughout my work is the rigorous quantification and interpretability of uncertainty, critical for trustworthy scientific discovery. I have developed novel approaches such as "Interpretable Uncertainty Quantification in AI for HEP" and integrated "Probabilistic neural networks for fluid flow surrogate modeling and data recovery," ensuring that model predictions come with well-calibrated confidence estimates. Furthermore, I have applied these methodologies to specific inference problems, including "Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" and "Peculiar Velocity Estimation from Kinetic SZ Effect using Deep Neural Networks," enhancing the precision and reliability of astrophysical measurements. My work also includes optimizing data utilization for improved inference, as demonstrated in "Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" and "Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field." Cumulatively, my contributions facilitate accelerated scientific discovery, enable robust data interpretation, and provide reliable, quantifiable predictions in high-stakes scientific applications.

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
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Interpretable Uncertainty Quantification in AI for HEP" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Interpretable Uncertainty Quantification in AI for HEP</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
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
