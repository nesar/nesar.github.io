---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific discovery and engineering design increasingly rely on complex simulations and large datasets. Many physical and engineering systems are governed by intricate non-linear dynamics, making their behavior computationally expensive to model or difficult to infer from limited observations. This computational burden often limits the scope of scientific exploration, real-time decision-making, and the robust quantification of uncertainties inherent in both models and data.

In this context, the field of Emulation and Inference leverages advanced machine learning and artificial intelligence techniques to accelerate and enhance scientific understanding. Emulation involves building fast, accurate surrogate models—often called emulators—that can mimic the behavior of complex simulations at a fraction of the computational cost. This enables rapid exploration of parameter spaces, efficient uncertainty propagation, and inverse problem solving. Inference, on the other hand, focuses on extracting meaningful parameters, hidden states, or predictive insights from observational data, often in the presence of noise and incompleteness, while providing robust quantification of the associated uncertainties.

My research at the intersection of machine learning, physics, and engineering focuses on developing novel probabilistic and interpretable AI frameworks for high-fidelity emulation and robust inference. I have developed and applied methodologies such as Probabilistic Neural Networks (PNNs) and Gaussian Process emulation to construct reduced-order surrogate models for complex systems, including fluid flows and high-dimensional stress fields. A key emphasis has been on enabling interpretable uncertainty quantification within these AI models, essential for trustworthy scientific predictions. This work also includes techniques for latent-space time evolution of non-intrusive models and automated machine learning frameworks, streamlining the model development process.

Furthermore, I have contributed to significant advancements in scientific inference across various domains. This includes the development of differentiable prediction models like SHAMNet for large-scale structure in cosmology, enabling efficient parameter inference, and the creation of SYTH-Z for probabilistic redshift estimation from synthetic spectra. My work extends to robust parameter estimation, such as peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect using deep neural networks, and global field reconstruction from sparse sensor data leveraging Voronoi tessellation-assisted deep learning. I have also developed matter power spectrum emulators for modified gravity cosmologies, critically accelerating the analysis of cosmological surveys. These contributions collectively empower scientists and engineers with tools for faster, more reliable, and interpretable analysis of complex physical phenomena, accelerating discovery and engineering innovation.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
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
