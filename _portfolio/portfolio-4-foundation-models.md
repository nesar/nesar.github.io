---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models, particularly large language models (LLMs), are rapidly transforming various domains by exhibiting remarkable capabilities in understanding, generating, and reasoning with human language. Their potential to augment human intelligence and accelerate discovery is particularly compelling in specialized scientific fields, where the volume of data is immense and the complexity of information is high. However, applying these general-purpose models to highly technical disciplines, which often involve vast, complex, and rapidly evolving datasets, presents unique challenges regarding domain-specific accuracy and nuanced understanding.

One significant hurdle lies in fine-tuning or adapting these models to excel in specialized tasks, where precise terminology, intricate reasoning patterns, and the critical need for factual accuracy are paramount. Furthermore, traditional evaluation metrics, often designed for general language tasks, frequently fall short in assessing an AI’s true utility and reliability as a scientific tool. Therefore, developing both specialized models capable of deep domain expertise and robust methodologies for evaluating their performance as genuine scientific research assistants becomes essential for their widespread adoption and trustworthy integration into research workflows.

My research directly addresses these challenges by developing advanced, domain-specialized large language models tailored for complex scientific inquiry, particularly in astronomy. I have led the creation of models like AstroMLab 3 and AstroMLab 4, which demonstrate benchmark-topping performance in astronomy-specific question-answering. Notably, AstroMLab 3, an 8-billion-parameter model, achieves performance comparable to much larger, general-purpose models such as GPT-4o in domain-specific tasks, showcasing the efficiency and effectiveness of specialized training. Further, the 70-billion-parameter AstroMLab 4 exemplifies the power of scaling these domain-specialized reasoning models to deliver unparalleled accuracy and depth in scientific Q&A, significantly outperforming previous benchmarks in the field, as explored in work investigating "Who Wins Astronomy Jeopardy!?".

Beyond model development, a critical aspect of my work involves establishing rigorous methodologies for evaluating AI’s capabilities as scientific research assistants. Through the EAIRA (Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants) framework, I have developed a systematic approach to assess how well AI models can support and enhance the scientific discovery process. This moves beyond simple accuracy metrics to evaluate factors like reasoning capabilities, hypothesis generation, and data interpretation specific to scientific contexts. This work is fundamental to building trust and demonstrating the tangible value of AI in research, enabling astronomers and other scientists to leverage these powerful tools more effectively, accelerate knowledge discovery, and navigate the vast landscapes of scientific data with unprecedented efficiency.

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
