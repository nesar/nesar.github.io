---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The burgeoning field of artificial intelligence, particularly large language models (LLMs) and foundation models, presents transformative potential across scientific disciplines. These models, pre-trained on vast datasets, demonstrate remarkable capabilities in understanding, generating, and reasoning with human language. However, their direct application in highly specialized scientific domains often encounters limitations due to the nuanced, technical, and often data-scarce nature of scientific knowledge. A key area of research focuses on adapting and specializing these powerful general-purpose models to excel in specific scientific contexts, thereby enabling new paradigms for scientific discovery and research assistance.

A critical challenge in integrating AI into scientific workflows lies in developing models that can not only retrieve information but also perform complex reasoning, synthesize knowledge, and provide accurate, domain-specific answers. This necessitates moving beyond generic capabilities towards architecting and training models specifically attuned to the intricacies of scientific discourse, data, and methodologies. Furthermore, robust and standardized methodologies are essential for rigorously evaluating the performance of these AI agents as true scientific research assistants, ensuring their reliability and utility in real-world research environments. This research explores these frontiers, focusing on the specialized application and systematic evaluation of AI in astronomy.

My research has significantly contributed to advancing the practical application of foundation models in specialized scientific domains, particularly astronomy. I have developed the AstroMLab series of domain-specialized large language models, demonstrating that highly performant and efficient AI solutions can be crafted for specific scientific challenges. For instance, AstroMLab 3, an 8-billion-parameter model, achieved performance levels comparable to GPT-4o in astronomy question-answering, highlighting the efficacy of focused domain adaptation over parameter count alone. Pushing this further, AstroMLab 4, a 70-billion-parameter domain-specialized reasoning model, exhibited benchmark-topping performance in astronomy Q&A, establishing new state-of-the-art results for accuracy and complex reasoning within the field.

Beyond developing these powerful models, my work has also focused on establishing rigorous evaluation frameworks. Through the EAIRA (Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants) project, I have designed and implemented a comprehensive methodology for assessing AI models not merely on their language generation, but on their ability to function as true scientific research aids. This systematic approach, initially explored through challenging contexts like "Astronomy Jeopardy!", provides a robust framework for benchmarking and comparing AI performance in scientific reasoning. The collective impact of this research demonstrates that carefully specialized and evaluated foundation models can provide cost-effective, highly accurate, and reliable tools for scientists, paving the way for AI to become indispensable partners in accelerating scientific discovery and knowledge dissemination.

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
