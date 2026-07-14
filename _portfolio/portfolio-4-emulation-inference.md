---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific and engineering disciplines frequently rely on high-fidelity numerical simulations to model complex phenomena, ranging from the evolution of the universe to the dynamics of turbulent fluid flows. While these simulations provide invaluable insights, their computational cost can be prohibitive, often restricting exhaustive parameter exploration, real-time analysis, and robust inference from observational data. To circumvent these limitations, the fields of emulation and surrogate modeling have emerged, leveraging advanced data-driven techniques, particularly machine learning, to create fast, approximate models. These "emulators" or "surrogates" significantly accelerate prediction and enable efficient inference, allowing for comprehensive uncertainty quantification and parameter estimation.

Such methodologies often involve dimensionality reduction to capture the dominant behaviors in high-dimensional systems, coupled with sophisticated regression techniques to map input parameters to system responses. A key aspect of modern emulation is the incorporation of probabilistic frameworks to provide not just point predictions, but also robust quantification of the uncertainty inherent in the models and the underlying data. This approach is critical for advancing understanding in areas ranging from the fundamental physics of the universe, such as large-scale structure formation and modified gravity theories, to intricate engineering problems like multiphysics simulations and aerodynamic design, thereby accelerating scientific discovery and informing engineering decisions.

My research focuses on developing and applying cutting-edge probabilistic machine learning and reduced-order modeling techniques to build highly efficient and reliable emulators for complex scientific simulations. In cosmology, I have significantly contributed to accelerating scientific discovery through novel emulation techniques. Specifically, I developed an *Emulator-Based Inference framework for Cosmological Subgrid Models*, which enables efficient parameter inference for microphysical processes that dictate large-scale structure formation, directly from cosmological data. Building on this, I also constructed a *Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies*. This emulator allows for the rapid and robust exploration of alternative gravitational theories, providing a critical tool for testing fundamental physics against astronomical observations with properly quantified uncertainties. A more general contribution includes my work on the *latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation*, which provides a versatile framework for efficiently predicting the long-term dynamics of high-dimensional systems by modeling their evolution in a low-dimensional latent space.

For complex fluid flow problems, my contributions center on leveraging *probabilistic neural networks (PNNs)* to enhance both predictive modeling and data analysis. I have developed *probabilistic neural network-based reduced-order surrogates for fluid flows*, which not only provide rapid predictions of fluid behavior but also crucially quantify the inherent uncertainty in these predictions – a vital aspect for high-consequence engineering design and analysis. Furthermore, I extended the utility of PNNs for *fluid flow surrogate modeling and data recovery*, demonstrating their capacity to reconstruct missing or corrupted simulation data with robust uncertainty estimates, thereby improving the integrity and utility of large-scale fluid dynamics datasets. These contributions collectively address the challenge of computational intensity and uncertainty quantification across diverse scientific and engineering domains, accelerating discovery and enabling more reliable decision-making.

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
