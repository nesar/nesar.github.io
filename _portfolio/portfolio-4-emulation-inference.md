---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific inquiry across fields such as cosmology and fluid dynamics heavily relies on complex numerical simulations, which, despite their power, are computationally intensive. This significant burden on resources forms a major bottleneck for comprehensive parameter exploration, robust uncertainty quantification, and the efficient calibration of intricate subgrid models, particularly within high-dimensional parameter spaces. The computational cost often renders exhaustive sampling through direct simulation infeasible, thus limiting the depth of scientific discovery.

To address these limitations, the development of sophisticated surrogate models, or emulators, has become a pivotal research area. These data-driven models, typically employing machine learning techniques like neural networks and Gaussian processes, are trained on a carefully selected, limited dataset of high-fidelity simulation outputs. Once established, an emulator can rapidly and accurately predict simulation outcomes for new input parameters at a mere fraction of the original computational cost. This acceleration allows for orders of magnitude more evaluations, fundamentally transforming the feasibility of exhaustive analyses and expanding the scope of scientific and engineering exploration. Crucially, these methods also aim to quantify the inherent uncertainty in their predictions.

My work significantly contributes to advancing these emulation and inference techniques for computationally demanding problems in both cosmology and fluid dynamics. I have engineered robust neural network and Gaussian process-based emulators capable of handling complex physics and high-dimensional parameter spaces. For instance, I developed an "Emulator-Based Inference of Cosmological Subgrid Models" and a "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies," enabling rapid exploration of non-standard theories and intricate subgrid physics. A key technical contribution is "Differentiable Predictions for Large Scale Structure with SHAMNet," which introduces a differentiable neural network for efficient and precise predictions of galaxy formation and clustering, facilitating gradient-based inference previously deemed intractable.

In fluid dynamics, I have advanced reduced-order modeling through innovative applications of probabilistic machine learning. My research has focused on creating "Probabilistic neural network-based reduced-order surrogates for fluid flows" and extending this to "Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation." These models not only efficiently surrogate complex fluid behaviors but also provide essential uncertainty estimates, crucial for robust engineering design and predictive reliability. Additionally, I have demonstrated the power of "Probabilistic neural networks for fluid flow surrogate modeling and data recovery," showcasing their capability to reconstruct missing data and provide resilient predictions even with sparse sensor inputs. Collectively, my contributions accelerate scientific discovery, enable comprehensive uncertainty quantification, and make previously intractable analyses feasible across diverse scientific and engineering disciplines.

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
