---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The field of machine learning is rapidly transforming scientific research, offering powerful tools to analyze complex datasets, accelerate simulations, and uncover patterns that are intractable with traditional methods. Across disciplines, researchers are leveraging advanced algorithms, from deep neural networks to generative models and probabilistic frameworks, to address grand challenges in data-rich domains. This includes areas like astrophysics and cosmology, where vast quantities of observational data and complex simulations demand sophisticated analysis for understanding the universe's evolution and contents, as well as engineering, where optimizing systems and predicting material behavior often relies on incomplete or high-dimensional data.

A key focus within this interdisciplinary area is the development of robust, interpretable, and physically informed machine learning models. This involves creating methodologies that can not only make accurate predictions but also provide insights into underlying scientific processes, handle data limitations such as sparsity or high dimensionality, and ensure that AI-driven discoveries are physically consistent and trustworthy. Benchmarking AI-evolved or AI-generated scientific data against physical realities, enhancing the interpretability of complex models, and addressing domain-specific challenges like noise reduction, anomaly detection, and feature extraction are critical for the responsible integration of machine learning into the scientific discovery pipeline.

My research extensively explores the application of machine learning to advance scientific understanding, particularly in astrophysics and engineering. In cosmology and astronomy, I have developed novel deep learning approaches for analyzing large-scale structures, including SHAMNet for differentiable predictions of cosmic structure formation and methodologies for physically benchmarking AI-evolved and AI-generated cosmic webs. My work also encompasses advanced techniques for galaxy characterization, from unsupervised machine learning methods to explore galaxy morphology beyond the traditional Hubble sequence, to a modular deep learning pipeline for robust strong gravitational lens detection and modeling, and SYTH-Z for probabilistic redshift estimation from synthetic spectra. Furthermore, I have focused on enhancing astronomical image analysis through neural networks for point spread function deconvolution and the application of generative adversarial networks for anomaly detection in large surveys like Hyper Suprime-Cam, alongside estimating peculiar velocities from kinetic Sunyaev-Zel'dovich effect data using deep neural networks.

Beyond astronomical applications, my contributions extend to developing robust machine learning solutions for engineering and general scientific challenges. This includes pioneering multi-task modeling approaches tailored for engineering applications with sparse data, and an automated machine learning framework combined with probabilistic modeling for analyzing high-dimensional stress fields. I have also developed innovative deep learning methods, assisted by Voronoi tessellation, for global field reconstruction from sparse sensor data. A central theme across my work is the pursuit of interpretability and trustworthiness in AI, exemplified by my contributions to enhancing interpretability in generative modeling through statistically disentangled latent spaces guided by generative factors in scientific datasets. These efforts collectively aim to not only push the boundaries of predictive modeling but also ensure that machine learning applications in science are transparent, physically consistent, and contribute meaningfully to scientific discovery.

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
