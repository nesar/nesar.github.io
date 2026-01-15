---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The accurate and efficient prediction of complex physical phenomena is a cornerstone of modern scientific discovery and engineering design. However, many state-of-the-art simulations in fields like astrophysics, fluid dynamics, and materials science are computationally prohibitive, making tasks such as comprehensive parameter space exploration, robust uncertainty quantification, and real-time decision-making incredibly challenging. This computational bottleneck often limits the pace of scientific advancement and the practical application of high-fidelity models.

To overcome these limitations, the fields of emulation and inference have emerged as critical tools. Emulation involves constructing fast, data-driven approximations, or surrogates, of complex numerical simulations using advanced machine learning techniques. These surrogates capture the essential input-output relationships of the original simulator, enabling predictions orders of magnitude faster. Coupled with sophisticated inference methods, these emulators facilitate rapid parameter estimation, sensitivity analysis, and the quantification of predictive uncertainties, thereby transforming our ability to analyze and understand complex systems with unprecedented speed and confidence.

My research focuses on developing advanced methodologies for constructing robust and efficient emulators and surrogate models, with a strong emphasis on probabilistic approaches to accurately quantify uncertainty. I have pioneered the application of *probabilistic neural networks (PNNs)* to build reduced-order surrogates for complex systems, notably in *fluid flows*, which not only provide rapid predictions but also inherently quantify the associated predictive uncertainty. Furthermore, I have explored the use of *Gaussian process emulation* for efficient *latent-space time evolution* in *non-intrusive reduced-order models*, offering a powerful framework for dynamic system emulation.

This work has been successfully applied to diverse and computationally demanding scientific domains. In *cosmology*, I have developed *emulator-based inference techniques for subgrid models*, significantly accelerating the analysis of high-resolution cosmological simulations. I also contributed to creating a *Matter Power Spectrum Emulator for f(R) modified gravity cosmologies*, enabling faster exploration of alternative theories of gravity. For *fluid dynamics*, my PNN-based models have demonstrated remarkable capabilities in *surrogate modeling* and *data recovery*, providing efficient tools for analyzing and reconstructing high-dimensional flow fields. These contributions empower researchers to undertake previously intractable analyses, accelerating scientific discovery and enhancing our understanding of fundamental physical processes.

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
