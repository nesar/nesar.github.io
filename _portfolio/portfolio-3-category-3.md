---
title: "Machine Learning Methods & Applications for Science"
excerpt: "Research in machine learning methods & applications for science"
collection: portfolio
---

The integration of machine learning (ML) methodologies has become paramount in accelerating discovery and deepening understanding across diverse scientific disciplines. From the vast datasets of cosmology and astrophysics to the complex simulations of fluid dynamics and high-energy physics, ML offers powerful tools to address challenges such as data sparsity, high dimensionality, noise reduction, and the computational expense of traditional methods. Researchers are increasingly leveraging deep learning, probabilistic modeling, and advanced AI architectures to extract insights, build predictive models, and automate analytical tasks that were once intractable.

These advanced computational techniques span a wide array of applications, including the development of high-fidelity surrogate models for computationally intensive simulations, the precise reconstruction of global fields from limited sensor data, and the crucial task of identifying rare or anomalous events within massive scientific datasets. A critical focus in this scientific integration is also placed on enhancing the interpretability of AI models and quantifying their inherent uncertainties, ensuring that AI-driven insights are not only accurate but also trustworthy and scientifically justifiable.

My research extensively explores the development and application of cutting-edge machine learning techniques to tackle some of the most pressing challenges in scientific data analysis and modeling. I have focused on creating robust and interpretable AI solutions, including the deployment of novel neural network architectures, generative adversarial networks (GANs), and probabilistic models. Specifically, my work has pioneered methods for enhancing interpretability through statistically disentangled latent spaces guided by generative factors, and for providing crucial uncertainty quantification in AI models, particularly in domains like High Energy Physics (HEP). I have also contributed to the development of multi-modal foundation models for complex scientific datasets, such as those found in cosmological simulations, establishing benchmarks for AI-evolved scientific processes.

Through this foundational work, I have delivered impactful applications across multiple scientific domains. In cosmology and astronomy, I have developed smart assistants like InferA for cosmological ensemble data, advanced anomaly detection systems for galaxy images using GANs, and neural network-based point spread function deconvolution for clearer astronomical observations. For fluid dynamics, my contributions include probabilistic neural network-based reduced-order surrogates, latent-space time evolution models using Gaussian process emulation, and global field reconstruction from sparse sensor data leveraging Voronoi tessellation-assisted deep learning. Furthermore, I have applied probabilistic modeling and automated machine learning frameworks to analyze high-dimensional stress fields, demonstrating the versatility of these techniques in engineering and material sciences. My overarching goal is to push the boundaries of scientific discovery by developing advanced, reliable, and interpretable AI tools.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/infera-a-smart-assistant-for-cosmological-ensemble_plot_1_590fdcf1.png" alt="Figure from InferA: A Smart Assistant for Cosmological Ensemble Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: InferA: A Smart Assistant for Cosmological Ensemble Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
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
