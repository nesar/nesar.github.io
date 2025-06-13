---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science <br/><img src='/images/research_machine-learning.png'>"
collection: portfolio
---

Applying machine learning techniques to astronomical problems, including neural networks for data analysis, generative models, and anomaly detection in scientific datasets.

## Research Figures

<div class="research-figures-grid">
  <div class="research-figure">
    <img src="/images/research/figures/anomaly_detection_in_astronomical_images_with_gene_page1_fig2_bf9df594.png" alt="Figure from Anomaly detection in astronomical images with generative adversarial networks" onclick="openModal(this)">
    <p class="figure-caption">From: Anomaly detection in astronomical images with generative adversarial networks</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/modular_deep_learning_analysis_of_galaxy-scale_str_page9_fig2_c3a26812.png" alt="Figure from Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images" onclick="openModal(this)">
    <p class="figure-caption">From: Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images</p>
  </div>
</div>

<style>
.research-figures-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.research-figure {
  text-align: center;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  transition: transform 0.2s ease;
}

.research-figure:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.research-figure img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.research-figure img:hover {
  opacity: 0.9;
}

.figure-caption {
  font-size: 0.85em;
  color: #6c757d;
  margin-top: 0.5rem;
  line-height: 1.3;
}

/* Modal styles */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  padding-top: 5%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}
</style>

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

// Close modal when clicking outside the image
window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}
</script>

## Related Publications:

- **Deconvolution of Astronomical Images with Deep Neural Networks** (2025) - Preprint
- **Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing
  Cluster Mass Estimation** (2024) - Preprint
- **Efficient mapping between void shapes and stress fields using deep convolutional neural networks with sparse data** (2024) - Journal of Computing and Information Science in Engineering
- **Enhancing Interpretability in Generative Modeling: Disentangled Latent Spaces in Scientific Datasets** (2024) - Authorea Preprints
- **Scalable Probabilistic Modeling and Machine Learning With Dimensionality Reduction for Expensive High-Dimensional Problems** (2023) - Preprint
- **Neural Network Based Point Spread Function Deconvolution For
  Astronomical Applications** (2022) - Preprint
- **Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z** (2022) - Monthly Notices of the Royal Astronomical Society
- **Peculiar Velocity Estimation from Kinetic SZ Effect using Deep Neural Networks** (2021) - Monthly Notices of the Royal Astronomical Society (2021)
- **Weak Lensing: Optimal Separation of Scales** (2021) - Preprint
- **Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks** (2021) - Monthly Notices of the Royal Astronomical Society
- **Beyond the hubble sequence–exploring galaxy morphology with unsupervised machine learning** (2021) - Monthly Notices of the Royal Astronomical Society
- **A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection and Modeling** (2020)
- **Anomaly detection in astronomical images with generative adversarial networks** (2020) - arXiv preprint arXiv:2012.08082
- **Unstructured fluid flow data recovery using machine learning and Voronoi diagrams** (2020) - APS Division of Fluid Dynamics Meeting Abstracts
- **Generative networks for emulating synthetic sky images** (2019) - Technical report, Kavli Summer Program in Astrophysics
- **Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images** (2019) - ArXiv
- **Cosmological analysis pipelines through Neural Networks** (2018) - APS April Meeting Abstracts
