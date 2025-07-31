---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The application of large language models (LLMs) and other foundation models is rapidly transforming various scientific disciplines by offering powerful new tools for data analysis, knowledge synthesis, and problem-solving. While general-purpose LLMs demonstrate impressive capabilities across a wide array of tasks, their inherent limitations in deep domain-specific knowledge and reasoning often hinder their utility in highly specialized fields like astrophysics. Addressing this gap requires the development of tailored models that combine the architectural sophistication of foundation models with expert knowledge of a specific scientific domain, along with robust methodologies for evaluating their performance and utility in research contexts.

Research in this area has focused on establishing a systematic approach to developing and assessing domain-specific artificial intelligence for scientific inquiry. This includes exploring the baseline performance of general AI in scientific knowledge tasks, progressing to the engineering of highly specialized LLMs. Key efforts involve demonstrating how targeted training and architectural choices can imbue models with deep scientific understanding, enabling them to perform complex reasoning and answer nuanced questions within a specific discipline. A crucial component of this work also lies in establishing comprehensive evaluation methodologies that move beyond simplistic accuracy metrics to genuinely assess an AI model's effectiveness as a scientific research assistant.

My work has systematically explored the development and rigorous evaluation of domain-specialized large language models for complex scientific applications, particularly within astronomy. I have engineered the AstroMLab series of models, showcasing how targeted specialization can lead to unprecedented performance. For example, my research introduced AstroMLab 3, an 8-billion-parameter model that achieves GPT-4o level performance in astronomy question-answering, demonstrating the efficiency and efficacy of smaller, specialized models. Building on this, AstroMLab 4, a 70-billion-parameter domain-specialized reasoning model, was developed to deliver benchmark-topping performance in astronomy Q&A, further pushing the boundaries of what is achievable with large-scale, fine-tuned models.

Crucially, I also established EAIRA, a comprehensive methodology for evaluating AI models as scientific research assistants. This framework allows for a more nuanced assessment of AI's utility, moving beyond simple factual recall to evaluate models on their ability to support scientific workflows, generate hypotheses, and aid in complex problem-solving. My research, beginning with early explorations like "AstroMLab 1: Who Wins Astronomy Jeopardy!?," consistently underscores the immense potential of tailoring foundation models to specific scientific disciplines, paving the way for a new generation of intelligent, reliable AI collaborators that can significantly accelerate scientific discovery.

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
