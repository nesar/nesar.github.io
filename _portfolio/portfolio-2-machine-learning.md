---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The application of machine learning has become a transformative force across various scientific disciplines, particularly in fields grappling with vast datasets and complex physical phenomena like astrophysics and cosmology. Modern astronomical surveys produce petabytes of data, presenting an unprecedented challenge and opportunity for extracting fundamental scientific insights. Machine learning models are uniquely suited to identify subtle patterns, classify objects, detect anomalies, and reconstruct physical properties from these intricate observations, thereby accelerating discovery and deepening our understanding of the universe. This includes everything from the smallest galactic structures to the largest cosmic webs.

A key focus in this emerging field is developing robust, interpretable, and physically informed machine learning methodologies. The goal is not merely to predict or classify, but to ensure that the models’ outputs are scientifically sound and that their internal workings can be understood and trusted by domain experts. This involves integrating physical principles directly into model architectures, enhancing interpretability of latent spaces, and benchmarking AI-generated data against established physical realities, ultimately bridging the gap between data-driven inference and theoretical understanding.

My research extensively explores the innovative integration of machine learning techniques to address pressing challenges in astrophysics and cosmology. I have developed methods for enhancing interpretability in generative models by guiding latent spaces with known generative factors, crucial for understanding complex scientific datasets. My work includes applying generative adversarial networks (GANs) for anomaly detection in large astronomical image surveys, identifying unusual galaxy morphologies or transient events that deviate from expected patterns, and further exploring galaxy morphology beyond the traditional Hubble sequence using unsupervised machine learning.

Furthermore, I have focused on refining cosmological measurements and simulations. This includes reducing model error in weak lensing cluster mass estimation through optimized galaxy selection and improving large-scale structure predictions with differentiable techniques like SHAMNet. My contributions extend to developing neural network-based methods for point spread function deconvolution in astronomical images, essential for sharper observations, and building a modular deep learning pipeline for the detection and modeling of galaxy-scale strong gravitational lenses, which are vital probes of dark matter. I have also pioneered techniques for global field reconstruction from sparse sensor data using Voronoi tessellation-assisted deep learning and contributed to peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect, offering new insights into cosmic flows. This body of work aims to accelerate scientific discovery, improve the precision of cosmological parameters, and unlock new avenues for exploring the universe.

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
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
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
