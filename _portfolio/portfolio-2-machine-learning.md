---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning (ML) has emerged as a transformative paradigm across scientific disciplines, particularly in astronomy, where vast and complex datasets from modern observatories present unprecedented challenges and opportunities. The sheer volume, high dimensionality, and inherent noise of astronomical data often overwhelm traditional analysis methods, necessitating sophisticated computational approaches. ML techniques, ranging from deep learning to unsupervised methods, are proving invaluable for tasks such as identifying faint signals, classifying celestial objects, detecting rare anomalies, and constructing physically meaningful models from observations.

This computational revolution is driving significant advancements in our understanding of the universe, from the dynamics of stellar populations to the evolution of galaxies and the fundamental processes governing extreme cosmic phenomena. By automating and enhancing data analysis pipelines, machine learning allows researchers to extract deeper insights, accelerate discovery, and tackle questions that were previously intractable, thereby expanding the frontiers of astrophysical research.

My research broadly focuses on developing and applying cutting-edge machine learning methodologies to address pressing challenges in astronomy and astrophysics. I have extensively utilized deep learning, particularly Generative Adversarial Networks (GANs) and convolutional neural networks, to improve image quality through neural network-based Point Spread Function deconvolution and to pioneer anomaly detection in large astronomical surveys like Hyper Suprime-Cam galaxy images. These efforts aim to discover novel and unexpected cosmic phenomena that deviate from known classifications.

Beyond anomaly detection, my work extends to comprehensive galaxy morphology studies, where I have employed unsupervised machine learning to explore structures "Beyond the Hubble Sequence," revealing new insights into galaxy classification. I have also developed robust, modular deep learning pipelines for critical tasks such as galaxy-scale strong gravitational lens detection and modeling, which are crucial for probing dark matter and cosmology. Furthermore, I have contributed to enhancing the interpretability of generative models by developing techniques for statistically disentangled latent spaces, ensuring that complex ML models can yield transparent and physically meaningful insights in scientific datasets. My research also touches upon stellar astrophysics, identifying "Carbon-Enhanced Metal-Poor star candidates" from Gaia DR3 spectra and constructing large photometric catalogs of Red Clump stars across the Milky Way. Additionally, I contribute to the broader scientific community by outlining best practices for constructing impactful machine learning research in astronomy.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/carbon-enhanced-metal-poor-star-candidates-from-bp_plot_1_17c64dee.png" alt="Figure from Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3</div>
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
