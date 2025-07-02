---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The burgeoning field of foundation models, particularly large language models (LLMs), has demonstrated remarkable general-purpose capabilities across diverse tasks. However, their direct application to complex scientific domains often faces limitations due to a lack of specialized knowledge, nuanced reasoning abilities, and the precision required for scientific inquiry. While general models can synthesize information, their capacity for deep scientific reasoning, hypothesis generation, and accurate interpretation of domain-specific data remains a significant challenge. Bridging this gap requires developing models that not only possess extensive factual knowledge but also exhibit advanced reasoning and problem-solving skills tailored to the unique demands of scientific research.

Specialized scientific disciplines, such as astronomy, present a unique testbed for advancing foundation model capabilities. These fields demand an understanding of complex theoretical frameworks, observational data, and intricate interconnections between vast datasets. Moreover, the utility of AI in scientific discovery hinges not just on raw performance, but on a robust and systematic methodology for evaluating their efficacy as genuine research assistants. This includes assessing their ability to answer complex questions, synthesize information, and contribute meaningfully to the scientific process, moving beyond simple knowledge recall towards true scientific reasoning and insight generation.

My research endeavors have focused on addressing these challenges by developing and rigorously evaluating domain-specialized large language models within the field of astronomy. Through the AstroMLab series, I have pioneered the creation of models specifically engineered for scientific question-answering and reasoning. This includes AstroMLab 3, an 8-billion-parameter model that achieved performance comparable to highly advanced general models like GPT-4o in astronomy-specific tasks, demonstrating the significant gains achievable through domain specialization. Building on this, I further developed AstroMLab 4, a 70-billion-parameter domain-specialized reasoning model that exhibited benchmark-topping performance in complex astronomy Q&A, proving that targeted architectural and training approaches can push the boundaries of AI capabilities in scientific contexts.

Beyond model development, a critical contribution of my work lies in establishing methodologies for effectively evaluating these AI systems as genuine scientific research assistants. My research, specifically highlighted in EAIRA, introduces a systematic framework for assessing AI models not just on factual recall, but on their reasoning depth, capacity for information synthesis, and overall utility in accelerating scientific discovery. Early work, such as "AstroMLab 1: Who Wins Astronomy Jeopardy!?", laid the groundwork for robust, game-theoretic evaluation of domain knowledge. This comprehensive approach ensures that the developed foundation models are not merely performant, but are truly capable of serving as valuable tools for researchers, enabling more efficient and insightful scientific exploration.

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
