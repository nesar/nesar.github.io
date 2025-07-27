---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative force in modern scientific research, particularly in data-rich fields like astrophysics, cosmology, and materials science. Its application spans a wide array of challenges, from handling the immense scale and complexity of scientific datasets to uncovering subtle patterns, accelerating complex simulations, automating classification tasks, and identifying rare or anomalous phenomena. The advent of deep learning, coupled with advancements in unsupervised and generative modeling, is enabling researchers to extract deeper insights from high-dimensional data, opening new avenues for fundamental discovery.

A crucial focus within this interdisciplinary domain is the development of robust, interpretable, and physically informed machine learning methodologies. This involves not only achieving high predictive performance but also ensuring that the models provide meaningful scientific insights and adhere to known physical laws. Generative models, for instance, are being leveraged for synthetic data generation, anomaly detection, and enhancing the fidelity of scientific data. Simultaneously, the integration of differentiable programming allows for the seamless incorporation of physical models into machine learning pipelines, while unsupervised learning techniques are invaluable for discovering novel structures, classifications, and rare objects in datasets without prior labeling.

My research extensively explores the application of advanced machine learning techniques to address fundamental challenges in astrophysics and cosmology, with a particular emphasis on developing interpretable and physically informed models. I have developed methods to enhance interpretability in generative modeling by creating statistically disentangled latent spaces, guided by generative factors inherent in scientific datasets. This work, alongside my contributions to anomaly detection in astronomical images using Generative Adversarial Networks (GANs) – notably for Hyper Suprime-Cam galaxy images – enables the efficient identification of rare or unexpected phenomena, crucial for discovery in large-scale surveys.

Furthermore, my work significantly contributes to the realm of cosmological simulations and galaxy characterization. I have developed SHAMNet, a framework for differentiable predictions for Large Scale Structure, which bridges the gap between theoretical models and observational data. Complementary to this, I have engaged in physical benchmarking for AI-generated Cosmic Web structures, ensuring the scientific fidelity of machine learning outputs. My contributions extend to exploring galaxy morphology beyond traditional classification schemes, utilizing unsupervised machine learning to uncover new insights, and developing a modular deep learning pipeline for the robust detection and modeling of galaxy-scale strong gravitational lenses. Additionally, I have applied these techniques to specific astronomical problems, such as identifying Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3, demonstrating the power of machine learning in discovering rare stellar populations.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from machine learning synthetic spectra for probabilist" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: machine learning synthetic spectra for probabilist</div>
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
