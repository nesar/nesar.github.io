---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning (ML) has emerged as a transformative force in scientific research, offering powerful tools to navigate the ever-increasing complexity and volume of data generated across diverse disciplines. From astrophysics and materials science to engineering and environmental monitoring, ML algorithms are enabling unprecedented insights, accelerating discovery, and automating intricate analysis tasks. This paradigm shift empowers scientists to move beyond traditional hypothesis testing, exploring intricate patterns, predicting novel phenomena, and making data-driven decisions that were previously intractable.

A key focus within this interdisciplinary field involves developing and deploying ML solutions tailored to specific scientific challenges. These often include addressing data sparsity, high dimensionality, noise, and the critical need for model interpretability. Advanced techniques are employed for tasks such as identifying rare anomalies, disentangling complex latent factors, reconstructing global fields from sparse sensor measurements, and effectively leveraging vast, unstructured data archives. The effective application of ML in science thus requires not only robust algorithmic development but also a deep understanding of the scientific context and the unique characteristics of scientific datasets.

My research extensively explores the application and development of advanced machine learning methodologies to address critical problems in scientific domains, particularly within astronomy and engineering. I have developed and applied deep learning techniques, including Convolutional Neural Networks, for complex astronomical image analysis tasks such as accurate Point Spread Function deconvolution and the automated detection and modeling of galaxy-scale strong gravitational lenses. Furthermore, I have pioneered the use of Generative Adversarial Networks (GANs) for anomaly detection in large astronomical image datasets, enabling the discovery of unusual cosmic objects and exploring galaxy morphology beyond traditional classification schemes through unsupervised machine learning.

Beyond image analysis, my work encompasses diverse applications and methodologies. I have contributed to multi-task modeling for engineering applications with sparse data, and implemented probabilistic modeling combined with automated machine learning (AutoML) frameworks for analyzing high-dimensional stress fields. To enhance interpretability in generative models, I have developed methods for statistically disentangled latent spaces guided by generative factors in scientific datasets. My research also includes novel approaches for global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning, reducing model error in weak lensing cluster mass estimation through optimized galaxy selection, and predicting new scientific concept-object associations by mining the literature, thereby significantly advancing scientific understanding and discovery.

<div class="research-figures">
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
