---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The intersection of advanced machine learning and computational science has forged powerful new paradigms for scientific discovery, notably in the fields of emulation and inference. Emulation involves creating fast, data-driven surrogate models that mimic the behavior of complex, expensive physical simulations or real-world systems. These emulators provide rapid predictions, enabling efficient exploration of vast parameter spaces, uncertainty quantification, and real-time decision-making. Complementing this, inference focuses on extracting meaningful insights, unknown parameters, or hidden physics from observational data, often incomplete or noisy, by leveraging sophisticated statistical and machine learning techniques.

Traditional numerical simulations, while precise, are often computationally prohibitive, especially when exploring multi-dimensional parameter spaces or requiring real-time responses. Similarly, extracting actionable information from vast and often sparse scientific datasets presents significant challenges, demanding robust methods to handle noise, incompleteness, and high dimensionality. Emulation and inference techniques, particularly those based on deep learning and probabilistic modeling, are critical for overcoming these bottlenecks. They enable scientists to accelerate hypothesis testing, optimize experimental designs, and unravel intricate relationships within complex systems, from the dynamics of cosmic structures to the behavior of turbulent flows.

These methodologies frequently employ advanced machine learning architectures, including various forms of neural networks, to capture complex non-linear relationships. A crucial aspect of this research area is the robust quantification of uncertainty associated with predictions and inferences. Probabilistic machine learning models, such as probabilistic neural networks and Gaussian processes, are increasingly adopted to provide not just point estimates but also reliable measures of confidence, which is paramount for scientific credibility and informed decision-making across domains like astrophysics, fluid dynamics, and high-energy physics.

My work specifically addresses these grand challenges by developing novel machine learning methodologies for both emulation and inference across diverse scientific fields. In astrophysics and cosmology, I have developed advanced techniques for rapid and robust parameter estimation, such as SYTH-Z, a machine learning framework for probabilistic redshift estimation from synthetic spectra, providing crucial uncertainty quantification. I have also contributed to understanding large-scale structure with SHAMNet, enabling differentiable predictions for improved cosmological constraints, and developed deep neural network approaches for peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect. Furthermore, I have engineered efficient emulators, including a Matter Power Spectrum Emulator for f(R) modified gravity cosmologies, significantly accelerating theoretical predictions and model comparison.

Beyond cosmology, my research extends to high-performance computing and engineering applications, particularly in fluid dynamics. I have pioneered the use of probabilistic neural networks (PNNs) for reduced-order surrogate modeling of fluid flows, offering both efficient simulation and robust uncertainty quantification and data recovery. This includes developing latent-space time evolution models using Gaussian process emulation for non-intrusive reduced-order models. Additionally, I have tackled the challenge of global field reconstruction from sparse sensor data, utilizing Voronoi tessellation-assisted deep learning to infer full-field dynamics. A recurring theme across all my contributions is the development of interpretable uncertainty quantification techniques, ensuring that AI predictions are not only accurate but also trustworthy and actionable for scientific discovery and critical engineering applications.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/global-field-reconstruction-from-sparse-sensors-wi_plot_1_93ef286c.png" alt="Figure from Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning</div>
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
