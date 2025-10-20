---
title: "General Machine Learning & Scientific Computing"
excerpt: "Research in general machine learning & scientific computing"
collection: portfolio
---

The convergence of machine learning and scientific computing has opened unprecedented avenues for understanding and simulating complex phenomena across various scientific and engineering disciplines. This interdisciplinary field seeks to leverage data-driven approaches to overcome computational bottlenecks, enhance predictive capabilities, and extract meaningful insights from intricate datasets. Key challenges include the efficient analysis of high-dimensional data, the reconstruction of global fields from limited measurements, the development of robust and accurate surrogate models for complex physical systems, and the crucial quantification of uncertainty in these predictions.

Addressing these challenges necessitates the development of advanced algorithms that can not only predict system behavior but also provide interpretable explanations for their outputs and rigorously quantify their confidence. Researchers in this domain focus on creating sophisticated models capable of learning intricate relationships from data, thereby enabling faster-than-real-time simulations, optimizing experimental design, and facilitating the discovery of underlying scientific principles. Particular emphasis is placed on developing reduced-order models (ROMs) for dynamic systems, probabilistic frameworks for uncertainty-aware predictions, and techniques for transforming raw data into disentangled, interpretable representations.

My research endeavors focus on developing and applying cutting-edge machine learning techniques to tackle these fundamental problems in scientific computing. I have developed robust probabilistic neural network (PNN) frameworks for fluid flow surrogate modeling and data recovery, which inherently quantify uncertainty in their predictions. This extends to latent-space time evolution of non-intrusive reduced-order models using Gaussian Process emulation, providing efficient and uncertainty-aware dynamics for complex systems. Furthermore, I have applied probabilistic modeling and automated machine learning (AutoML) frameworks to analyze and predict high-dimensional stress fields, ensuring both accuracy and robustness.

A significant part of my contribution lies in enhancing data reconstruction and interpretability. I have pioneered global field reconstruction from sparse sensors using a novel Voronoi tessellation-assisted deep learning approach, significantly improving the fidelity of reconstructions from limited data. Critically, my work also addresses the interpretability challenge in generative modeling by developing methods for statistically disentangled latent spaces. These are guided by generative factors in scientific datasets, providing clearer insights into the underlying physical mechanisms. Collectively, my contributions provide powerful, uncertainty-aware, and interpretable machine learning tools for accelerating scientific discovery and engineering design across diverse applications, from fluid dynamics to material science.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
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
