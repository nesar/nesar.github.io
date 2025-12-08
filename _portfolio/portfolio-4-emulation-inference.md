---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The emulation and inference research area is at the forefront of scientific discovery, driven by the increasing complexity and computational cost of modern simulations and the burgeoning volume of experimental data. Scientists across disciplines, from astrophysics and cosmology to fluid dynamics and high-energy physics, rely on sophisticated computational models to understand fundamental phenomena. However, exploring vast parameter spaces, making real-time predictions, or extracting subtle signals from noisy data often proves intractable with traditional simulation techniques. Emulation addresses this by creating fast, accurate surrogate models—often powered by machine learning—that mimic the behavior of complex simulations at a fraction of the computational expense.

Inference, on the other hand, focuses on extracting meaningful information, parameters, and predictions from observed data or simulation outputs. This process is inherently linked to uncertainty quantification, a critical component that assesses the reliability and robustness of any scientific claim. Machine learning, particularly deep neural networks and probabilistic approaches, has revolutionized both emulation and inference by enabling the construction of highly non-linear, high-dimensional mappings between inputs and outputs, while also providing frameworks for quantifying the inherent uncertainties in these predictions. This combined approach allows for unprecedented speed-ups in scientific analysis, accelerates the exploration of complex theories, and enables more robust and interpretable insights from data.

My work in this domain centers on developing and applying advanced machine learning methodologies to create efficient emulators and perform robust inference in computationally intensive scientific fields. I have focused on building probabilistic neural networks (PNNs) for fluid flow surrogate modeling and data recovery, which provide not just predictions but also crucial estimates of uncertainty. I've also pioneered the use of latent-space time evolution using Gaussian process emulation to accelerate non-intrusive reduced-order models, and developed Voronoi tessellation-assisted deep learning for global field reconstruction from sparse sensor data, significantly enhancing our ability to model complex systems.

In astrophysics and cosmology, I have developed innovative solutions such as SYTH-Z, which generates machine learning synthetic spectra for probabilistic redshift estimation, vastly improving our understanding of galaxy distances. My contributions also include SHAMNet, which provides differentiable predictions for large-scale structure, and a matter power spectrum emulator specifically for f(R) modified gravity cosmologies, enabling rapid testing of alternative gravity theories. Furthermore, I have applied deep neural networks for peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect and worked on reducing model error in weak lensing cluster mass estimation through optimized galaxy selection. A core aspect of my research across all these applications is the development of interpretable uncertainty quantification techniques in AI for high-energy physics and other domains, ensuring that the powerful predictions made by AI models are accompanied by transparent and trustworthy measures of their reliability.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
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
