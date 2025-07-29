---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning (ML) has emerged as a transformative paradigm across diverse scientific disciplines, particularly in fields characterized by vast, complex, and high-dimensional datasets. Its application spans fundamental physics, astronomy, and engineering, offering unprecedented capabilities for data analysis, pattern recognition, and predictive modeling. This interdisciplinary research area focuses on developing and deploying sophisticated computational tools to accelerate scientific discovery, extract hidden insights from observational data, and simulate complex physical phenomena with high fidelity.

A key challenge in modern science is not just data volume, but also interpreting complex models, quantifying their uncertainties, and ensuring physical consistency. ML addresses these by enabling automated feature extraction, classification, regression, and anomaly detection. Techniques range from deep neural networks for image and spectral analysis to generative models for data synthesis and probabilistic frameworks for robust uncertainty quantification. The ultimate goal is to enhance the interpretability and trustworthiness of AI systems in scientific contexts, ensuring ML-driven insights are accurate, transparent, and physically meaningful.

My research significantly contributes to this landscape by developing and applying advanced machine learning methodologies to critical problems in astrophysics, cosmology, and high-energy physics. A core area of my work focuses on enhancing the interpretability and robustness of AI models, particularly through generative approaches. I have developed methods for creating statistically disentangled latent spaces, guided by generative factors, crucial for understanding complex scientific datasets. This is complemented by techniques for interpretable uncertainty quantification in AI, ensuring predictions are transparent and reliable. Furthermore, my work includes anomaly detection in astronomical images, utilizing generative adversarial networks (GANs) to identify unusual celestial objects and phenomena in data like Hyper Suprime-Cam galaxy images.

Beyond interpretability and anomaly detection, my contributions encompass diverse applications from astronomical image analysis to high-dimensional data reconstruction. I have developed a modular deep learning pipeline for galaxy-scale strong gravitational lens detection and modeling, vital for cosmology. My work in astronomical imaging includes neural network based Point Spread Function deconvolution, exploring galaxy morphology with unsupervised learning, and optimizing galaxy selection for weak lensing cluster mass estimation. For spectroscopic data, I developed machine learning synthetic spectra for probabilistic redshift estimation (SYTH-Z) and identified Carbon-Enhanced Metal-Poor star candidates from Gaia DR3. Furthermore, I have applied probabilistic modeling and automated ML for high-dimensional stress field analysis, explored global field reconstruction from sparse sensors, and conducted physical benchmarking for AI-generated cosmic web simulations, alongside peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect. These applications underscore my commitment to advancing scientific understanding through innovative and physically-informed machine learning solutions.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
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
