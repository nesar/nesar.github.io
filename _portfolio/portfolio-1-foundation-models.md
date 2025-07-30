---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models, particularly large language models (LLMs), have demonstrated transformative capabilities across diverse domains. However, their direct application in highly specialized scientific fields presents unique challenges related to factual accuracy, domain-specific reasoning, and the integration of complex scientific knowledge. Effectively leveraging these powerful models for scientific discovery and assistance necessitates tailored approaches to model development, data curation, and, crucially, robust evaluation methodologies that reflect the nuanced demands of scientific inquiry.

The field of astronomy, with its vast and ever-expanding datasets, intricate theoretical frameworks, and specialized terminology, serves as an excellent testbed for exploring the potential and limitations of AI as a scientific research partner. Developing AI systems that can accurately answer complex astronomical queries, synthesize information from diverse sources, and even propose new research directions requires not only massive computational resources but also a deep understanding of how to align AI capabilities with scientific rigor and human expert expectations.

My research program focuses on advancing the state-of-the-art in applying and adapting foundation models to scientific domains, particularly astronomy, with the ultimate goal of developing AI systems capable of serving as genuine scientific research assistants. Initially, in "AstroMLab 1: Who Wins Astronomy Jeopardy!?", I explored baseline capabilities and identified critical gaps in existing AI models when confronted with nuanced astronomical knowledge. Building on this, my work in "AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model" and "AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" involved developing and fine-tuning domain-specialized large language models. These models, leveraging 8 billion and 70 billion parameters respectively, were engineered to excel in astronomy Q&A, demonstrating benchmark-topping performance and achieving capabilities comparable to leading general-purpose models like GPT-4o within this specific scientific domain, a testament to the power of targeted specialization.

A cornerstone of this research is the rigorous evaluation of these AI systems. Recognizing the unique demands of scientific reliability, I established a comprehensive framework in "EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants." This methodology moves beyond simple accuracy metrics, focusing on aspects critical to scientific utility, such as reasoning capabilities, trustworthiness, and the ability to handle complex, multi-faceted scientific queries. Through these contributions, my work provides not only advanced, high-performing AI models for scientific applications but also establishes the vital methodological foundations for assessing and validating AI's role in future scientific discovery.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 1: Who Wins Astronomy Jeopardy!?" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 1: Who Wins Astronomy Jeopardy!?</div>
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
