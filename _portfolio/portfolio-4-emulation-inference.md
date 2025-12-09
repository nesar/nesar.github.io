---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Computational science and engineering are increasingly reliant on the efficient simulation and analysis of complex physical systems. From turbulent fluid flows and intricate material stress distributions to vast astronomical datasets, these simulations are often computationally prohibitive, demanding novel approaches to accelerate discovery and design. Emulation and inference, powered by advanced machine learning and statistical methodologies, provide a powerful paradigm for overcoming these bottlenecks. This research area focuses on developing data-driven surrogate models that can accurately replicate the behavior of complex systems at a fraction of the computational cost, enabling rapid exploration of design spaces and real-time predictions.

A central theme within this domain is the development of robust and interpretable models that not only predict outcomes but also quantify the uncertainty associated with those predictions. Probabilistic machine learning techniques, including advanced neural networks and Gaussian processes, are fundamental in constructing these sophisticated emulators. These methods allow for the capture of complex nonlinear relationships within high-dimensional data, reducing the dimensionality of intricate systems through techniques like reduced-order modeling, and critically, providing statistically sound measures of confidence in their outputs. Such uncertainty quantification is paramount for reliable decision-making in high-stakes scientific and engineering applications, moving beyond mere point predictions to provide a complete understanding of model limitations and robustness.

My research actively contributes to advancing the field of emulation and inference through the development and application of cutting-edge probabilistic machine learning methodologies. I have focused on creating robust, efficient, and interpretable surrogate models that can accurately represent complex physical phenomena, ranging from fluid dynamics to material science and astrophysics. My work aims to not only accelerate computational simulations but also to provide comprehensive uncertainty quantification, ensuring that model predictions are accompanied by a clear understanding of their reliability and inherent variability. This approach significantly enhances the utility of machine learning in scientific discovery and engineering design.

Specifically, I have developed novel probabilistic neural network (PNN) architectures for reduced-order surrogate modeling of fluid flows, demonstrating their capability for efficient prediction and data recovery. Extending this, I have pioneered methods for latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, effectively capturing complex system dynamics. My work also includes applying probabilistic modeling and automated machine learning frameworks to high-dimensional stress fields, showcasing robustness across engineering challenges. Crucially, I have focused on interpretable uncertainty quantification in high-energy physics (HEP) and astrophysics. This includes SYTH-Z, a machine learning framework for generating synthetic spectra to enable probabilistic redshift estimation, delivering full probability distributions that greatly enhance astrophysical inference. These contributions underscore the versatility and impact of integrating advanced probabilistic machine learning with complex scientific and engineering problems.

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
