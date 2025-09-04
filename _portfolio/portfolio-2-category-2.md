---
title: "AI/ML Methodologies & Scientific Computing"
excerpt: "Research in ai/ml methodologies & scientific computing"
collection: portfolio
---

The intersection of Artificial Intelligence (AI), Machine Learning (ML), and Scientific Computing presents transformative opportunities for accelerating discovery and engineering innovation. This field focuses on developing advanced computational methodologies to address complex challenges in science and engineering, ranging from understanding intricate physical phenomena to managing vast scientific datasets. Key areas of investigation include the development of robust surrogate models, the interpretation of high-dimensional data, and the quantification of uncertainty inherent in AI-driven predictions.

Researchers in this domain are particularly concerned with transcending the "black-box" nature of many AI models, seeking to imbue them with greater interpretability and provide reliable estimates of their predictive confidence. This involves developing novel approaches for uncertainty quantification (UQ) and designing models that can statistically disentangle underlying generative factors. Applications span diverse scientific disciplines, including fluid dynamics, materials science, and high-energy physics (HEP), where AI/ML methods are employed for tasks such as data recovery, real-time simulation, and the efficient exploration of complex parameter spaces.

My research endeavors specifically address these challenges, focusing on the development and application of advanced AI/ML methodologies to enhance scientific computing capabilities. I have developed probabilistic neural networks (PNNs) and integrated Gaussian process emulation for reduced-order surrogate modeling, particularly for complex fluid flows, enabling efficient simulation and data recovery while providing crucial uncertainty estimates. A significant aspect of my work also includes establishing a systematic methodology, EAIRA, for evaluating AI models as scientific research assistants, ensuring their rigorous assessment in scientific contexts.

Furthermore, my contributions extend to enhancing interpretability and uncertainty quantification in AI for high-energy physics, through methods that generate statistically disentangled latent spaces guided by generative factors in scientific datasets. I have also pioneered techniques for global field reconstruction from sparse sensor data using Voronoi tessellation-assisted deep learning, providing robust solutions for data-limited scenarios. This includes applying probabilistic modeling and automated machine learning frameworks to analyze high-dimensional stress fields. Collectively, my work aims to create more reliable, interpretable, and computationally efficient AI/ML tools that empower scientific discovery and foster data-driven innovation across various scientific and engineering disciplines.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
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
