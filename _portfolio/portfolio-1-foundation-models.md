---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The rapid advancements in large language models, often referred to as foundation models, have opened unprecedented opportunities for transforming various specialized domains, including the sciences. These models possess an extraordinary capacity to process, synthesize, and generate human-like text, making them promising candidates for aiding complex tasks such as information retrieval, data analysis, and scientific reasoning. However, effectively deploying general-purpose models in highly technical fields like astronomy requires overcoming significant challenges, primarily concerning domain-specific knowledge acquisition, nuanced reasoning capabilities, and robust evaluation methodologies tailored to scientific rigor.

Research in this area focuses on bridging the gap between general AI capabilities and the specific demands of scientific inquiry. A critical aspect involves developing highly specialized models that can demonstrate deep understanding and accurate reasoning within a given scientific discipline, moving beyond mere factual recall to enable genuine scientific assistance. Furthermore, establishing comprehensive and objective frameworks for evaluating the performance of AI models in scientific contexts is paramount. Such methodologies ensure that these intelligent assistants not only perform well on general benchmarks but also meet the stringent requirements of accuracy, reliability, and interpretability necessary for scientific research.

My work has centered on pioneering the development and evaluation of domain-specialized large language models for astronomy. I have specifically focused on creating powerful AI agents capable of high-level reasoning and accurate knowledge retrieval within this complex scientific field. For instance, I developed the AstroMLab series of models, progressing from initial explorations into AI's capabilities in astronomy through benchmarks like "Astronomy Jeopardy!", to highly performant, specialized architectures. This progression includes AstroMLab 3, an 8-billion parameter model that achieved performance on par with GPT-4o in astronomy-specific tasks, and culminated with AstroMLab 4, a 70-billion parameter domain-specialized reasoning model that established new benchmark-topping performance in astronomy question-answering.

Beyond model development, I have also contributed significantly to the methodological rigor of AI evaluation in scientific domains. Recognizing the need for standardized and robust assessment, I established EAIRA (Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants). This framework provides a systematic approach for rigorously testing and validating AI models' utility as scientific research assistants, moving beyond simple accuracy metrics to encompass reasoning, interpretability, and practical applicability. Through these contributions, my research aims to accelerate scientific discovery by building and validating intelligent AI tools that truly augment human expertise in specialized fields like astronomy.

<div class="no-figures"><p>Representative figures will be added soon.</p></div>

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
