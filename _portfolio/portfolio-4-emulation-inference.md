---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Complex scientific research in fields such as cosmology, astrophysics, and fluid dynamics heavily relies on computationally intensive simulations to model intricate physical phenomena. These simulations, while powerful, often pose a significant bottleneck for exploring vast parameter spaces, performing robust statistical inference, and quantifying uncertainties, especially when confronted with large datasets or the need for rapid predictions. To overcome these challenges, a transformative approach involves developing high-fidelity, data-driven surrogate models, often termed emulators or reduced-order models (ROMs). These models learn the input-output relationships of complex simulations, enabling orders-of-magnitude speedups while maintaining accuracy.

The development of such emulators leverages advanced machine learning techniques, including deep neural networks, probabilistic neural networks, and Gaussian processes, to capture non-linear relationships and efficiently extrapolate or interpolate within the simulation's parameter space. Crucially, these surrogate models are designed not just for speed, but also for robust and interpretable uncertainty quantification, which is paramount for scientific discovery and reliable decision-making. Their applications span from accelerating the analysis of cosmic large-scale structure and galaxy formation to modeling complex turbulent fluid flows, enabling rapid parameter inference from observational data and the exploration of new physical theories.

My work significantly contributes to the development and application of advanced emulation and inference techniques across diverse scientific domains. I have focused on creating robust, fast, and interpretable machine learning surrogates that push the boundaries of computational science. For instance, in cosmology, I have developed emulators for complex phenomena such as subgrid models within galaxy formation simulations and for the matter power spectrum in modified gravity theories, specifically f(R) cosmologies, dramatically accelerating the process of cosmological parameter inference from observations. Furthermore, I developed SHAMNet, which provides differentiable predictions for large-scale structure, enabling efficient gradient-based optimization and sensitivity analysis.

Beyond cosmology, my contributions extend to developing novel surrogate models for fluid dynamics, employing probabilistic neural networks and Gaussian process emulation for reduced-order models. These advancements allow for efficient latent-space time evolution of non-intrusive ROMs and data recovery, offering powerful tools for real-time analysis and design optimization in engineering applications. A central theme in my research is interpretable uncertainty quantification, which I have applied to AI models in high-energy physics and utilized to reduce model error in astrophysical applications like weak lensing cluster mass estimation through optimised galaxy selection. Collectively, my methodologies emphasize building trust in AI-driven scientific tools by providing not just predictions, but also a clear understanding of their associated uncertainties, ultimately accelerating scientific discovery and enhancing our capacity for data-driven inference in complex systems.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/emulator-based-inference-of-cosmological-subgrid-m_plot_1_9c094db3.png" alt="Figure from Emulator-Based Inference of Cosmological Subgrid Models" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Emulator-Based Inference of Cosmological Subgrid Models</div>
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
