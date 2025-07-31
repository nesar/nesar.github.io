---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative paradigm across various scientific disciplines, offering powerful tools to tackle complex data analysis, model intricate phenomena, and accelerate discovery. In fields like astrophysics and cosmology, the sheer volume and complexity of observational and simulated data present significant challenges for traditional analytical methods. Machine learning, particularly deep learning, provides innovative solutions for tasks such as identifying subtle patterns, reconstructing physical fields, detecting rare events, and interpreting high-dimensional datasets. Its application enables scientists to extract deeper insights, enhance the efficiency of data processing, and push the boundaries of current understanding.

The integration of machine learning techniques facilitates advancements in areas ranging from image processing and anomaly detection to the generation of synthetic data and the unsupervised exploration of morphological spaces. For instance, neural networks can be meticulously designed to address inverse problems like deconvolution or to reconstruct global fields from sparse measurements. Generative models, such as Generative Adversarial Networks (GANs), prove invaluable for learning complex data distributions, enabling robust anomaly detection, and creating realistic simulations. Furthermore, unsupervised learning methods allow for unbiased exploration of data characteristics, revealing new classifications and relationships previously obscured by predefined categories.

My research delves into the cutting-edge application of machine learning to address fundamental challenges in scientific discovery, primarily within astrophysics and cosmology. I have developed novel methodologies leveraging deep learning and generative models to enhance interpretability, improve data analysis, and automate complex scientific workflows. For example, my work includes enhancing interpretability in generative modeling by developing statistically disentangled latent spaces guided by generative factors, which is crucial for understanding the underlying physics in scientific datasets. I have also pioneered the use of neural networks for Point Spread Function (PSF) deconvolution in astronomical applications, significantly improving image quality and analytical precision.

Furthermore, my contributions extend to developing robust anomaly detection systems, utilizing Generative Adversarial Networks (GANs) for identifying unusual objects in large astronomical image surveys like Hyper Suprime-Cam galaxy images, and applying these to general astronomical images. I have explored new frontiers in galaxy morphology, moving "Beyond the Hubble Sequence" by employing unsupervised machine learning to uncover novel classifications. My work also encompasses the development of a modular deep learning pipeline for automated galaxy-scale strong gravitational lens detection and modeling, streamlining critical astrophysical analyses. Additionally, I have contributed to global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning and initiated physical benchmarking for AI-generated cosmic web simulations, ensuring their scientific validity. These efforts collectively aim to accelerate scientific understanding, improve data interpretation, and unlock new avenues for discovery.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/physical-benchmarking-for-ai-generated-cosmic-web_plot_1_11f44910.png" alt="Figure from Physical Benchmarking for AI-Generated Cosmic Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Physical Benchmarking for AI-Generated Cosmic Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/anomaly-detection-in-hyper-suprime-cam-galaxy-imag_plot_1_58355288.png" alt="Figure from Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks</div>
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
