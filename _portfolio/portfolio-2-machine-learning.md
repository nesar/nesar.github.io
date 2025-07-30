---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a cornerstone technology in scientific research, particularly in fields grappling with vast and complex datasets. Its application enables unprecedented capabilities in data analysis, pattern recognition, anomaly detection, and predictive modeling, pushing the boundaries of discovery across diverse disciplines from material science to astrophysics. The ability of sophisticated algorithms to uncover subtle relationships within data, automate laborious tasks, and even generate novel insights is revolutionizing traditional scientific workflows.

In astronomy and cosmology, the confluence of ever-increasing data volumes from advanced observatories and the complexity of physical phenomena necessitates innovative computational approaches. Machine learning offers powerful tools to address challenges such as classifying celestial objects, estimating astrophysical parameters, identifying rare events, and simulating large-scale cosmic structures. These techniques are crucial for extracting maximum scientific value from petabyte-scale datasets and for developing more accurate and efficient methods for understanding the universe.

My research extensively explores the application of advanced machine learning techniques to address pressing challenges in astrophysics and scientific data analysis. I have developed methodologies to enhance the interpretability of generative models by guiding statistically disentangled latent spaces with known generative factors in scientific datasets, which is critical for ensuring trustworthiness and scientific utility in AI-generated data. For instance, I have designed generative adversarial networks (GANs) for anomaly detection in astronomical images, including those from the Hyper Suprime-Cam survey, enabling the identification of rare or unexpected cosmic phenomena. Furthermore, my work extends to improving the accuracy of astrophysical measurements, such as optimizing galaxy selection for weak lensing cluster mass estimation to significantly reduce model error, and developing neural network-based point spread function deconvolution for clearer astronomical observations.

Beyond individual applications, I have focused on building robust and scalable machine learning pipelines. This includes a modular deep learning pipeline specifically for the automated detection and detailed modeling of galaxy-scale strong gravitational lenses, a crucial tool for cosmology. My research also delves into unsupervised machine learning to explore galaxy morphology beyond traditional classification schemes like the Hubble Sequence, offering new perspectives on galactic evolution. Moreover, I have contributed to physically benchmarking AI-generated cosmic web simulations, ensuring their fidelity and scientific validity against established cosmological models. Collectively, my contributions span interpretability, anomaly detection, physical parameter estimation, and large-scale data processing, aiming to accelerate scientific discovery and enhance our understanding of complex natural phenomena.

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
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/physical-benchmarking-for-ai-generated-cosmic-web_plot_1_11f44910.png" alt="Figure from Physical Benchmarking for AI-Generated Cosmic Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Physical Benchmarking for AI-Generated Cosmic Web</div>
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
