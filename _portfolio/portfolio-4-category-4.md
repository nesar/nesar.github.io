---
title: "Advanced AI/ML Methodologies"
excerpt: "Research in advanced ai/ml methodologies"
collection: portfolio
---

The study of complex physical phenomena and high-dimensional scientific datasets presents significant challenges across engineering and scientific disciplines. Effectively predicting system behavior, optimizing designs, and understanding underlying mechanisms often requires advanced computational tools that can handle vast amounts of data, propagate uncertainties, and operate efficiently. Traditional simulation methods can be computationally prohibitive, while empirical approaches may lack generalizability or fail to capture intricate interdependencies. This necessitates the development of sophisticated artificial intelligence and machine learning methodologies to accelerate discovery and enhance decision-making.

A core focus in this area involves advancing techniques for surrogate modeling, uncertainty quantification, and interpretability. Surrogate models, particularly reduced-order models, aim to replace expensive high-fidelity simulations with faster, data-driven approximations. Integrating probabilistic frameworks is crucial for quantifying the inherent uncertainties in complex systems and making robust predictions. Furthermore, with the increasing complexity of AI models, ensuring interpretability is paramount, especially in scientific contexts where understanding the "why" behind predictions is as important as the predictions themselves. Addressing these challenges enables more rapid exploration of design spaces, real-time control, and a deeper scientific understanding of systems ranging from turbulent fluid flows to material stress fields.

My research systematically addresses these critical challenges by developing and applying advanced AI/ML methodologies. I have focused on enhancing interpretability in generative modeling by designing frameworks that achieve statistically disentangled latent spaces, guided by known generative factors in scientific datasets. This approach provides clearer insights into the underlying mechanisms driving data generation. Furthermore, I have developed and applied robust probabilistic modeling and automated machine learning frameworks, specifically tailored for analyzing high-dimensional stress fields, allowing for a comprehensive understanding of complex mechanical behaviors while quantifying associated uncertainties.

My work extends to developing efficient and reliable surrogate models for computationally intensive simulations, particularly in fluid dynamics. I have engineered probabilistic neural networks to create reduced-order surrogates for fluid flows, providing both accurate predictions and a quantification of predictive uncertainty. Complementing this, I have explored latent-space time evolution for non-intrusive reduced-order models using Gaussian process emulation, which offers a powerful way to evolve system dynamics efficiently in a compressed representation. Additionally, I have pioneered methods for global field reconstruction from sparse sensor data, utilizing deep learning techniques assisted by Voronoi tessellation to accurately recover complete spatial fields from limited observations. Through these contributions, my goal is to enable more efficient analysis, prediction, and understanding of complex scientific and engineering systems.

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
