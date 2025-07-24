---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The advent of large language models (LLMs) has revolutionized artificial intelligence, offering unprecedented capabilities in understanding and generating human-like text. As these "foundation models" continue to evolve, a critical frontier lies in adapting and specializing them for complex scientific domains. General-purpose LLMs, while powerful, often lack the deep domain-specific knowledge, nuanced reasoning abilities, and contextual understanding required to effectively address intricate scientific questions or function as reliable research assistants. This necessitates the development of specialized models trained on vast quantities of domain-specific data and rigorously evaluated against benchmarks that reflect real-world scientific challenges.

The challenge is two-fold: not only must these models achieve high accuracy on domain-specific tasks, but their performance also needs to be assessed through methodologies that accurately capture their utility in a scientific research workflow. This includes evaluating their ability to perform complex reasoning, synthesize information, and provide accurate, verifiable answers, moving beyond simple factual recall. Developing robust benchmarks and a systematic evaluation framework is paramount to establishing trust and efficacy in AI-powered scientific tools, ensuring they genuinely augment human research capabilities.

My research significantly contributes to this critical area by focusing on the development and rigorous evaluation of specialized foundation models for scientific applications, particularly in astronomy. Early work, such as "AstroMLab 1: Who Wins Astronomy Jeopardy!?," explored the initial capabilities and limitations of general LLMs in astronomy Q&A, laying the groundwork for more targeted development. Recognizing the need for a standardized approach to validate AI in scientific contexts, I subsequently established a comprehensive methodology in "EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants." This framework provides a robust lens through which to assess AI performance beyond mere accuracy, considering factors crucial for their role as scientific research assistants, including reasoning, trustworthiness, and utility.

Building on these foundations, I have developed a series of domain-specialized models, demonstrating exceptional performance in astronomy Q&A and reasoning. "AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model" showcases how a smaller, 8-billion-parameter model, through focused fine-tuning on astronomical data, can achieve performance comparable to leading general-purpose models like GPT-4o on domain-specific tasks. Further scaling this effort, "AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" introduces a 70-billion-parameter model that not only sets new benchmarks in astronomy Q&A but also excels in complex domain-specific reasoning, pushing the boundaries of what specialized AI can achieve in scientific inquiry. This body of work underscores the power of domain-specific adaptation and comprehensive evaluation in transforming foundation models into indispensable tools for scientific discovery.

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
