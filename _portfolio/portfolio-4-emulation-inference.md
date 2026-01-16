---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Computational modeling of complex physical systems, spanning disciplines from cosmology and astrophysics to fluid dynamics, often involves simulations that are computationally demanding. These high-fidelity simulations, while indispensable for scientific discovery and engineering design, present significant challenges for comprehensive parameter exploration, robust uncertainty quantification, and real-time predictive analysis. The field of emulation, also known as surrogate modeling, addresses these hurdles by developing computationally inexpensive yet accurate approximations of these complex simulators. By learning the input-output relationships of a high-fidelity model, emulators enable rapid predictions, vastly accelerating scientific workflows and facilitating deeper insights into system behavior.

Machine learning techniques, particularly advanced neural networks and Gaussian processes, have emerged as transformative tools for constructing these powerful emulators. They are adept at capturing highly non-linear relationships and managing high-dimensional data, which are characteristic of scientific simulations. A critical challenge within this research domain is not only achieving computational speed-up but also accurately quantifying the uncertainty associated with emulator predictions. Trustworthy uncertainty estimates are paramount for scientific credibility, risk assessment, and informed decision-making, particularly in fields where models guide observational campaigns or critical design choices.

My research extensively explores and advances the methodologies of emulation and inference, primarily leveraging probabilistic machine learning to solve complex problems across diverse scientific domains. I have developed novel probabilistic neural network (PNN) architectures, demonstrating their effectiveness as reduced-order surrogates for fluid flows and for robust data recovery, even from noisy and sparse observations, as detailed in my work on "Probabilistic neural network-based reduced-order surrogate for fluid flows" and "Probabilistic neural networks for fluid flow surrogate modeling and data recovery." This approach significantly enhances the efficiency and reliability of dynamic system modeling.

In the realm of cosmology, I have focused on building highly efficient emulators for computationally intensive models. My contributions include an "Emulator-Based Inference of Cosmological Subgrid Models" to accelerate the analysis of complex astrophysical processes, and a "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies," which provides a critical tool for efficiently exploring alternative gravity theories and comparing their predictions with astronomical observations. A core thread through my work is the emphasis on robust and interpretable uncertainty quantification, as evidenced by my research on "Interpretable Uncertainty Quantification in AI for HEP." Furthermore, I have developed techniques for "Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation," which significantly improves the modeling of complex system dynamics by learning their evolution in a compressed, efficient representation. These advancements collectively yield faster, more accurate, and more reliable predictive models, accelerating the pace of scientific discovery and enabling new avenues of research.

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
