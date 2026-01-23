---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The application of machine learning (ML) has become a transformative force across numerous scientific disciplines, offering unprecedented capabilities for data analysis, complex system modeling, and accelerated discovery. In fields ranging from astrophysics and cosmology to high-energy physics and engineering, ML techniques are indispensable for navigating massive datasets, extracting subtle patterns, and making robust predictions. Key challenges in these domains often involve dealing with high-dimensional data, sparse observations, inherent uncertainties, and the critical need for model interpretability and reliability. Researchers are actively developing novel ML methodologies to address these complexities, thereby pushing the boundaries of scientific understanding.

A significant focus within this area involves leveraging advanced deep learning architectures, such as neural networks and generative adversarial networks (GANs), to tackle specific scientific problems. This includes developing tools for automated anomaly detection in large astronomical surveys, reconstructing intricate physical fields from limited sensor data, and generating realistic synthetic data to augment observational studies. Furthermore, the development of intelligent ML frameworks extends to creating smart research assistants that can manage and interpret vast scientific ensembles, enhance data processing pipelines, and accelerate the iterative cycles of scientific inquiry.

My research broadly focuses on the development and application of advanced machine learning techniques to address fundamental questions in science and critical engineering challenges. I have pioneered methodologies that enhance the utility of AI in data-rich scientific environments, focusing on robustness, interpretability, and the ability to operate effectively with imperfect or sparse data. My contributions span a range of technical innovations, including multi-task learning paradigms, sophisticated probabilistic modeling, and the strategic use of deep learning for complex pattern recognition and data synthesis.

I have developed innovative solutions across various domains, such as applying multi-task modeling for engineering applications with sparse data and creating a modular deep learning pipeline for galaxy-scale strong gravitational lens detection and modeling. My work also includes enhancing interpretability in generative modeling by developing statistically disentangled latent spaces guided by generative factors in scientific datasets. Furthermore, I have contributed significantly to astronomical data analysis, including anomaly detection in galaxy images using generative adversarial networks, neural network-based point spread function deconvolution, and developing SYTH-Z for machine learning synthetic spectra for probabilistic redshift estimation. My research also extends to the design of methodologies for evaluating AI models as scientific research assistants (EAIRA) and the creation of tools like InferA for cosmological ensemble data.

Through these contributions, I aim to not only improve the accuracy and efficiency of scientific analysis but also to build trust in AI systems by focusing on interpretable uncertainty quantification, particularly for high-energy physics, and by providing physical benchmarks for AI-generated cosmic web simulations. This work underscores my commitment to advancing the frontier of scientific discovery through responsible and innovative machine learning.

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
