---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a paradigm shift in artificial intelligence, characterized by their immense scale and pre-training on vast and diverse datasets. These models, often large language models (LLMs), exhibit remarkable emergent capabilities across a wide range of tasks, from natural language understanding and generation to complex reasoning and problem-solving. While powerful in general applications, their utility in highly specialized, knowledge-intensive domains often benefits from further adaptation and refinement.

Applying foundation models to scientific disciplines presents both unique opportunities and challenges. Scientific research, particularly in fields like astronomy, involves complex concepts, specialized terminology, and the synthesis of information from extensive, constantly evolving data archives. General-purpose models, despite their breadth, often struggle with the nuanced precision and deep domain-specific reasoning required for advanced scientific inquiry, necessitating tailored approaches and robust evaluation methodologies.

Establishing the efficacy of AI models as tools for scientific research demands rigorous evaluation frameworks. These frameworks must go beyond simple accuracy metrics, assessing qualities like factual consistency, reasoning ability, and the capacity to function as reliable research assistants. The development of specialized benchmarks and methodologies is thus paramount to ensure these advanced AI systems genuinely augment human scientific endeavors, providing accurate and trustworthy insights within their specific domains.

My research addresses these challenges by developing and evaluating highly specialized foundation models for the field of astronomy. I initiated this work by exploring baseline performance with AstroMLab 1, a foundational step in understanding how AI could tackle astronomy-specific queries. Building upon this, I have developed the AstroMLab series of large language models, specifically engineered to excel in astronomy-related question answering and scientific reasoning. AstroMLab 3, for instance, demonstrated the remarkable capability of achieving performance levels comparable to general-purpose models like GPT-4o, but with significantly fewer parameters (8 billion), highlighting the efficiency and power of domain-specialized training and fine-tuning.

Further advancing this work, AstroMLab 4 pushed the boundaries by developing a 70-billion-parameter model that achieved benchmark-topping performance in complex astronomy Q&A tasks, showcasing enhanced reasoning capabilities critical for scientific discovery. Alongside model development, I have also established a rigorous framework for evaluating AI models as scientific research assistants through the EAIRA methodology. This systematic approach provides a robust means to assess the utility and reliability of these AI systems. My work therefore significantly contributes to bridging the gap between general AI capabilities and the specific demands of cutting-edge scientific research, demonstrating the transformative potential of domain-specialized foundation models.

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
