---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific discovery across diverse domains, from astrophysics and cosmology to fluid dynamics and materials science, increasingly relies on sophisticated computational models. These models, while powerful, are often computationally expensive, making comprehensive exploration of parameter spaces or real-time inference challenging. The field of emulation and inference addresses these bottlenecks by developing fast, accurate, and statistically robust surrogate models (emulators) that mimic the behavior of complex simulations, alongside advanced techniques for extracting meaningful insights and predictions from noisy or sparse observational data. A critical component of this research area is the robust quantification of uncertainty, which is essential for establishing the credibility of predictions and informing decision-making in scientific contexts.

These challenges necessitate the development of novel machine learning and statistical methodologies. Probabilistic modeling, deep learning, and reduced-order modeling techniques are at the forefront, enabling the construction of high-fidelity surrogates that can predict outcomes orders of magnitude faster than full simulations. Moreover, these methods provide frameworks for propagating uncertainties from input parameters and observational noise through to model predictions, offering a complete statistical picture. The ability to perform rapid inference and quantify uncertainties is pivotal for accelerating scientific research, optimizing experimental design, and facilitating the real-time analysis of large-scale datasets.

My research focuses on pioneering the development and application of advanced machine learning and probabilistic modeling techniques to create robust emulation and inference solutions for complex scientific problems. I have developed high-fidelity surrogate models, including probabilistic neural network-based reduced-order surrogates for fluid flows and a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, significantly accelerating the exploration of vast parameter spaces. My work also extends to latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, showcasing innovative approaches to dynamic system modeling. An emphasis is placed on interpretable Uncertainty Quantification in AI for High Energy Physics and the application of probabilistic modeling with automated machine learning frameworks for high-dimensional stress fields, ensuring that model predictions are not only fast but also reliable and transparent.

Furthermore, I have made significant contributions to advanced inference techniques for extracting critical information from observational data. This includes the development of Peculiar Velocity Estimation from Kinetic SZ Effect using Deep Neural Networks and Machine learning synthetic spectra for probabilistic redshift estimation (SYTH-Z), directly impacting cosmological and astrophysical surveys. My work also addresses global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning, demonstrating innovative methods for data recovery and interpolation in challenging scenarios. Through these efforts, I strive to build sophisticated, data-driven tools that empower scientific discovery by transforming complex, data-intensive tasks into efficient, insightful, and reliable analytical processes.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/global-field-reconstruction-from-sparse-sensors-wi_plot_1_93ef286c.png" alt="Figure from Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning</div>
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
