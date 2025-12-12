---
title: "Foundation Models for Science"
excerpt: "Research in foundation models for science"
collection: portfolio
---

Foundation models are emerging as a transformative paradigm across numerous scientific disciplines, offering unprecedented capabilities for processing, interpreting, and generating insights from vast and complex datasets. These powerful AI systems, trained on diverse and extensive data, hold immense potential to accelerate scientific discovery by automating tedious tasks, identifying subtle patterns, and facilitating deeper understanding. In fields such as astrophysics and cosmology, researchers are constantly faced with a deluge of multi-modal data stemming from telescope observations, intricate numerical simulations, and theoretical models. Navigating and extracting meaningful scientific knowledge from these massive and heterogeneous datasets often requires specialized expertise and significant computational resources, presenting a major bottleneck in the research workflow.

The application of foundation models in science aims to address these challenges by providing intelligent tools that can handle the scale and complexity inherent in modern scientific inquiry. By developing models capable of understanding not just human language but also scientific notations, data formats, and domain-specific concepts, researchers can unlock new avenues for exploration. These models can act as advanced assistants, capable of performing tasks from data analysis and hypothesis generation to literature review and experimental design, thereby empowering scientists to focus on higher-level conceptual challenges and innovation.

My research focuses on the development and rigorous evaluation of specialized foundation models designed to enhance scientific inquiry, particularly within astronomy and cosmology. I have pioneered the creation of highly effective, domain-specialized large language models (LLMs) and multi-modal foundation models that exhibit outstanding performance on complex scientific tasks. For instance, the AstroMLab series of models, including AstroMLab 1, 3, and 4, has demonstrated benchmark-topping capabilities in astronomy question-answering, achieving performance comparable to or exceeding generalist models like GPT-4o while using significantly fewer parameters (e.g., an 8B-parameter model). These models are engineered to perform not just factual recall but also sophisticated, domain-specific reasoning, as showcased by their success in challenging contexts like "Astronomy Jeopardy!".

Beyond textual question-answering, my work extends to the interpretation of diverse scientific data modalities. I have developed InferA, a smart assistant specifically designed to help scientists navigate and derive insights from complex cosmological ensemble data, streamlining the analysis process. Furthermore, I have engineered multi-modal foundation models for directly analyzing cosmological simulation data, integrating various data types to construct a more comprehensive understanding of cosmic phenomena. A critical area of my contribution involves "Teaching LLMs to Speak Spectroscopy," endowing these models with the ability to interpret and reason about spectroscopic data, which is fundamental for understanding the composition and dynamics of celestial objects. To ensure the reliability and utility of these advanced tools, I established EAIRA, a comprehensive methodology for systematically evaluating AI models as scientific research assistants, providing a framework to assess their performance, trustworthiness, and overall impact on scientific workflows.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/infera-a-smart-assistant-for-cosmological-ensemble_plot_1_590fdcf1.png" alt="Figure from InferA: A Smart Assistant for Cosmological Ensemble Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: InferA: A Smart Assistant for Cosmological Ensemble Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
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
