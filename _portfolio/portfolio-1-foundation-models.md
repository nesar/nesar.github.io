---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The advent of foundation models has heralded a new era in artificial intelligence, demonstrating unparalleled capabilities in understanding and generating complex patterns across diverse data modalities. Applying these powerful models to scientific domains, particularly astronomy, presents a unique opportunity to accelerate discovery, automate complex analytical tasks, and extract novel insights from the ever-growing deluge of scientific data. This research area tackles the significant challenge of adapting general-purpose AI models to the highly specialized languages, intricate data structures, and rigorous reasoning demands inherent in scientific inquiry.

Scientific research often involves integrating information from disparate sources, including vast observational datasets, high-fidelity simulations, and expansive textual literature. Foundation models, especially those capable of multi-modal processing, are exceptionally well-suited to bridge these data silos. However, developing such models requires addressing domain-specific nuances, ensuring factual accuracy, and fostering robust scientific reasoning capabilities that can withstand expert scrutiny. A critical aspect of this work involves creating methodologies not only for building these advanced AI systems but also for rigorously evaluating their performance and trustworthiness as genuine scientific research assistants.

My work in this area focuses on developing and deploying specialized foundation models tailored for astronomical research, aiming to transform how scientists interact with data and literature. I have developed the AstroMLab series, which includes domain-specialized large language models (LLMs) ranging from an 8B-parameter model achieving GPT-4o level performance to a 70B-parameter model demonstrating benchmark-topping performance in astronomy Q&A. These models, as showcased in "AstroMLab 1: Who Wins Astronomy Jeopardy!?" and "AstroMLab 4," are designed to understand and answer complex astronomical queries with expert-level accuracy and reasoning.

Beyond textual understanding, I have contributed to multi-modal foundation models capable of interpreting diverse scientific data. For instance, my "Multi-modal Foundation Model for Cosmological Simulation Data" integrates visual, temporal, and numerical data from complex simulations, providing a holistic understanding of cosmological phenomena. Complementing this, "InferA: A Smart Assistant for Cosmological Ensemble Data" offers intelligent assistance for navigating and analyzing large-scale simulation outputs. Furthermore, I have developed specific methodologies, such as "Teaching LLMs to Speak Spectroscopy," to effectively embed highly technical scientific knowledge into these models, enabling them to decipher specialized data formats and terminologies. My research also extends to the practical application of these models for knowledge discovery, as demonstrated in "Predicting New Concept-Object Associations in Astronomy by Mining the Literature."

A cornerstone of my research involves establishing robust evaluation frameworks to ensure the reliability and utility of AI in scientific contexts. Through "EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants," I have created a rigorous approach for assessing the capabilities of these models, moving beyond simple accuracy metrics to evaluate their genuine contribution to the scientific process. This comprehensive body of work underscores my commitment to advancing the frontiers of AI for science, enabling new discoveries and streamlining the research pipeline through intelligent, domain-aware foundation models.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
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
