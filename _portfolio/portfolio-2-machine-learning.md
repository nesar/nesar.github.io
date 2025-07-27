---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The application of machine learning (ML) has emerged as a profoundly transformative force across numerous scientific disciplines, particularly in fields like astrophysics and high-energy physics, which are characterized by vast, complex, and high-dimensional datasets. ML techniques offer powerful capabilities for extracting subtle patterns, predicting system behaviors, and automating laborious tasks that are often beyond the scope of traditional analytical methods. This interdisciplinary research area focuses on leveraging advanced computational paradigms to accelerate discovery and enhance understanding of fundamental scientific phenomena.

Key challenges addressed by ML in science include the efficient processing and interpretation of observational and simulated data, the robust identification of rare events or anomalies, and the development of physically informed models capable of producing actionable insights. Common methodologies involve deep learning architectures, such as convolutional neural networks for image analysis, generative adversarial networks for data synthesis and anomaly detection, and advanced unsupervised techniques for pattern recognition. A critical focus remains on ensuring that these AI models are not only accurate but also interpretable, providing transparent and quantifiable insights that build trust and facilitate scientific validation.

My research significantly contributes to these areas by developing and applying novel machine learning methodologies to address pressing scientific questions. A core focus has been on enhancing the interpretability and utility of generative models for scientific applications. For instance, I have developed methods to create statistically disentangled latent spaces in generative models, guided by underlying physical factors, which improves the interpretability of complex scientific datasets. This work extends to developing and applying generative adversarial networks for robust anomaly detection in astronomical images, ensuring that rare or unexpected astrophysical phenomena can be efficiently identified. Furthermore, I have explored the physical benchmarking of AI-generated cosmic web structures, validating the scientific fidelity of synthesized data.

Beyond generative modeling, my contributions span a wide range of deep learning applications for scientific discovery. I have developed neural network-based solutions for critical tasks such as Point Spread Function deconvolution in astronomical images and estimating peculiar velocities from the Kinetic Sunyaev-Zel'dovich effect, significantly improving observational data analysis. My work also includes machine learning synthetic spectra for probabilistic redshift estimation (SYTH-Z) and developing a modular deep learning pipeline for detecting and modeling galaxy-scale strong gravitational lenses, accelerating the analysis of vast astronomical surveys. To deepen our understanding of cosmic structures, I have explored galaxy morphology using unsupervised machine learning, moving "Beyond the Hubble Sequence." Crucially, my research also addresses the critical need for robust AI models by focusing on interpretable uncertainty quantification in AI for High Energy Physics and developing differentiable predictions for large-scale structure with SHAMNet, integrating physical constraints directly into the models. Additionally, I have explored novel approaches like Voronoi tessellation-assisted deep learning for global field reconstruction from sparse sensors.

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
