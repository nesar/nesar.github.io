---
title: "Advanced AI/ML Methodology & General Scientific Applications"
excerpt: "Research in advanced ai/ml methodology & general scientific applications"
collection: portfolio
---

The integration of advanced artificial intelligence and machine learning methodologies is increasingly pivotal for accelerating scientific discovery and engineering innovation across diverse domains. A critical focus is the development of AI systems that transcend black-box prediction, offering transparency, reliability, and meaningful interpretability. This involves crafting models that explain their reasoning, rigorously quantify uncertainties, and provide scientific insights resonant with physical principles. Such advancements are essential for fostering trust and enabling researchers to confidently leverage AI/ML for complex scientific challenges.

A significant thrust involves building robust AI frameworks for high-stakes scientific data. This includes pioneering probabilistic machine learning models that inherently quantify uncertainty, crucial for high-energy physics and fluid dynamics. Furthermore, efforts are dedicated to constructing interpretable generative models, where latent spaces reflect meaningful physical factors, thereby enhancing our understanding of data generation. The development of efficient reduced-order models (ROMs) through the integration of deep learning with classical scientific modeling is also key for accurately and efficiently simulating complex phenomena, overcoming computational bottlenecks while preserving physical consistency.

My research extensively contributes to these critical areas by developing and applying advanced AI/ML methodologies specifically tailored for general scientific applications, with a consistent emphasis on interpretability, robustness, and efficiency, particularly in uncertainty quantification. I have developed novel techniques for enhancing interpretability in generative modeling through the creation of statistically disentangled latent spaces, guided by generative factors intrinsic to scientific datasets. This work allows for a clearer understanding and control over complex data generation processes. Furthermore, I established EAIRA, a comprehensive methodology for rigorously evaluating AI models in their capacity as scientific research assistants, thereby ensuring their utility and reliability within a demanding research environment.

My work extensively leverages probabilistic modeling to address both uncertainty and efficiency in complex systems. I have developed and applied probabilistic neural networks (PNNs) for robust fluid flow surrogate modeling, data recovery, and as powerful reduced-order surrogates. These PNNs inherently provide interpretable uncertainty quantification, crucial for high-dimensional stress fields and high-energy physics investigations. Moreover, I have introduced innovative approaches for global field reconstruction from sparse sensor data using Voronoi tessellation-assisted deep learning, and advanced the latent-space time evolution of non-intrusive reduced-order models through Gaussian process emulation. This significantly improves the efficiency and accuracy of simulating dynamic scientific systems, showcasing my commitment to AI/ML solutions that explain, quantify, and accelerate scientific discovery.

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
