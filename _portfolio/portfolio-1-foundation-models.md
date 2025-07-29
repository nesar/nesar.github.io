---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models, particularly large language models, represent a transformative paradigm in artificial intelligence, demonstrating remarkable capabilities across diverse tasks. Their application in specialized domains, however, presents unique challenges related to data scarcity, domain-specific terminology, and the need for high-fidelity reasoning. Successfully deploying these models in scientific research necessitates not only adapting their architecture and training but also developing rigorous methodologies to assess their reliability and performance within complex scientific contexts.

The field of astronomy, with its vast and ever-growing datasets, intricate theoretical frameworks, and specialized terminology, is an ideal candidate for leveraging advanced AI. Automating knowledge retrieval, assisting with complex data analysis, and facilitating scientific inquiry through natural language interaction are critical areas. While general-purpose LLMs offer a starting point, achieving truly impactful performance requires models specifically trained and fine-tuned on astronomical knowledge, alongside robust evaluation frameworks to benchmark their efficacy as genuine scientific tools.

My research focuses on pioneering the development and evaluation of domain-specific foundation models tailored for the demanding scientific inquiry within astronomy. Through the AstroMLab series, I have developed specialized large language models that demonstrate unprecedented capabilities in astronomical question-answering and complex reasoning. Specifically, AstroMLab 3, an 8-billion parameter model, achieved performance on par with generalist models like GPT-4o in astronomy benchmarks, showcasing the power of domain specialization even with smaller model sizes. Furthermore, AstroMLab 4, a 70-billion parameter domain-specialized reasoning model, has set new benchmarks, delivering top-tier performance in comprehensive astronomy Q&A tasks that require deep factual recall and sophisticated inferential reasoning.

A cornerstone of my work involves establishing rigorous methodologies for evaluating AI models as bona fide scientific research assistants. The EAIRA framework provides a systematic approach to assess the utility, accuracy, and reliability of AI systems in scientific contexts, moving beyond simple accuracy metrics to evaluate their true potential for accelerating discovery. This methodical evaluation, initially explored in AstroMLab 1 through a "Jeopardy!"-style challenge, underpins the development of increasingly capable models. My contributions emphasize not only building high-performing specialized models but also ensuring their utility and trustworthiness through robust, scientifically sound evaluation protocols, thereby facilitating their integration into the scientific workflow and enhancing researchers' access to complex astronomical knowledge.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_3_1c174bef.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
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
