---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The exploration of complex physical phenomena, from the evolution of the universe to intricate fluid dynamics, heavily relies on high-fidelity numerical simulations. While these simulations provide invaluable insights, their computational cost often renders them impractical for extensive parameter space exploration, robust uncertainty quantification, or real-time applications. This limitation creates a significant bottleneck in scientific discovery, hindering efficient model calibration and rapid system design.

To overcome these challenges, the field of scientific machine learning develops surrogate models, often termed emulators or reduced-order models. These data-driven approximations are trained on limited high-fidelity simulation outputs to rapidly predict outcomes for new inputs, dramatically accelerating scientific workflows. Methodologies leverage neural networks, Gaussian processes, and dimensionality reduction. A critical aspect involves incorporating probabilistic frameworks, allowing emulators not only to predict but also to quantify associated uncertainty, which is essential for reliable scientific inference.

Such surrogate modeling transforms various scientific disciplines. In cosmology, emulators enable efficient parameter inference for large-scale structure observations, facilitating the study of dark energy, dark matter, and modified gravity, as well as unresolved subgrid processes. In fluid dynamics, they allow rapid prediction of flow fields under varying conditions, offering pathways for real-time control, optimization, and recovery of missing data, bridging the gap between theoretical modeling and practical engineering applications.

My research focuses on developing and applying cutting-edge machine learning and statistical methods to construct highly accurate, efficient, and robust emulators and reduced-order models. I have developed novel differentiable emulators, such as SHAMNet, for predicting large-scale structure observables, significantly accelerating cosmological parameter inference and modified gravity exploration via gradient-based optimization. My work also extends to developing probabilistic neural networks for fluid flow surrogate modeling, providing rapid predictions, crucial uncertainty quantification, and facilitating data recovery from sparse measurements. A key technical contribution involves latent-space time evolution using Gaussian process emulation to create non-intrusive reduced-order models for complex, time-dependent systems.

These advancements have a profound impact. In cosmology, I have applied emulator-based inference to constrain complex subgrid models governing baryonic effects and developed matter power spectrum emulators for f(R) modified gravity cosmologies. In fluid dynamics, my probabilistic surrogates provide tools for real-time analysis and control. Collectively, my contributions enable faster scientific discovery, more reliable uncertainty quantification, and the ability to tackle previously intractable problems in both fundamental physics and applied engineering.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/emulator-based-inference-of-cosmological-subgrid-m_plot_1_9c094db3.png" alt="Figure from Emulator-Based Inference of Cosmological Subgrid Models" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Emulator-Based Inference of Cosmological Subgrid Models</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/matter-power-spectrum-emulator-for-fr-modified-gra_plot_1_d6154d54.png" alt="Figure from Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies</div>
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
