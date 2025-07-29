---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The simulation and analysis of complex physical systems, such as turbulent fluid flows or the large-scale structure of the universe, pose significant computational challenges. Traditional high-fidelity simulations are often prohibitively expensive, making it difficult to explore vast parameter spaces, perform inverse problems, or conduct real-time analysis. This computational bottleneck necessitates the development of advanced computational strategies, specifically in the areas of emulation and inference. Emulation involves creating fast, accurate surrogate models that mimic the behavior of complex simulators, while inference focuses on extracting meaningful parameters and understanding from observational data, often leveraging these emulators.

A key approach in this domain is the development of reduced-order models (ROMs), which drastically lower the dimensionality of complex systems while retaining essential dynamics. Machine learning, particularly deep neural networks, has emerged as a powerful paradigm for constructing these surrogates and emulators. These data-driven models can learn intricate non-linear relationships, offering significant speedups. Furthermore, incorporating probabilistic methods into these neural network architectures is crucial for quantifying uncertainty in predictions, providing robust and reliable estimates, and enabling principled data recovery and parameter inference in scientific applications.

My research extensively contributes to addressing these challenges by developing novel, machine learning-driven methodologies for emulation and inference in computationally demanding scientific domains. I have focused on leveraging the power of neural networks to build efficient and accurate surrogate models for complex physical phenomena, specifically in the fields of cosmology and fluid dynamics. A central theme of my work is the integration of probabilistic frameworks, allowing for robust uncertainty quantification alongside high-speed predictions, which is critical for trustworthy scientific discovery and engineering design.

In the realm of cosmology, I developed SHAMNet, a differentiable neural network-based emulator designed to predict large-scale structure, significantly accelerating parameter inference for galaxy formation models. For f(R) modified gravity cosmologies, I constructed a matter power spectrum emulator, enabling rapid exploration of alternative gravity theories. Concurrently, in fluid dynamics, I have advanced the use of probabilistic neural networks to create robust reduced-order surrogates for fluid flows, enabling not only fast predictions but also reliable uncertainty quantification and data recovery from sparse observations. Furthermore, my work on latent-space time evolution using Gaussian process emulation has provided non-intrusive methods for dynamic system prediction, decoupling the surrogate from the original simulator code. These contributions underscore my commitment to developing powerful, uncertainty-aware, and computationally efficient tools for scientific modeling and analysis.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_2_68f5e3f1.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/matter-power-spectrum-emulator-for-fr-modified-gra_plot_1_d6154d54.png" alt="Figure from Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/latent-space-time-evolution-of-non-intrusive-reduc_plot_3_698663be.png" alt="Figure from Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation</div>
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
