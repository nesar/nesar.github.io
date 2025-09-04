---
title: "Astronomical Image & Spectral Analysis with AI"
excerpt: "Research in astronomical image & spectral analysis with ai"
collection: portfolio
---

Astronomical observations, increasingly vast and complex, generate immense datasets from ground-based and space-borne telescopes. Analyzing these intricate images and spectra is fundamental to understanding the universe, from probing galaxy evolution and cosmology to discovering transient phenomena. However, challenges persist in extracting meaningful information, including instrumental noise, atmospheric blurring, and the sheer scale and dimensionality of the data, which often obscure subtle features or rare events, demanding advanced analytical tools.

The advent of artificial intelligence (AI), particularly machine learning (ML) and deep learning, offers powerful new paradigms to overcome these analytical hurdles. AI-driven techniques excel at identifying complex relationships, performing classification, and generating insights from large, noisy datasets, making them invaluable tools for modern astrophysics. These methodologies are being deployed across various domains, including enhancing image quality, interpreting spectroscopic data, classifying astronomical objects, detecting anomalous events, and modeling intricate astrophysical phenomena such as gravitational lensing.

My research specifically leverages these advanced AI techniques to address critical challenges in astronomical data analysis, enhancing both the quality and interpretability of observational data. I have developed neural network based approaches for point spread function deconvolution, which demonstrably improve image resolution and fidelity. Furthermore, I introduced SYTH-Z, a machine learning framework for generating synthetic spectra, enabling more robust and probabilistic redshift estimations essential for cosmological studies. My work also utilizes generative adversarial networks (GANs) for anomaly detection in astronomical images, effectively identifying unusual galaxy morphologies in datasets like Hyper Suprime-Cam and other unexpected events.

Beyond individual object analysis, my contributions extend to broader structural and evolutionary studies of galaxies. I have developed unsupervised machine learning methods to explore galaxy morphology beyond the traditional Hubble sequence, uncovering novel classifications and revealing underlying astrophysical processes. Moreover, I spearheaded the development of a modular deep learning pipeline specifically designed for the automated detection and detailed modeling of galaxy-scale strong gravitational lenses. This pipeline represents a crucial step towards efficiently processing massive datasets from upcoming surveys, enabling precise measurements of dark matter distributions and refined cosmological parameters. These advancements collectively push the boundaries of our understanding of the universe through more accurate, efficient, and insightful data analysis.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/anomaly-detection-in-hyper-suprime-cam-galaxy-imag_plot_1_58355288.png" alt="Figure from Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/anomaly-detection-in-astronomical-images-with-gene_plot_1_6d84e8fe.png" alt="Figure from Anomaly Detection in Astronomical Images with Generative Adversarial Networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Anomaly Detection in Astronomical Images with Generative Adversarial Networks</div>
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
