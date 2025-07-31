---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The emergence of large-scale foundation models has revolutionized artificial intelligence, demonstrating remarkable capabilities across diverse tasks. While these models exhibit strong general-purpose reasoning and language understanding, their direct application in highly specialized scientific domains often presents challenges related to factual accuracy, domain-specific nuance, and deep analytical reasoning. Achieving high performance and reliability for scientific research, particularly in fields with complex data and intricate theoretical frameworks like astrophysics, necessitates a focused approach that combines foundational model strengths with targeted domain expertise.

Research in this area has therefore concentrated on developing methodologies and specialized models that can bridge this gap, ensuring that AI systems are not merely conversational tools but become robust, reliable scientific assistants. This involves establishing rigorous benchmarking frameworks to quantify performance, developing evaluation methodologies tailored to scientific tasks, and architecting models specifically designed to leverage domain knowledge. The goal is to push the boundaries of AI's utility in scientific discovery, enabling models to accurately answer complex questions, synthesize information, and even contribute to the research process itself.

My research directly addresses these critical needs within the context of astronomy and astrophysics. I have developed a series of domain-specialized large language models, known as AstroMLab, designed to achieve state-of-the-art performance in astronomical question-answering and reasoning. For instance, AstroMLab 3, an 8-billion-parameter model, was engineered to reach performance levels comparable to GPT-4o in astronomy-specific tasks. Building on this, AstroMLab 4 is a 70-billion-parameter domain-specialized reasoning model that has achieved benchmark-topping performance in astronomy Q&A, demonstrating the power of scale combined with targeted domain fine-tuning for complex scientific inquiry.

Beyond model development, a significant part of my contribution involves establishing robust methodologies for evaluating AI models as scientific research assistants. Through the EAIRA framework, I have defined a systematic approach to assess the capabilities of AI in supporting scientific endeavors, moving beyond simple accuracy metrics to evaluate factors like reasoning, trustworthiness, and utility in a research context. My work also includes pioneering competitive benchmarking scenarios, such as the "Astronomy Jeopardy!" challenge from AstroMLab 1, to rigorously test and quantify the practical knowledge and reasoning abilities of these models in a challenging, knowledge-intensive environment. This comprehensive approach ensures that the developed AI systems are not only powerful but also verifiably effective and reliable tools for the scientific community.

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
