---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models, particularly large language models (LLMs), have emerged as transformative technologies with the potential to revolutionize various domains, including scientific research. Their unprecedented ability to process and generate human-like text makes them powerful tools for information retrieval, synthesis, and complex problem-solving. In scientific disciplines, these models offer the promise of accelerating discovery by assisting with literature review, hypothesis generation, and data interpretation, thereby reducing the burden of manual information processing on researchers and enabling new modes of inquiry.

However, the application of general-purpose foundation models to highly specialized scientific fields presents unique challenges. Issues such as factual inaccuracies, known as hallucinations, and a lack of deep domain-specific knowledge often limit their immediate utility in research settings. This necessitates the development of domain-specialized models tailored to the nuances and vast knowledge bases of particular sciences, alongside robust methodologies for their rigorous evaluation. Establishing how well these AI models can function as reliable scientific research assistants requires going beyond simple accuracy metrics to assess their capacity for complex reasoning, knowledge application, and utility in actual research workflows.

My research in this area focuses on pushing the boundaries of what specialized foundation models can achieve in astronomy. I have developed and rigorously tested domain-specialized large language models designed to excel in astronomical question-answering and reasoning. For instance, my work includes a 70B-parameter domain-specialized reasoning model that has achieved benchmark-topping performance in astronomy Q&A. Demonstrating an emphasis on efficiency and accessibility, I have also developed an 8B-parameter specialized model that achieves performance levels comparable to general-purpose models like GPT-4o in the astronomy domain, showcasing the power of focused specialization over sheer size. This has been concretely exemplified through applications like "Astronomy Jeopardy!", which serves as a challenging benchmark for evaluating the models' deep understanding and reasoning capabilities within the field.

A crucial aspect of my contribution extends beyond model development to the establishment of robust evaluation frameworks. Recognizing the limitations of traditional metrics for scientific AI, I developed EAIRA (Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants). This methodology provides a systematic approach to assess an AI's utility as a research assistant, focusing on its ability to perform complex scientific tasks, synthesize information, and avoid erroneous or misleading outputs critical for scientific integrity. Through this integrated approach of specialized model development and rigorous, context-aware evaluation, my work aims to unlock the full potential of foundation models to genuinely augment scientific discovery and assist researchers in navigating the ever-growing complexities of modern science.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 1: Who Wins Astronomy Jeopardy!?" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 1: Who Wins Astronomy Jeopardy!?</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_2_0a77f6ec.png" alt="Figure from AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_2_205db31f.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
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
