---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific inquiry into complex physical phenomena often relies on high-fidelity simulations that are computationally intensive, presenting significant challenges for tasks such as uncertainty quantification, parameter inference, and real-time analysis. This computational bottleneck limits the ability to thoroughly explore vast parameter spaces, impeding scientific discovery and model validation across disciplines ranging from astrophysics to engineering. The development of efficient and accurate surrogate models, or emulators, has emerged as a critical solution to these challenges.

Emulators are data-driven approximations that learn the input-output relationship of complex simulations, providing predictions at a fraction of the computational cost. These models typically employ advanced machine learning techniques, such as neural networks and Gaussian processes, to build fast, statistical representations of the underlying physics. A crucial aspect of this field is the development of robust methodologies for quantifying the uncertainty associated with emulator predictions, which is vital for reliable scientific inference and decision-making.

Furthermore, for high-dimensional systems like fluid flows, the integration of reduced-order modeling (ROM) techniques with emulation becomes essential. ROMs project the system's dynamics onto a lower-dimensional subspace, significantly simplifying the problem while retaining the most important characteristics. Combining these with probabilistic machine learning methods allows for the creation of surrogates that not only accelerate predictions but also provide a principled framework for capturing and propagating uncertainties throughout the modeling process, thereby enhancing the utility and trustworthiness of these advanced computational tools.

My work in this area has focused on developing and applying advanced emulation and inference techniques to bridge the gap between high-fidelity simulations and the demands of scientific exploration. I have specifically contributed to the creation of probabilistic neural network (PNN)-based reduced-order surrogates for complex fluid flows, enabling efficient forward predictions and robust data recovery from sparse measurements. Furthermore, I have developed methods for latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, which significantly accelerates the dynamic prediction of high-dimensional systems by learning their evolution in a compact, lower-dimensional representation.

Beyond fluid dynamics, I have applied these sophisticated emulation frameworks to address critical problems in cosmology. This includes the development of an emulator for the matter power spectrum in f(R) modified gravity cosmologies, which dramatically speeds up the exploration of alternative gravitational theories. Additionally, I have leveraged emulator-based inference to efficiently constrain and understand cosmological subgrid models, thereby enabling robust statistical analysis and enhancing our ability to extract cosmological parameters from observational data, all while rigorously quantifying uncertainties and significantly reducing computational barriers.

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
