---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a paradigm shift in artificial intelligence, demonstrating remarkable capabilities across diverse tasks through their large scale and pre-training on vast datasets. While general-purpose foundation models have achieved significant milestones, their direct application to highly specialized scientific domains often faces limitations due to the unique characteristics of scientific data, terminology, and reasoning requirements. Fields such as astrophysics and cosmology, characterized by colossal and intricate datasets derived from simulations and observational instruments, present a particularly fertile ground for the development of domain-adapted foundation models. These specialized models are crucial for extracting insights, accelerating discovery, and handling the immense complexity inherent in modern scientific research.

The unique challenges in scientific contexts include processing multi-modal data—ranging from numerical simulations and observational images to spectroscopic measurements and complex textual literature—and performing sophisticated, context-aware reasoning. Generic models frequently struggle with the nuanced understanding of scientific jargon, the interpretation of highly specialized data formats, and the intricate logical steps required for hypothesis generation or experiment design. Therefore, developing foundation models explicitly designed and trained for scientific applications is imperative. These models aim to bridge the gap between raw scientific data and actionable knowledge, serving as intelligent assistants that can augment human expertise and computational power in the scientific discovery pipeline.

My research has focused on pioneering the development and rigorous evaluation of domain-specialized foundation models tailored for astrophysics and cosmology. A cornerstone of this effort is the AstroMLab series, which established rigorous benchmarks and methodologies for assessing the performance of Large Language Models (LLMs) in scientific domains. Beginning with 'AstroMLab 1: Who Wins Astronomy Jeopardy!?', I explored the nascent capabilities of LLMs in astronomy Q&A. This work advanced significantly with 'AstroMLab 3,' where I developed an 8B-parameter specialized LLM achieving GPT-4o level performance in astronomy, demonstrating that smaller, domain-focused models can rival much larger general-purpose counterparts. Further pushing these boundaries, 'AstroMLab 4' introduced a 70B-parameter domain-specialized reasoning model that set new benchmark-topping performance for complex astronomy Q&A, showcasing the immense potential of deeply specialized architectures for scientific reasoning.

Beyond textual understanding, I have extended these capabilities to multi-modal scientific data. My work on a 'Multi-modal Foundation Model for Cosmological Simulation Data' enables comprehensive analysis and interpretation of complex simulation outputs, while 'Teaching LLMs to Speak Spectroscopy' addresses the critical challenge of extracting insights from detailed spectroscopic measurements. Furthermore, I developed 'InferA: A Smart Assistant for Cosmological Ensemble Data,' designed to streamline the analysis of vast datasets. To ensure the reliability and efficacy of these tools, I established a robust evaluation framework in 'EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants.' Collectively, this research demonstrates that specialized foundation models can act as powerful scientific research assistants, capable of complex reasoning, multi-modal data interpretation, and significantly accelerating the pace of discovery in astrophysics and cosmology.

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
