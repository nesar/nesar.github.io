---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The advent of large language models (LLMs) has marked a significant shift in artificial intelligence, demonstrating remarkable capabilities across a wide array of general-purpose tasks. However, their direct application to highly specialized scientific domains, such as astrophysics, often encounters limitations. Generic LLMs typically lack the deep, nuanced domain-specific knowledge, the precise scientific reasoning abilities, and the contextual understanding required to effectively engage with complex scientific data, literature, and inquiry. This gap highlights a critical need for developing tailored AI solutions that can truly function as invaluable research assistants, capable of contributing meaningfully to scientific discovery.

Addressing this challenge necessitates the creation of domain-specialized foundation models. These models are meticulously trained and optimized on vast datasets pertinent to their specific scientific fields, enabling them to internalize expert knowledge and develop advanced reasoning capabilities. The goal is to transcend simple information retrieval, allowing these AI systems to interpret complex scientific questions, synthesize information from disparate sources, and even formulate hypotheses or suggest experimental avenues. Concurrently, establishing robust and scientifically rigorous methodologies for evaluating these AI models is paramount, ensuring their reliability, accuracy, and trustworthiness in assisting human researchers.

My research extensively explores the development and application of domain-specialized large language models designed to augment scientific research, primarily within astronomy. Initially, my work in "AstroMLab 1: Who Wins Astronomy Jeopardy!?" investigated the baseline performance of general-purpose LLMs on astronomy-specific question-answering tasks, highlighting their limitations and the clear necessity for more specialized approaches to achieve true scientific utility. This foundational analysis underscored the potential, yet also the substantial challenges, in leveraging AI for complex scientific inquiry.

Building upon these insights, I have developed the "AstroMLab" series, a collection of domain-specialized reasoning models tailored for astronomical applications. "AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model" demonstrated that even an 8-billion parameter model, when properly specialized, could achieve performance levels comparable to much larger general-purpose models like GPT-4o on astronomy-specific tasks. Further advancing this capability, "AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" introduced a more powerful 70-billion parameter model, achieving state-of-the-art results in astronomy question-answering, thereby setting new benchmarks for domain-specific AI. Complementing these model developments, my work in "EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" provides a critical framework for rigorously assessing the capabilities of AI models as scientific tools, ensuring their practical utility and scientific integrity. This comprehensive body of work significantly contributes to the field by demonstrating the immense potential of highly specialized foundation models to accelerate scientific discovery and enhance research productivity.

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
