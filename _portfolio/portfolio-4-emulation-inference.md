---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The exploration of complex scientific phenomena, from the evolution of the universe to the intricacies of fluid dynamics, often relies on computationally intensive simulations. These high-fidelity models, while indispensable for scientific discovery and engineering design, pose significant challenges due to their prohibitive computational cost, limiting the scope of parameter space exploration, uncertainty quantification, and data-driven inference. This bottleneck necessitates the development of advanced surrogate modeling and emulation techniques that can provide accurate, fast, and robust approximations of these complex systems. The field of emulation and inference leverages breakthroughs in machine learning, statistical modeling, and numerical methods to create these data-driven proxies, bridging the gap between theoretical models and observational data.

This research area focuses on building highly efficient, data-driven representations of high-dimensional, non-linear physical systems. Methodologies frequently involve deep learning architectures, probabilistic graphical models, and reduced-order modeling strategies to capture underlying dynamics and relationships. Key objectives include achieving orders-of-magnitude speedups in prediction time, quantifying predictive uncertainties, and enabling efficient inverse problem solving and parameter inference. Applications span diverse domains, including predicting large-scale structure formation in cosmology, modeling turbulence and flow fields in engineering, and understanding the behavior of modified gravity theories crucial for fundamental physics.

My research focuses on developing advanced machine learning and statistical methodologies to create high-fidelity emulators and reduced-order surrogates for complex physical systems. I have developed differentiable prediction frameworks, such as SHAMNet, for cosmological large-scale structure simulations, significantly accelerating the generation of mock universes and enabling efficient parameter inference by providing an end-to-end differentiable pipeline. Furthermore, my work extensively utilizes Probabilistic Neural Networks (PNNs) and Gaussian Process emulation to build robust surrogate models for fluid flows and other dynamic systems. These approaches not only provide accurate predictions but also inherently quantify predictive uncertainty. I have also explored latent-space time evolution techniques to capture the dynamics of reduced-order models non-intrusively. Specific applications include emulating the matter power spectrum for f(R) modified gravity cosmologies, which is crucial for testing gravitational theories, and developing surrogates for complex fluid flow scenarios, including data recovery from sparse observations.

The technical contributions of my work lie in developing novel architectures and probabilistic frameworks that overcome the limitations of traditional methods. For instance, SHAMNet provides a differentiable end-to-end pipeline, making it uniquely powerful for inverse problems in cosmology. The integration of PNNs into reduced-order modeling offers enhanced robustness and uncertainty quantification, vital for reliable scientific prediction and data recovery in sparse-data regimes, particularly in fluid dynamics. By leveraging these techniques, I have demonstrated orders-of-magnitude speedups in simulation time, enabling comprehensive exploration of vast parameter spaces that were previously intractable. This significantly accelerates scientific discovery, improves the reliability of engineering designs, and facilitates a deeper understanding of fundamental physical phenomena by making complex simulations accessible for rigorous analysis and statistical inference.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
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
