---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative paradigm across numerous scientific disciplines, offering powerful tools to extract knowledge from increasingly vast and complex datasets. In fields such as astrophysics, cosmology, and high-energy physics, researchers grapple with challenges like high-dimensional data, noisy measurements, and the need for sophisticated models to interpret fundamental phenomena. The application of machine learning techniques facilitates advancements in areas ranging from accelerated data analysis and anomaly detection to the precise characterization of physical systems and the discovery of novel patterns.

Specifically, in astronomical and cosmological research, machine learning is pivotal for addressing a diverse array of inverse problems and data interpretation tasks. This includes the deconvolution of astronomical images to enhance resolution, the automated detection of rare or anomalous events, and the classification and characterization of celestial objects like galaxies and cosmic structures. Furthermore, machine learning models are being developed to reconstruct global physical fields from sparse measurements, quantify uncertainties in complex simulations, and derive cosmological parameters from observational data, thereby pushing the boundaries of our understanding of the universe.

My research centers on developing and applying advanced machine learning methodologies to tackle these critical challenges in science, particularly within astrophysics and cosmology. I have pioneered the use of neural network-based techniques for point spread function deconvolution, significantly enhancing image resolution in astronomical applications. For galaxy analysis, I have developed a modular deep learning pipeline for strong gravitational lens detection and modeling, alongside utilizing unsupervised machine learning to explore galaxy morphology beyond traditional classification schemes. Furthermore, my work extensively involves anomaly detection in large astronomical surveys, employing generative adversarial networks (GANs) to identify novel or unusual objects in Hyper Suprime-Cam galaxy images.

Beyond image processing, I have contributed to developing differentiable prediction frameworks like SHAMNet for large-scale structure, alongside physical benchmarking for AI-generated cosmic webs, improving our ability to simulate and interpret cosmological data. My work also includes probabilistic redshift estimation using machine learning-generated synthetic spectra (SYTH-Z) and peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect using deep neural networks, providing crucial insights into cosmic flows. A core theme of my research is robust data handling and uncertainty quantification; I have developed an automated machine learning framework for high-dimensional stress fields and explored interpretable uncertainty quantification in AI for high-energy physics, ensuring the reliability and transparency of AI-driven scientific discoveries. Additionally, I have developed novel approaches for global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning, showcasing the adaptability of these techniques across diverse scientific domains. These contributions collectively advance our capacity for scientific discovery by enabling more precise measurements, accelerating data analysis, and uncovering previously hidden patterns in complex scientific datasets.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from machine learning synthetic spectra for probabilist" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: machine learning synthetic spectra for probabilist</div>
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
