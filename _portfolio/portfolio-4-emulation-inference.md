---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Computational science increasingly relies on complex simulations to model intricate natural phenomena, from astrophysical processes governing the universe's evolution to the turbulent dynamics of fluid flows. These simulations, while powerful, often demand immense computational resources, making extensive parameter space exploration, robust uncertainty quantification, and rapid hypothesis testing prohibitively challenging. The field of emulation and inference directly addresses these bottlenecks by developing advanced statistical and machine learning techniques to construct fast, accurate surrogate models, often termed emulators, of these computationally intensive simulators.

These surrogate models enable orders-of-magnitude faster predictions, thereby facilitating comprehensive exploration of high-dimensional parameter spaces and the propagation of uncertainties through complex scientific pipelines. Key challenges within this domain include ensuring the accuracy and fidelity of emulators across broad input ranges, precisely quantifying their own inherent predictive uncertainties, and integrating them effectively within larger inference frameworks. Methodologies such as probabilistic neural networks, Gaussian process emulation, and differentiable programming are at the forefront of tackling these challenges, offering pathways to accelerate scientific discovery and enhance the interpretability and reliability of model predictions.

My research significantly contributes to this landscape by developing innovative machine learning and statistical methodologies for high-fidelity emulation and robust inference across diverse scientific domains. I have pioneered the application of probabilistic neural networks (PNNs) for generating reduced-order surrogates, particularly for computationally intensive systems like fluid flows, enabling efficient surrogate modeling and critical data recovery even with limited observations. Furthermore, I have developed advanced non-intrusive reduced-order models leveraging Gaussian process emulation for latent-space time evolution, substantially accelerating simulations while maintaining accuracy. A core aspect of my work also includes the development of differentiable prediction frameworks, such as SHAMNet, which facilitates direct backpropagation through scientific models for optimized parameter inference in areas like large-scale structure cosmology.

These methodological advancements are directly applied to pressing problems in cosmology and astrophysics, including emulator-based inference of cosmological subgrid models and the development of matter power spectrum emulators for complex f(R) modified gravity cosmologies. My work also addresses the crucial need for interpretable uncertainty quantification in AI models applied to high-energy physics (HEP), ensuring that model predictions come with reliable estimates of their confidence. By providing tools for faster, more accurate, and uncertainty-aware scientific predictions, my contributions empower researchers to explore more complex theories, analyze larger datasets, and achieve a deeper understanding of fundamental physical processes.

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
