---
title: "Machine Learning for Astronomical Data Analysis"
excerpt: "Research in machine learning for astronomical data analysis"
collection: portfolio
---

The field of astronomy is undergoing a data revolution, with modern observatories generating unprecedented volumes of complex information, from deep-field images to vast spectroscopic surveys and high-resolution cosmological simulations. Extracting meaningful scientific insights from these colossal datasets presents significant computational and analytical challenges. Machine learning (ML) and deep learning (DL) techniques have emerged as transformative tools, offering powerful solutions for automating data processing, enhancing signal detection, and enabling novel discoveries.

These advanced computational methods are increasingly indispensable across diverse astronomical domains. They are applied to unravel the mysteries of large-scale structure formation, classify galaxy morphologies, identify rare cosmic phenomena, and refine the precision of astrophysical parameter estimations. From improving the quality of observational data through sophisticated image processing to accelerating the analysis of intricate cosmological simulations, ML and DL are at the forefront of pushing the boundaries of astronomical research.

My research lies at the intersection of machine learning and astronomical data analysis, where I develop and apply cutting-edge AI methodologies to address some of the most pressing questions in astrophysics and cosmology. I have leveraged deep neural networks for critical tasks such as accurately estimating peculiar velocities from the kinetic Sunyaev-Zel'dovich effect, and for robustly deconvolving point spread functions to enhance the clarity of astronomical images. A key focus of my work involves pioneering anomaly detection techniques using Generative Adversarial Networks (GANs) to discover rare and unexpected objects in large observational datasets, exemplified by my contributions to identifying anomalies in Hyper Suprime-Cam galaxy images. Furthermore, I have developed modular deep learning pipelines for the efficient detection and precise modeling of galaxy-scale strong gravitational lenses, offering new avenues for probing dark matter distributions and cosmological parameters.

My contributions also encompass exploring galaxy morphology beyond traditional classifications through unsupervised machine learning, uncovering new insights into galaxy evolution. I developed SYTH-Z, a novel approach utilizing machine learning for generating synthetic spectra for probabilistic redshift estimation, significantly improving accuracy and efficiency in large spectroscopic surveys. More recently, I have been at the forefront of developing advanced AI models for cosmological data, including the creation of multi-modal foundation models designed for comprehensive analysis of complex cosmological simulation data. This work also includes benchmarking AI-evolved models for cosmological structure formation, advancing our understanding of the universe's evolution. My efforts consistently aim to reduce model error, such as through optimized galaxy selection for weak lensing cluster mass estimation, ensuring high-fidelity scientific outcomes from the era of big astronomical data.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
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
