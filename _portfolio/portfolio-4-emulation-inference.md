---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Modern scientific inquiry across fields like cosmology, astrophysics, and fluid dynamics often grapples with complex systems governed by intricate physical laws. Simulating these systems accurately requires immense computational resources, making exhaustive exploration of parameter spaces and robust statistical inference computationally prohibitive. This challenge has driven the development of advanced computational techniques, particularly emulation and inference, to accelerate scientific discovery. Emulation involves constructing fast, accurate surrogate models (emulators) that mimic the behavior of expensive simulations, while inference utilizes these emulators to efficiently constrain physical parameters, propagate uncertainties, and explore vast model spaces.

The power of emulation and inference lies in their ability to bridge the gap between theoretical models and observational data. By leveraging machine learning, statistical methods, and reduced-order modeling techniques, researchers can build computationally inexpensive surrogates that capture the essential physics of high-fidelity simulations. These surrogates enable rapid forward modeling, allowing for efficient likelihood evaluations, Bayesian inference, and sensitivity analyses. Furthermore, integrating uncertainty quantification into these frameworks is paramount, providing not just predictions but also reliable estimates of their confidence, which is crucial for making robust scientific conclusions and guiding future experiments.

My research extensively focuses on developing and applying sophisticated machine learning and statistical methodologies for emulation and inference across a range of complex scientific domains. I have pioneered the use of probabilistic neural networks and Gaussian process emulation to construct high-fidelity, reduced-order surrogates, effectively enabling the latent-space time evolution of complex fluid flows and probabilistic data recovery. This work extends to developing specific emulators for cosmological observables, including the matter power spectrum for both standard and modified gravity cosmologies, such as f(R) gravity, alongside facilitating emulator-based inference of crucial cosmological subgrid models.

A significant aspect of my contributions involves ensuring both the efficiency and reliability of these advanced AI tools. I have developed frameworks for interpretable uncertainty quantification in AI applications within High Energy Physics, ensuring that predictions are not only accurate but also accompanied by transparent measures of confidence. Additionally, I have focused on creating differentiable prediction models, exemplified by SHAMNet for large-scale structure, which allows for efficient gradient-based optimization and robust cosmological inference. These methodologies collectively accelerate the exploration of complex parameter spaces, enhance our ability to extract insights from data, and provide trustworthy predictions for fundamental scientific problems.

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
