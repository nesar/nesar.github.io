---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine Learning (ML) is revolutionizing scientific research by enabling unprecedented analytical capabilities across vast datasets, from understanding the universe to optimizing engineering processes. In fields like astrophysics and cosmology, ML provides powerful tools for confronting the deluge of data from cutting-edge observatories like the Rubin LSST, facilitating the discovery of subtle patterns, modeling complex phenomena, and deepening our comprehension of cosmic evolution, dark energy, and the structure of the universe. This includes tasks such as robust object detection, morphology classification, parameter estimation, and the simulation of large-scale structures.

A central theme in this scientific ML endeavor involves tackling critical challenges such as data sparsity, high dimensionality, and the inherent need for model interpretability and reliable uncertainty quantification. Addressing these demands necessitates the development of sophisticated techniques, including generative models for synthetic data generation and anomaly detection, advanced deep learning architectures for specific tasks like deconvolution or field reconstruction, and multi-task learning frameworks. These methodologies extend beyond astronomy, finding crucial applications in other scientific and engineering domains, for instance, in the analysis of high-dimensional stress fields with limited experimental data.

My research extensively explores the application of cutting-edge machine learning techniques to accelerate scientific discovery and address fundamental challenges, focusing on enhancing model performance, interpretability, and reliability. I have pioneered the use of generative adversarial networks (GANs) for anomaly detection in astronomical images, crucial for identifying rare phenomena. Furthermore, I have worked on enhancing the interpretability of generative models by creating statistically disentangled latent spaces, guided by generative factors, and established physical benchmarking techniques for evaluating AI-generated cosmic web simulations. I have also focused on robust uncertainty quantification, developing interpretable measures for AI in high-energy physics and integrating probabilistic modeling into automated frameworks for high-dimensional stress field analysis. In astrophysics and cosmology, my work has leveraged deep learning for critical tasks such as neural network-based point spread function deconvolution and global field reconstruction from sparse sensor data using Voronoi tessellation-assisted deep learning. I have also advanced our understanding of the universe through projects like peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect, and developing machine learning synthetic spectra for probabilistic redshift estimation (SYTH-Z). My research includes a modular deep learning pipeline for strong gravitational lens detection and modeling, optimizing galaxy selection for weak lensing cluster mass estimation, and exploring galaxy morphology with unsupervised machine learning. I have also investigated multi-task modeling for engineering applications with sparse data.

Collectively, my work demonstrates a commitment to pushing the boundaries of machine learning for scientific applications, from foundational cosmological questions to practical engineering challenges. I aim to create AI solutions that are not only powerful and accurate but also interpretable, reliable, and capable of quantifying their own uncertainties, thereby fostering greater trust and accelerating the pace of scientific exploration and discovery across diverse scientific disciplines.

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
