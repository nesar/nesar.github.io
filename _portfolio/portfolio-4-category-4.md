---
title: "Large Language Models & AI Scientific Assistants"
excerpt: "Research in large language models & ai scientific assistants"
collection: portfolio
---

The advent of large language models (LLMs) has ushered in a transformative era for artificial intelligence, offering unprecedented capabilities in natural language understanding and generation. These powerful models hold immense promise for accelerating scientific discovery by acting as intelligent research assistants, capable of synthesizing information, answering complex questions, and even aiding in data interpretation. However, realizing this potential within highly specialized scientific domains presents significant challenges. General-purpose LLMs often lack the deep contextual knowledge, precision, and reasoning abilities required for scientific inquiry, struggling with domain-specific terminology, intricate data analysis, and the rigorous standards of accuracy and verifiability inherent in scientific research.

Effectively integrating LLMs into scientific workflows necessitates a multi-faceted approach. This includes developing robust methodologies for adapting LLMs to specific scientific disciplines, creating specialized datasets and fine-tuning techniques to imbue them with expert knowledge, and, critically, establishing comprehensive frameworks for evaluating their performance and reliability. Without rigorous benchmarks and evaluation protocols, it remains challenging to ascertain the trustworthiness and utility of AI models as scientific collaborators, hindering their adoption in critical research applications.

My research directly addresses these challenges by advancing the development and evaluation of domain-specialized LLMs as scientific research assistants. I have focused on designing and implementing novel techniques to imbue LLMs with deep scientific expertise, particularly within astronomy and spectroscopy, and establishing methodologies for their systematic assessment. Through the AstroMLab series, I developed specialized large language models tailored for astronomy. This began with AstroMLab 1, which established initial benchmarks for AI performance in astronomy Q&A, culminating in AstroMLab 3 and AstroMLab 4. AstroMLab 3 demonstrated that a highly specialized 8B-parameter LLM could achieve GPT-4o level performance in astronomy, highlighting the efficiency gains possible with targeted domain adaptation. Building on this, AstroMLab 4 further pushed the boundaries with a 70B-parameter domain-specialized reasoning model, achieving benchmark-topping performance in complex astronomy Q&A tasks.

Beyond domain-specific model development, my work includes establishing robust evaluation frameworks. The EAIRA project, "Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants," introduces a systematic approach for assessing AI models’ capabilities and trustworthiness in research contexts, providing essential guidance for their responsible deployment. Furthermore, in "Teaching LLMs to Speak Spectroscopy," I have demonstrated innovative methods for enabling LLMs to interpret and reason with highly technical data types, such as spectroscopic measurements, extending their utility beyond text-based Q&A to analytical scientific tasks. Collectively, these contributions aim to significantly enhance the capability, reliability, and widespread applicability of AI as indispensable tools for scientific discovery.

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
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy in Astronomy with a Specialized 8B-Parameter Large Language Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy in Astronomy with a Specialized 8B-Parameter Large Language Model</div>
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
