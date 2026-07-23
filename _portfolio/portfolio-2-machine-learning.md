---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine Learning (ML) has emerged as a transformative paradigm across diverse scientific disciplines, offering powerful tools to tackle grand challenges in data-rich fields like astrophysics, cosmology, and engineering. Scientific datasets often present unique complexities, including high dimensionality, sparsity, noise, and the critical need for robust interpretation, making them ideal targets for advanced ML methodologies.

Within this landscape, ML addresses critical needs such as efficient anomaly detection in vast astronomical surveys, the reconstruction of intricate physical fields from limited sensor data, and the systematic exploration of complex data spaces. It facilitates intelligent systems that sift through scientific literature, guide experimental design, and provide insights into underlying physics. A significant focus also lies in developing ML models that are not only accurate but also interpretable, ensuring their adoption and trustworthiness within the scientific community, especially for generative models or large-scale collaborations requiring rigorous validation.

My research significantly advances ML applications across scientific frontiers through novel methodologies. I have pioneered multi-task modeling for sparse engineering data and utilized generative adversarial networks (GANs) for anomaly detection in astronomical images, including Hyper Suprime-Cam galaxy data. Furthermore, I developed modular deep learning pipelines for galaxy-scale strong gravitational lens detection and modeling, alongside neural network-based point spread function deconvolution. A key focus has been on enhancing interpretability, contributing to techniques for creating statistically disentangled latent spaces in generative models, guided by generative factors in scientific datasets. My work also includes novel data reconstruction, employing Voronoi tessellation-assisted deep learning for global field reconstruction from sparse sensors.

In cosmology and astrophysics, I have contributed to benchmarking AI-evolved cosmological structure formation and developed methodologies for evaluating AI models as scientific research assistants, exemplified by EAIRA. Recognizing the scale of modern astronomical projects, I explored opportunities for AI/ML within collaborations like the Rubin LSST Dark Energy Science Collaboration, developing intelligent assistants such as InferA to navigate complex ensemble data. My research also leverages ML for discovery, including predicting new concept-object associations in astronomy by mining literature and exploring galaxy morphology beyond the Hubble Sequence using unsupervised ML. These contributions collectively advance AI in scientific discovery, enabling more efficient and accurate data analysis, fostering new exploration, and ensuring the reliability and interpretability of ML-driven scientific insights.

<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>

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
