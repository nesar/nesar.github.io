---
title: "AI/ML Methodologies & Scientific Language Models"
excerpt: "Research in ai/ml methodologies & scientific language models"
collection: portfolio
---

The application of Artificial Intelligence and Machine Learning (AI/ML) is profoundly transforming scientific research, offering unprecedented capabilities for data analysis, complex system modeling, and hypothesis generation. This paradigm shift addresses the increasing volume and complexity of scientific datasets, enabling researchers to uncover hidden patterns, develop predictive models, and accelerate discovery across diverse domains. Core to this transformation is the development of robust methodologies that can not only achieve high performance but also provide interpretability and quantify uncertainty, which are crucial for scientific rigor and building trust in AI-driven insights.

A significant frontier in this evolving landscape involves specialized AI/ML techniques for modeling physical phenomena and the emerging field of domain-specific Scientific Language Models. Methodologies such as probabilistic modeling, deep learning for high-dimensional data, and reduced-order surrogate models are critical for tasks like global field reconstruction, fluid dynamics simulation, and stress field analysis, often requiring sophisticated approaches for uncertainty quantification and latent space disentanglement. Concurrently, the advent of large language models (LLMs) has opened avenues for building intelligent scientific assistants, necessitating the development of models capable of nuanced domain reasoning, understanding scientific "languages" like spectroscopy, and being rigorously evaluated for their efficacy as research tools.

My research significantly contributes to both pillars: advancing AI/ML methodologies for scientific problems and pioneering the development of specialized scientific language models. I have spearheaded the AstroMLab series, demonstrating how domain-specialized large language models can achieve benchmark-topping performance and even GPT-4o level capabilities in complex astronomy Q&A and reasoning tasks, often with significantly fewer parameters than general-purpose models. A key aspect of this work involves establishing robust methodologies, such as EAIRA, for evaluating AI models as scientific research assistants and developing techniques to "teach" LLMs to understand and speak the specific languages of science, exemplified by my work in enabling LLMs to interpret spectroscopy data.

Concurrently, I have developed and applied advanced AI/ML techniques to address critical challenges in scientific modeling. My contributions include enhancing interpretability in generative modeling through statistically disentangled latent spaces guided by generative factors, and developing innovative probabilistic neural networks and Gaussian process emulation for robust reduced-order surrogate modeling, particularly for complex fluid flows and high-dimensional stress fields. This work also focuses on interpretable uncertainty quantification in AI for high energy physics and global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning. My methodologies emphasize creating models that are not only accurate but also provide transparent insights and reliable uncertainty estimates, ultimately accelerating scientific discovery and building trust in AI-driven scientific tools.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants</div>
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
