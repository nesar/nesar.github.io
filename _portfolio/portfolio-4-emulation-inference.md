---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The field of scientific emulation and inference is dedicated to developing sophisticated computational models that can rapidly and accurately approximate the outputs of complex, often computationally prohibitive, numerical simulations. This is crucial across diverse scientific disciplines, from astrophysics and cosmology to fluid dynamics and high-energy physics, where understanding intricate physical processes relies heavily on high-fidelity simulations that are too slow for extensive parameter exploration or real-time analysis. The primary goal is to create "surrogate models" or "emulators" that capture the essential physics with significantly reduced computational cost, thereby enabling efficient parameter estimation, uncertainty quantification, and accelerating the pace of scientific discovery.

A key challenge in this domain is not only achieving computational efficiency but also ensuring the reliability and interpretability of predictions. This involves developing robust methods for quantifying the uncertainty associated with emulator predictions, which is essential for making credible scientific inferences. Furthermore, the ability to perform efficient Bayesian inference and explore high-dimensional parameter spaces for complex physical models necessitates highly optimized and accurate surrogate representations. Techniques such as reduced-order modeling further contribute by compressing the complexity of high-dimensional systems, allowing for faster time-evolution and analysis of dynamic phenomena.

My research focuses on developing and applying cutting-edge machine learning and statistical methods to build robust, interpretable, and computationally efficient emulators and inference frameworks for complex physical systems. I have developed novel probabilistic neural network architectures and leveraged Gaussian process emulation to create high-fidelity surrogate models for diverse applications. For instance, my work addresses the computationally expensive task of cosmological subgrid model inference, providing rapid and accurate predictions crucial for understanding structure formation.

I have also developed methodologies for differentiable predictions for large-scale structure using SHAMNet, enabling more efficient parameter estimation in cosmology. In the realm of fluid dynamics, I have contributed to probabilistic neural network-based reduced-order surrogates, including their application for fluid flow surrogate modeling and data recovery, and explored latent-space time evolution using Gaussian process emulation to efficiently model dynamic systems. A significant aspect of my contributions involves establishing interpretable uncertainty quantification in AI for high-energy physics, enhancing the trustworthiness of machine learning predictions, and developing specific emulators such as the Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, which are vital for probing fundamental physics. These contributions collectively enable faster scientific discovery, more reliable parameter inference, and a deeper understanding of complex physical phenomena.

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
