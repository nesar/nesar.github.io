---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning (ML) has emerged as a transformative force in scientific discovery, offering powerful tools to navigate the increasing complexity and volume of data across diverse fields, from astrophysics and cosmology to materials science and engineering. This paradigm shift enables researchers to extract insights, automate intricate analyses, and develop predictive models that push the boundaries of traditional scientific inquiry. The integration of ML facilitates breakthroughs in understanding fundamental physical processes, accelerating the discovery of novel phenomena, and optimizing experimental design and data interpretation.

However, applying ML in scientific contexts often presents unique challenges that demand specialized approaches. These include dealing with sparse or high-dimensional datasets, ensuring physical consistency of models, quantifying uncertainty reliably, enhancing model interpretability for scientific validation, and detecting subtle anomalies that might signify new discoveries. Developing robust, accurate, and trustworthy ML solutions tailored for scientific data—which frequently possess complex underlying structures and noise characteristics—is paramount for realizing the full potential of artificial intelligence in advancing scientific knowledge.

My research significantly contributes to developing and applying advanced ML methodologies across diverse scientific domains. I have developed multi-task modeling techniques to tackle engineering applications with sparse data, and implemented probabilistic modeling frameworks for high-dimensional stress fields, demonstrating robust solutions for complex industrial problems. In astronomy and cosmology, my work spans deep learning solutions for intricate tasks such as strong gravitational lens detection and modeling, deconvolution of point spread functions, and the estimation of peculiar velocities from the kinetic Sunyaev-Zel'dovich effect using neural networks. Furthermore, I have pioneered the use of generative adversarial networks (GANs) for anomaly detection in Hyper Suprime-Cam galaxy images, explored unsupervised machine learning to move 'Beyond the Hubble Sequence' in galaxy morphology studies, and developed a machine learning synthetic spectra approach (SYTH-Z) for probabilistic redshift estimation. My work also addresses opportunities for AI/ML in large-scale endeavors like the Rubin LSST Dark Energy Science Collaboration, extending to global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning.

A core focus of my contributions lies in enhancing the reliability and interpretability of AI systems in science. I have developed methods for enhancing interpretability in generative modeling through statistically disentangled latent spaces guided by generative factors in scientific datasets. My work also addresses interpretable uncertainty quantification in AI for high-energy physics, crucial for validating scientific findings. In cosmology, I have led efforts in benchmarking AI-evolved cosmological structure formation against physical simulations, and explored techniques for reducing model error through optimized galaxy selection for weak lensing cluster mass estimation. Beyond methodological advancements, I have demonstrated direct scientific impact by identifying Carbon-Enhanced Metal-Poor star candidates from Gaia DR3 spectra and predicting new concept-object associations in astronomy by mining the literature, illustrating the power of ML in accelerating discovery and hypothesis generation.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
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
