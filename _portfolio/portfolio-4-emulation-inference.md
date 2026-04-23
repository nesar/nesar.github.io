---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific research across diverse fields such as astrophysics, cosmology, fluid dynamics, and high energy physics often relies on complex, computationally intensive simulations to model intricate physical phenomena. These simulations, while powerful, pose significant bottlenecks for exploring vast parameter spaces, performing efficient inverse inference from observational data, and making real-time predictions. The sheer computational cost can render comprehensive scientific discovery and robust uncertainty quantification prohibitively expensive, hindering progress in understanding fundamental processes and interpreting experimental results.

To overcome these challenges, the field of emulation and surrogate modeling has emerged, focusing on developing fast, accurate, and often differentiable approximate models of complex simulations. These emulators, typically built using advanced machine learning techniques, enable orders-of-magnitude acceleration in predictive tasks, facilitating rapid parameter inference, design optimization, and data analysis. A critical aspect of this research area is not only generating accurate predictions but also providing robust and interpretable quantification of the uncertainty associated with these predictions, which is essential for reliable scientific conclusions and trustworthy AI applications.

My work significantly contributes to this domain by developing novel machine learning methodologies for both accelerating complex scientific simulations through emulation and performing robust parameter inference with quantifiable uncertainty. I have pioneered the use of Probabilistic Neural Networks (PNNs) and Gaussian Process emulation to construct reduced-order surrogates for systems ranging from fluid flows to cosmological models. Specifically, I have developed PNN-based reduced-order models for fluid flows, enabling efficient surrogate modeling and data recovery while rigorously quantifying prediction uncertainties, as demonstrated in my work on "Probabilistic neural network-based reduced-order surrogate for fluid flows." For broader application, I have also explored latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, pushing the boundaries of dynamic system modeling. Furthermore, my research in "Interpretable Uncertainty Quantification in AI for HEP" highlights the crucial need for transparent and reliable error estimation in scientific AI applications.

In cosmology and astrophysics, my contributions span several key areas. I have developed a "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies," allowing for rapid exploration of alternative gravity theories. My work on "Emulator-Based Inference of Cosmological Subgrid Models" significantly accelerates the understanding of galaxy formation processes. I also introduced SHAMNet for "Differentiable Predictions for Large Scale Structure," providing a powerful tool for cosmological parameter estimation. Beyond large-scale structure, I have applied deep neural networks to "Peculiar Velocity Estimation from Kinetic SZ Effect" and developed SYTH-Z, a "Machine learning synthetic spectra for probabilistic redshift estimation," crucial for galaxy surveys. These advancements collectively provide high-fidelity, computationally efficient tools that accelerate scientific discovery, enable deeper insights into complex physical phenomena, and equip researchers with robust uncertainty measures critical for modern data-driven science.

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
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
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
