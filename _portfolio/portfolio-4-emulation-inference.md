---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The exploration of complex scientific phenomena across fields such as astrophysics, cosmology, and fluid dynamics often relies on computationally intensive simulations. These simulations, while powerful, present significant challenges for efficient parameter space exploration, uncertainty quantification, and real-time analysis. Consequently, the development of sophisticated emulation and inference techniques has become paramount. Emulators, also known as surrogate models or reduced-order models, provide fast, accurate approximations of these complex simulations, enabling rapid exploration of vast parameter spaces and accelerating scientific discovery. Complementary to this, robust inference methodologies are essential for extracting meaningful insights from observational data and simulation outputs, particularly when dealing with inherent uncertainties and high-dimensional parameter spaces.

This research area harnesses the power of advanced machine learning and statistical methods to construct these emulators and perform precise inference. Techniques range from deep neural networks and Gaussian processes to automated machine learning frameworks, all tailored to capture intricate non-linear relationships and provide robust uncertainty estimates. The objective is to transform the landscape of scientific investigation by making cutting-edge simulations more accessible and their outputs more interpretable, thereby pushing the boundaries of what is computationally and analytically feasible in areas ranging from understanding the universe's evolution to designing advanced engineering systems.

My research extensively addresses these challenges, focusing on the development and application of novel machine learning frameworks for high-fidelity emulation and robust probabilistic inference across diverse scientific domains. I have pioneered the creation of efficient surrogate models for computationally expensive simulations, including a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies and an Emulator-Based Inference of Cosmological Subgrid Models, significantly reducing the computational burden while maintaining accuracy. My work also includes probabilistic neural network-based reduced-order surrogates for fluid flows and their latent-space time evolution using Gaussian process emulation, enabling efficient analysis and data recovery for complex dynamic systems. Additionally, I developed SHAMNet for Differentiable Predictions for Large Scale Structure, enhancing our ability to model cosmic structures.

Beyond emulation, my contributions extend to developing sophisticated probabilistic inference techniques to extract knowledge from complex data with quantified uncertainties. This includes the development of SYTH-Z, which employs machine learning synthetic spectra for probabilistic redshift estimation, and a framework for Interpretable Uncertainty Quantification in AI for High Energy Physics (HEP), vital for robust scientific conclusions. I have also applied probabilistic modeling and automated machine learning frameworks to analyze high-dimensional stress fields and developed deep neural networks for Peculiar Velocity Estimation from the Kinetic SZ Effect. Furthermore, my research includes strategies for Reducing Model Error Using Optimised Galaxy Selection for Weak Lensing Cluster Mass Estimation, demonstrating a commitment to improving the precision and reliability of scientific measurements and predictions across astrophysics, cosmology, and engineering.

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
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
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
