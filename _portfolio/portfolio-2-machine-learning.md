---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative paradigm across diverse scientific disciplines, offering powerful tools to analyze complex data, accelerate discovery, and model intricate phenomena. In fields such as astrophysics, cosmology, high-energy physics, and engineering, the sheer volume and complexity of data often exceed the capabilities of traditional analytical methods. Machine learning, encompassing deep learning, generative models, and probabilistic frameworks, provides advanced solutions for pattern recognition, prediction, and insight extraction, pushing the boundaries of understanding from fundamental particles to the vast cosmic web.

This rapidly evolving area necessitates the development of robust, interpretable, and uncertainty-aware artificial intelligence models, which are crucial for scientific rigor. Scientists require not only accurate predictions but also a clear understanding of model decisions and the confidence associated with those predictions, especially when dealing with sparse or noisy datasets, or when simulating complex physical processes. Machine learning techniques are thus leveraged to tackle challenges such as anomaly detection, multi-modal data fusion, physical parameter estimation, and the reduction of model errors in observational data, enhancing the reliability and utility of AI in scientific discovery.

My research extensively applies cutting-edge machine learning methodologies to address pressing questions in astrophysics and cosmology. I have developed and utilized deep learning pipelines for tasks such as the detection and modeling of strong gravitational lenses and the deconvolution of point spread functions for astronomical applications. My work extends to understanding cosmic structures, contributing to benchmarking AI-evolved cosmological simulations, developing differentiable predictions for large-scale structure with SHAMNet, and estimating peculiar velocities from the kinetic Sunyaev-Zel'dovich effect. Furthermore, I have explored galaxy morphology using unsupervised machine learning, applied generative adversarial networks for anomaly detection in astronomical images, and advanced stellar analysis through identifying Carbon-Enhanced Metal-Poor star candidates from Gaia data and creating SYTH-Z for probabilistic redshift estimation.

A central theme in my contributions is the emphasis on building interpretable and uncertainty-quantified AI systems, vital for scientific rigor. I have worked on enhancing interpretability in generative modeling by developing statistically disentangled latent spaces guided by generative factors, and on providing interpretable uncertainty quantification in AI for High Energy Physics. My research also focuses on improving model reliability, such as reducing model error using optimized galaxy selection for weak lensing cluster mass estimation and through physical benchmarking for AI-generated cosmic web. Beyond astronomy, I have applied these principles to engineering applications, including multi-task modeling for sparse data and leveraging probabilistic modeling for high-dimensional stress fields. Additionally, I have developed techniques for global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning, showcasing the broad applicability of these advanced machine learning paradigms.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/multi-task-modeling-for-engineering-applications-w_plot_1_30afceb7.png" alt="Figure from Multi-task Modeling for Engineering Applications with Sparse Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-task Modeling for Engineering Applications with Sparse Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
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
