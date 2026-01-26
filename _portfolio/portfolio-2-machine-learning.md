---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The application of machine learning (ML) is rapidly transforming scientific research, offering powerful tools to tackle complex challenges across diverse domains. In particular, astrophysics and cosmology generate vast and intricate datasets from telescopes and simulations, presenting unique opportunities and demands for advanced analytical techniques. This field focuses on developing and deploying cutting-edge ML methodologies to extract insights, accelerate discovery, and enhance our understanding of the universe, from the smallest celestial objects to the large-scale structure of the cosmos.

Key challenges in scientific data analysis include managing high-dimensional, often sparse data, ensuring model interpretability, robustly estimating physical parameters, and identifying subtle patterns or anomalies. To address these, researchers leverage a spectrum of ML paradigms, including deep learning, generative adversarial networks (GANs), multi-task learning, and probabilistic modeling. These techniques enable improved data processing, such as point spread function deconvolution for astronomical images, the generation of physically consistent synthetic data, and sophisticated anomaly detection crucial for discovering rare phenomena.

My research significantly contributes to this evolving landscape by developing and applying novel machine learning approaches to solve pressing problems in astrophysics, cosmology, and related engineering fields. I have focused on creating robust and interpretable models for complex scientific datasets. For instance, my work includes developing neural network architectures for essential astronomical tasks like point spread function deconvolution and the detection and modeling of galaxy-scale strong gravitational lenses, crucial for understanding dark matter and cosmic expansion. I have also advanced generative adversarial networks for anomaly detection in large astronomical surveys, identifying rare celestial objects, and for generating physically consistent cosmic web simulations, which are benchmarked against traditional N-body simulations to ensure scientific accuracy.

Furthermore, I have developed methods to enhance interpretability in generative models by guiding latent spaces with generative factors, and I’ve employed probabilistic modeling for more robust redshift estimation (SYTH-Z) and for optimizing galaxy selection in weak lensing cluster mass estimation to reduce model error. My contributions extend to tackling sparse data challenges through multi-task modeling for engineering applications and global field reconstruction with Voronoi tessellation-assisted deep learning. I have also explored the use of unsupervised machine learning to explore galaxy morphology beyond the Hubble Sequence, providing new insights into galaxy evolution, and developed frameworks for high-dimensional stress field analysis, demonstrating the versatility of these ML approaches across scientific disciplines.

<div class="research-figures">
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
