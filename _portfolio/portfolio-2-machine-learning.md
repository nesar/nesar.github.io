---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The field of Machine Learning (ML) is fundamentally transforming scientific research by offering unprecedented capabilities for data analysis, pattern discovery, and predictive modeling across disciplines from astrophysics and cosmology to engineering. ML algorithms are invaluable for extracting insights from vast, complex, and often noisy datasets, enabling tasks such as identifying subtle signals, accelerating computationally intensive simulations, and automating the analysis of high-dimensional information. This includes the application of advanced deep learning techniques, such as convolutional neural networks for image analysis, generative adversarial networks for synthetic data generation and anomaly detection, and probabilistic modeling frameworks for quantifying inherent uncertainties, thereby pushing the boundaries of scientific discovery.

Research in Machine Learning for Science actively addresses critical challenges like data sparsity, the need for enhanced model interpretability, and robust uncertainty quantification. By developing sophisticated multi-task learning approaches, methods for global field reconstruction from sparse sensors, and techniques to disentangle latent spaces in generative models, the field aims to create more transparent, reliable, and physically informed AI tools. These advancements are essential for validating ML predictions against established physical laws, ensuring that AI-driven discoveries are both accurate and trustworthy, and ultimately accelerating insights from complex scientific instruments and experiments.

My research contributions lie at the forefront of developing and applying innovative machine learning techniques to tackle complex problems across astrophysics, cosmology, and engineering. I have developed modular deep learning pipelines for critical tasks such as galaxy-scale strong gravitational lens detection and modeling, and neural network-based point spread function deconvolution for astronomical imaging. My work includes leveraging generative adversarial networks for robust anomaly detection in vast astronomical image datasets and for physically benchmarking AI-generated cosmic web structures. Furthermore, I have pioneered multi-task modeling for sparse engineering data and applied probabilistic frameworks for high-dimensional stress fields, alongside uniquely exploring scientific literature mining to predict new concept-object associations in astronomy.

A central theme in my work is the emphasis on interpretability and robust uncertainty quantification within AI models, crucial for scientific trust and discovery. I have developed methods for enhancing interpretability in generative modeling by statistically disentangling latent spaces guided by generative factors, and rigorous frameworks for interpretable uncertainty quantification in high energy physics. My contributions extend to benchmarking AI-evolved cosmological structure formation and developing techniques like SYTH-Z for probabilistic redshift estimation. I have also explored galaxy morphology with unsupervised machine learning and contributed to global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning, directly engaging with large-scale initiatives like the Rubin LSST Dark Energy Science Collaboration.

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
