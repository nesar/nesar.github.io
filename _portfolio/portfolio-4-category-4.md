---
title: "Scientific Machine Learning for Complex Physics"
excerpt: "Research in scientific machine learning for complex physics"
collection: portfolio
---

Scientific Machine Learning (SciML) has emerged as a transformative paradigm for understanding, predicting, and controlling complex physical systems, ranging from turbulent fluid flows to high-dimensional stress fields. Traditional simulation methods, such as Computational Fluid Dynamics (CFD) and Finite Element Analysis (FEA), are often computationally intensive, making real-time predictions, extensive parameter studies, and uncertainty quantification prohibitively expensive. SciML addresses these limitations by leveraging data-driven approaches, often infused with physics knowledge, to create efficient and accurate models capable of learning intricate relationships and dynamics within physical phenomena.

A primary focus within SciML is the development of reduced-order models (ROMs) and surrogate models, which aim to capture the essential dynamics of high-dimensional systems in a significantly lower-dimensional space, thereby drastically reducing computational costs. Furthermore, the ability to reconstruct complete physical fields from sparse sensor measurements is critical for experimental validation and practical deployment. Integrating probabilistic frameworks into these models is crucial for quantifying prediction uncertainty, a non-negotiable aspect for robust decision-making and safety-critical applications in engineering and scientific discovery.

My research focuses on developing advanced Scientific Machine Learning methodologies to tackle critical challenges in complex physics, with a particular emphasis on fluid dynamics and high-dimensional stress analysis. I have extensively developed probabilistic modeling techniques, including Probabilistic Neural Networks (PNNs), to construct robust reduced-order surrogates for fluid flows, enabling efficient prediction and crucial data recovery capabilities while quantifying the inherent uncertainties in predictions. This work extends to modeling the latent-space time evolution of non-intrusive reduced-order models using Gaussian Process emulation, providing a powerful framework for capturing complex dynamic behaviors with uncertainty estimates.

In parallel, I have developed techniques for global field reconstruction from sparse sensor data, utilizing a novel Voronoi tessellation-assisted deep learning approach to accurately infer full fields from limited measurements. This is complemented by my work on applying automated machine learning (AutoML) frameworks coupled with probabilistic modeling for efficiently handling high-dimensional stress fields, streamlining the model development process. My contributions aim to provide computationally efficient, accurate, and uncertainty-aware machine learning solutions that significantly advance our capability to model, predict, and control complex physical systems under various conditions.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/global-field-reconstruction-from-sparse-sensors-wi_plot_1_93ef286c.png" alt="Figure from Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
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
