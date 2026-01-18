---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning (ML) is rapidly transforming scientific research across diverse disciplines, offering powerful tools to extract knowledge from increasingly vast and complex datasets. From astrophysics to materials science, ML algorithms are being deployed to accelerate discovery, automate laborious tasks, and uncover hidden patterns that are intractable with traditional methods. This involves developing sophisticated models capable of handling high-dimensional data, sparse observations, and the inherent noise and uncertainties prevalent in scientific measurements.

In fields such as astrophysics and cosmology, ML is instrumental in classifying celestial objects, detecting rare phenomena, and reconstructing physical fields. The sheer volume of astronomical survey data, for instance, necessitates automated approaches for tasks like galaxy morphology classification, gravitational lens detection, and anomaly identification. Similarly, in engineering, ML aids in predicting material properties and analyzing high-dimensional sensor data, often under conditions of limited or sparse observations. A key focus within this domain is developing robust, interpretable, and physically informed ML models that can provide insights into underlying scientific principles.

My research lies at the intersection of machine learning and various scientific domains, primarily focusing on astrophysics and engineering applications. I have developed and applied advanced machine learning techniques, including generative adversarial networks (GANs), deep neural networks, probabilistic modeling, and unsupervised learning, to address critical challenges in scientific data analysis. For instance, I have utilized GANs extensively for tasks such as anomaly detection in large astronomical image datasets, exemplified by my work on Hyper Suprime-Cam galaxy images, and for physical benchmarking of AI-generated cosmic web structures, ensuring their fidelity to cosmological principles. A significant part of my methodological contribution involves enhancing the interpretability of generative models by guiding disentangled latent spaces with specific physical factors in scientific datasets.

Furthermore, my work has focused on creating practical and impactful solutions for scientific discovery. In astrophysics, I have developed modular deep learning pipelines for the efficient detection and modeling of galaxy-scale strong gravitational lenses, a crucial tool for cosmology. I have also applied these techniques to classify Carbon-Enhanced Metal-Poor (CEMP) star candidates from Gaia DR3 spectra and explored galaxy morphology beyond the traditional Hubble Sequence using unsupervised machine learning. Beyond astronomy, my contributions extend to engineering, where I have applied probabilistic modeling and automated machine learning frameworks to analyze high-dimensional stress fields and developed multi-task modeling approaches for sparse data applications. Additionally, I have developed techniques for global field reconstruction from sparse sensor data using Voronoi tessellation-assisted deep learning and improved observational data quality through neural network-based Point Spread Function deconvolution. This body of work consistently aims to accelerate scientific discovery, improve data quality, and provide more interpretable and robust insights from complex scientific data.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
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
