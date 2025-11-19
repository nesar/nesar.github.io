---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The intersection of machine learning and scientific research has emerged as a powerful paradigm, enabling unprecedented capabilities in data analysis, pattern recognition, and hypothesis generation across diverse fields. In astrophysics and cosmology, the exponential growth of observational data from surveys like Gaia and Hyper Suprime-Cam presents both immense opportunities and significant challenges for discovery. Machine learning techniques, particularly deep learning and unsupervised methods, are indispensable for navigating high-dimensional datasets, detecting rare phenomena, and extracting nuanced information from complex scientific simulations and observations.

Current research focuses on developing and deploying advanced algorithms to accelerate scientific progress. This includes leveraging generative models for anomaly detection and data synthesis, employing deep neural networks for image analysis tasks such as point spread function deconvolution and strong gravitational lens identification, and applying unsupervised learning to explore morphological complexities in galaxies. Furthermore, robust methodologies are crucial for benchmarking AI-evolved scientific models, enhancing the interpretability of complex machine learning outputs, and automating analysis of high-dimensional scientific data, thereby pushing the boundaries of scientific understanding from cosmological structure formation to material stress fields.

My research significantly contributes to these frontiers by developing and applying innovative machine learning methodologies across astrophysics, cosmology, and materials science. I have focused on creating robust deep learning pipelines, exemplified by a "Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection and Modeling," which automates the identification and characterization of crucial cosmological probes. A substantial portion of my work involves Generative Adversarial Networks (GANs); I have successfully utilized GANs for "Anomaly Detection in Hyper Suprime-Cam galaxy images" and other astronomical datasets, effectively identifying rare and novel objects. Beyond detection, I have also advanced interpretability in generative modeling by statistically disentangling latent spaces guided by generative factors, making complex models more transparent for scientific insight.

Furthermore, my contributions extend to leveraging unsupervised machine learning to move "Beyond the Hubble Sequence" in "Exploring Galaxy Morphology," revealing new classification schemes. I have also developed neural network-based methods for "Point Spread Function Deconvolution For Astronomical Applications," improving image fidelity. My work encompasses applying probabilistic modeling and automated machine learning for high-dimensional stress field analysis, rigorous benchmarking of "AI-evolved cosmological structure formation," and identifying specific stellar populations like "Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in Gaia DR3." Additionally, I have synthesized best practices in "Constructing Impactful Machine Learning Research for Astronomy," providing a comprehensive framework for robust scientific advancements in this rapidly evolving field.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/carbon-enhanced-metal-poor-star-candidates-from-bp_plot_1_17c64dee.png" alt="Figure from Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3</div>
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
