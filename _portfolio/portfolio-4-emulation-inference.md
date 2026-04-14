---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific discovery in many domains, from astrophysics to engineering, relies heavily on complex numerical simulations. While these simulations provide high-fidelity predictions, they are often computationally expensive, making extensive parameter exploration, real-time analysis, or robust uncertainty quantification challenging. This inherent computational cost necessitates the development of efficient surrogate models, also known as emulators, which can approximate the behavior of intricate simulations at a fraction of the computational expenditure, thereby accelerating scientific inquiry and engineering design.

The field of emulation and inference focuses on creating fast, accurate, and robust data-driven models that can predict simulation outputs for new inputs, often while providing estimates of their prediction uncertainty. Techniques frequently employed include neural networks, Gaussian processes, and various reduced-order modeling strategies. These methods are crucial for accelerating parameter inference from observational data, optimizing system designs, and enabling sensitivity analyses across high-dimensional parameter spaces in fields such as cosmology, fluid dynamics, and high-energy physics. A key aspect of modern approaches is the integration of probabilistic frameworks to provide meaningful uncertainty estimates alongside predictions, which is essential for drawing reliable scientific conclusions.

My research addresses these critical challenges by developing advanced machine learning and statistical methodologies for building efficient and reliable surrogate models. I have particularly focused on integrating probabilistic frameworks into neural networks, as demonstrated in my work on "Probabilistic neural network-based reduced-order surrogate for fluid flows" and "Probabilistic neural networks for fluid flow surrogate modeling and data recovery." These contributions enhance model robustness and provide interpretable uncertainty quantification, crucial for high-stakes scientific applications. Furthermore, I have explored "Differentiable Predictions for Large Scale Structure with SHAMNet," enabling end-to-end differentiable pipelines that significantly accelerate parameter inference in complex cosmological simulations. My work also extends to creating "Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation," which improves the efficiency of dynamic system modeling by leveraging the strengths of both reduced-order models and Gaussian processes.

The methodologies I have developed are directly applied to pressing problems across various scientific disciplines. In cosmology, I have created "Emulator-Based Inference of Cosmological Subgrid Models" and a "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies," allowing for rapid exploration of complex cosmological theories and efficient inference from observational data. For the high-energy physics community, I have contributed to "Interpretable Uncertainty Quantification in AI for HEP," ensuring that AI models used in particle physics experiments provide reliable and transparent uncertainty estimates, critical for discovery and precision measurements. My work consistently aims to bridge the gap between computationally intensive simulations and data analysis, enabling faster scientific discovery and more robust, uncertainty-aware inference. This approach empowers researchers to tackle previously intractable problems, accelerate model development, and gain deeper insights into the fundamental laws governing the universe and complex physical systems.

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
