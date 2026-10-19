---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Computational science and engineering increasingly rely on high-fidelity simulations to model complex physical phenomena, ranging from cosmological structure formation to turbulent fluid dynamics. While these simulations provide invaluable insights, their inherent computational expense often limits the scope of parameter space exploration, uncertainty quantification, and real-time analysis. This bottleneck motivates the development of sophisticated surrogate models, or emulators, which approximate the behavior of these complex simulations at a fraction of the computational cost, enabling rapid prediction and comprehensive inference.

The field of emulation and inference leverages advanced machine learning, deep learning, and statistical techniques to construct these fast, accurate, and often probabilistic surrogates. A key challenge lies in developing models that not only predict outcomes efficiently but also quantify the associated uncertainties, which is crucial for robust scientific discovery and decision-making. These methodologies are particularly transformative in high-dimensional systems where traditional approaches are intractable, facilitating tasks such as inverse problem solving, parameter estimation, and real-time system monitoring across diverse scientific and engineering disciplines.

My research focuses on developing and applying cutting-edge machine learning and deep learning methodologies to bridge the gap between computationally intensive simulations and rapid, data-driven scientific analysis. In cosmology, I have developed emulator-based inference frameworks to constrain parameters of subgrid models, accelerating our understanding of cosmic structure formation. I also introduced SYTH-Z, a machine learning approach for generating synthetic spectra that enables robust probabilistic redshift estimation. Furthermore, my work includes using deep neural networks for peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect and creating fast matter power spectrum emulators for modified gravity cosmologies like f(R), significantly advancing our ability to analyze large-scale cosmological surveys.

Beyond cosmology, I have made significant contributions to fluid dynamics, a domain characterized by high-dimensionality and complex non-linear dynamics. I have pioneered the use of probabilistic neural network-based reduced-order surrogates, offering efficient and uncertainty-aware models for fluid flows. This includes developing non-intrusive reduced-order models leveraging Gaussian process emulation in latent space to capture the time evolution of these systems effectively. Moreover, my work extends to using probabilistic neural networks for not only fluid flow surrogate modeling but also for robust data recovery from noisy or incomplete measurements, enabling more reliable predictions and insights in complex fluidic systems.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/emulator-based-inference-of-cosmological-subgrid-m_plot_1_9c094db3.png" alt="Figure from Emulator-Based Inference of Cosmological Subgrid Models" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Emulator-Based Inference of Cosmological Subgrid Models</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/peculiar-velocity-estimation-from-kinetic-sz-effec_plot_1_10d780ed.png" alt="Figure from Peculiar Velocity Estimation from Kinetic SZ Effect using Deep Neural Networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Peculiar Velocity Estimation from Kinetic SZ Effect using Deep Neural Networks</div>
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
