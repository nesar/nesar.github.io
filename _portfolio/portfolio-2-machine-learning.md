---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning (ML) and artificial intelligence (AI) are rapidly transforming the landscape of scientific discovery, offering unprecedented capabilities to analyze vast and complex datasets generated across disciplines. From astrophysics to materials science and particle physics, these computational tools enable researchers to uncover hidden patterns, accelerate simulations, and make predictions with increasing accuracy. This paradigm shift is particularly crucial in fields grappling with data deluge, where traditional analytical methods often fall short in extracting subtle signals or recognizing novel phenomena.

The application of AI/ML in scientific research, however, presents unique challenges, demanding robust methodologies that account for data sparsity, high dimensionality, and the imperative for interpretability and uncertainty quantification. Scientific applications often require models that are not only predictive but also provide insights into the underlying physical processes, ensuring trustworthiness and enabling scientific discovery. Developing AI systems that can effectively learn from, and contribute to, the scientific method is therefore a critical area of ongoing research, focusing on enhancing model reliability, generalizability, and the ability to discover the unknown.

My research focuses on developing and applying advanced machine learning techniques to address complex challenges across various scientific domains, particularly in astronomy and cosmology. I have developed deep learning pipelines for analyzing astronomical images, including a modular framework for galaxy-scale strong gravitational lens detection and modeling, and techniques for identifying anomalous galaxy images using generative adversarial networks (GANs) with Hyper Suprime-Cam data. My work extends to characterizing cosmic structures, where I have contributed to benchmarking AI-evolved cosmological structure formation and conducting physical benchmarking for AI-generated cosmic webs, critically evaluating their fidelity. Furthermore, I developed neural network-based point spread function deconvolution and SYTH-Z, a machine learning approach using synthetic spectra for probabilistic redshift estimation. I also explored unsupervised machine learning to move "Beyond the Hubble Sequence" in understanding galaxy morphology and identified Carbon-Enhanced Metal-Poor star candidates from Gaia DR3 spectra.

Beyond astrophysical applications, my contributions include enhancing the interpretability and reliability of AI models more broadly. I have advanced methods for enhancing interpretability in generative modeling by creating statistically disentangled latent spaces guided by generative factors in scientific datasets, crucial for understanding model decisions. My work on interpretable uncertainty quantification in AI for high-energy physics ensures that scientific conclusions drawn from AI models are robust and transparent. I have also applied multi-task modeling for sparse engineering data and probabilistic modeling with automated machine learning frameworks to tackle high-dimensional stress fields. Additionally, I have explored global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning. Collectively, my research aims to build robust, interpretable, and efficient machine learning tools that accelerate scientific discovery and deepen our understanding of complex systems.

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
