---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The exploration and understanding of complex physical systems, from the evolution of the cosmos to the intricacies of fluid dynamics, heavily rely on high-fidelity numerical simulations. However, these simulations are often computationally expensive, posing significant challenges for comprehensive parameter exploration, robust uncertainty quantification, and real-time analysis. The development of efficient and accurate surrogate models, or "emulators," has thus become a critical area of research, enabling orders of magnitude speedup in predictive capabilities while maintaining scientific rigor.

The core challenge lies in constructing these emulators to not only mimic the output of complex simulations but also to provide reliable estimates of their predictive uncertainties. This is essential for robust scientific inference, allowing researchers to confidently constrain model parameters, validate theories against observational data, and accelerate the discovery process across disciplines. Advanced machine learning techniques, particularly those capable of learning high-dimensional, non-linear relationships and inherently quantifying uncertainty, are at the forefront of addressing these demanding requirements.

My research extensively leverages advanced machine learning methodologies, including probabilistic neural networks and Gaussian process emulation, to develop high-fidelity and computationally efficient surrogate models and inference frameworks. I have focused on creating differentiable prediction models, such as SHAMNet for large-scale structure, to enable end-to-end differentiable inference of cosmological parameters and subgrid physics. My work also includes the development of probabilistic neural networks for reduced-order surrogate modeling in complex fluid flows, allowing for both efficient prediction and robust uncertainty quantification, and extending to latent-space time evolution using Gaussian processes to capture dynamic system behavior.

I have developed and applied these techniques to diverse scientific problems, ranging from precise cosmological parameter inference, including emulators for f(R) modified gravity cosmologies and AI for High Energy Physics, to accelerating astrophysical data analysis, such as probabilistic redshift estimation from synthetic spectra (SYTH-Z). Furthermore, my contributions extend to developing novel approaches for data recovery and robust uncertainty quantification in fluid dynamics using probabilistic neural networks. These efforts provide critical tools for accelerating scientific discovery, making previously intractable analyses feasible, and ensuring reliable, interpretable predictions across the physical sciences.

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
