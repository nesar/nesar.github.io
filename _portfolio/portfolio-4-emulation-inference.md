---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The increasing complexity of scientific and engineering problems often necessitates the use of high-fidelity numerical simulations, which, despite their accuracy, are extraordinarily computationally expensive. Fields such as cosmology, climate modeling, and fluid dynamics rely on these simulations to explore vast parameter spaces, understand intricate physical phenomena, and make predictions. However, the time and resources required to run these models repeatedly for tasks like design optimization, uncertainty quantification, or parameter inference present a significant bottleneck to scientific discovery and technological advancement.

This challenge has driven extensive research into developing efficient surrogate models, also known as emulators or reduced-order models (ROMs). These data-driven approximations learn the input-output relationship of complex simulations, providing predictions orders of magnitude faster than their high-fidelity counterparts. A critical aspect of developing reliable surrogates is not only to achieve high accuracy but also to robustly quantify the uncertainty associated with their predictions, ensuring that decisions and inferences made based on these models are statistically sound and trustworthy.

My research focuses on developing and applying advanced machine learning and statistical methodologies to create robust and efficient surrogate models for complex physical systems, enabling rapid inference and exploration. I have pioneered the use of probabilistic neural networks (PNNs) for surrogate modeling in fluid dynamics, demonstrating their capability to provide not just predictions but also crucial uncertainty estimates for high-dimensional flow fields and for challenging tasks like data recovery. This work significantly enhances the reliability of data-driven models by explicitly capturing predictive uncertainty.

Furthermore, I have developed novel emulator-based frameworks for accelerating scientific discovery in cosmology, specifically for performing efficient inference of cosmological subgrid models and for creating highly accurate Matter Power Spectrum emulators for modified gravity theories like f(R) cosmology. This work involves leveraging sophisticated techniques such as Gaussian process emulation and reduced-order modeling in latent spaces to efficiently capture the time evolution of complex systems, providing a powerful tool for analyzing large datasets and exploring new physical theories with unprecedented speed. These contributions accelerate scientific discovery and enable robust decision-making in computationally intensive domains.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/emulator-based-inference-of-cosmological-subgrid-m_plot_1_9c094db3.png" alt="Figure from Emulator-Based Inference of Cosmological Subgrid Models" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Emulator-Based Inference of Cosmological Subgrid Models</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/matter-power-spectrum-emulator-for-fr-modified-gra_plot_1_d6154d54.png" alt="Figure from Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/latent-space-time-evolution-of-non-intrusive-reduc_plot_1_662d841c.png" alt="Figure from Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation" onclick="openModal(this)" loading="lazy" />
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
