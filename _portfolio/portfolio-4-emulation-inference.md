---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The simulation and analysis of complex physical systems, ranging from the intricate dynamics of fluid flows to the vast structures of the universe, pose significant computational challenges. High-fidelity simulations, while crucial for scientific discovery and engineering design, are often computationally prohibitive, making tasks like parameter exploration, uncertainty quantification, and inverse inference intractable. This necessitates the development of efficient, predictive models that can accurately capture system behavior without the enormous computational cost of full simulations. Emulators and surrogate models serve this purpose by learning the input-output relationships of complex systems from a limited number of high-fidelity simulations.

A key focus in this research area is the development of robust, data-driven methodologies capable of generating these efficient surrogates. This often involves leveraging advanced machine learning techniques, such as neural networks and Gaussian processes, to build models that are not only fast but also provide quantification of predictive uncertainty. Reduced-order models (ROMs) are particularly valuable for high-dimensional systems like fluid flows, where they compress the system dynamics into a lower-dimensional latent space, further enhancing computational efficiency. The combination of these techniques allows for rapid prediction, accelerates parameter inference, and enables a deeper, probabilistic understanding of complex physical phenomena.

My work directly addresses these challenges by developing and applying innovative emulation and surrogate modeling techniques across diverse scientific domains. I have focused on creating computationally efficient and robust data-driven models that can accelerate scientific discovery and facilitate advanced analysis, particularly where traditional simulation methods are too slow or complex. A central theme in my research is the incorporation of probabilistic frameworks to provide crucial uncertainty quantification alongside predictions.

Specifically, I have developed advanced emulators for cosmological applications, including a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies and an Emulator-Based Inference framework for Cosmological Subgrid Models. These tools significantly accelerate the exploration of cosmological parameter spaces and enable efficient inference of fundamental physics from observational data. In fluid dynamics, I have contributed to the development of Probabilistic Neural Networks for fluid flow surrogate modeling and data recovery, and I have explored probabilistic neural network-based reduced-order surrogates for fluid flows. Furthermore, I have investigated Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, pushing the boundaries of how efficiently and accurately we can predict the time-dependent behavior of complex systems. My contributions emphasize the integration of machine learning with physics-based problems to yield faster, more interpretable, and uncertainty-aware scientific models, thereby enabling novel insights and accelerating the pace of research in areas from astrophysics to engineering.

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
