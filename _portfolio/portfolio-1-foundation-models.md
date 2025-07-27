---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The burgeoning field of Foundation Models, particularly Large Language Models (LLMs), has ushered in a new era of AI capabilities, demonstrating remarkable proficiency across a wide array of general-purpose tasks. These models, trained on vast datasets, serve as powerful baselines for diverse applications, from natural language understanding to complex reasoning. However, their direct application to specialized scientific domains often encounters limitations, including the potential for factual inaccuracies, a lack of deep domain-specific reasoning, and challenges in rigorously evaluating their utility in complex research workflows. Bridging this gap requires the development of highly specialized models and robust methodologies for their assessment within scientific contexts.

The application of AI in scientific research, especially in data-rich fields like astronomy, presents both significant opportunities and unique challenges. Scientific inquiry demands precision, nuanced understanding of complex concepts, and the ability to synthesize information from vast and often disparate sources. General-purpose LLMs, while capable of broad knowledge retrieval, may struggle with the intricate, often counter-intuitive, and highly technical concepts inherent in advanced scientific disciplines. This necessitates a targeted approach to developing AI systems that can not only access but also accurately interpret, reason about, and contribute to scientific knowledge.

My research portfolio focuses on the critical area of adapting and advancing Foundation Models for high-stakes scientific applications, particularly within the field of astronomy. I have developed a series of domain-specialized Large Language Models, collectively known as AstroMLab, designed to excel in astronomical knowledge retrieval and complex reasoning tasks. AstroMLab 1, for instance, explored the potential of AI in a "Jeopardy!"-style astronomy Q&A format, laying the groundwork for more advanced capabilities. Building on this, AstroMLab 3 showcased the development of an 8B-parameter LLM capable of achieving GPT-4o level performance in astronomy-specific contexts, demonstrating that highly performant models can be developed efficiently for specialized domains. Furthermore, AstroMLab 4 introduced a 70B-parameter domain-specialized reasoning model that achieved benchmark-topping performance in astronomy Q&A, highlighting the efficacy of large-scale, targeted specialization for superior scientific accuracy.

A core contribution of my work extends beyond model development to the crucial aspect of rigorous evaluation. Recognizing the need for standardized and reliable assessment of AI in scientific roles, I established EAIRA: a comprehensive methodology for evaluating AI models as scientific research assistants. This framework provides a systematic approach to measure an AI's factual accuracy, reasoning capabilities, and overall utility in assisting scientific inquiry, addressing the inherent complexities of assessing AI in a research context. Through these efforts, I aim to advance the state-of-the-art in specialized Foundation Models, providing powerful, accurate, and reliably evaluated AI tools that genuinely accelerate scientific discovery and assist researchers.

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
