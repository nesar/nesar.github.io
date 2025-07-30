---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The advent of large language models (LLMs) has marked a transformative period in artificial intelligence, showcasing remarkable capabilities in understanding, generating, and reasoning with human language. These "foundation models" have demonstrated impressive general intelligence across a wide array of tasks, from creative writing to complex problem-solving. However, their direct application to highly specialized scientific domains, which often involve nuanced terminology, intricate data analysis, and sophisticated reasoning, presents unique challenges. General-purpose models may lack the depth of knowledge or the specific reasoning patterns required for expert-level performance in fields like astronomy.

Addressing this gap requires dedicated research into adapting and specializing these powerful models for scientific inquiry. This involves not only fine-tuning models on domain-specific corpora but also developing robust methodologies to rigorously evaluate their performance as true scientific research assistants. The goal is to unlock the potential of foundation models to accelerate scientific discovery, automate tedious tasks, and democratize access to complex knowledge, thereby augmenting human intelligence in the research ecosystem.

My research has centered on exploring and advancing the application of foundation models, particularly large language models, within the specialized domain of astronomy. Early work, such as "AstroMLab 1: Who Wins Astronomy Jeopardy!?," laid the groundwork by benchmarking initial model capabilities on domain-specific Q&A tasks, highlighting both the potential and the limitations of general AI in expert fields. Building on this, I have developed a series of progressively more capable and specialized models. "AstroMLab 3" showcased the effectiveness of domain specialization by achieving GPT-4o level performance in astronomy with a significantly smaller, 8B-parameter large language model, demonstrating that tailored approaches can yield highly efficient and accurate results without requiring massive model sizes.

Further pushing the boundaries, "AstroMLab 4" scaled up this domain-specialized approach, developing a 70B-parameter model that achieved benchmark-topping performance in astronomy Q&A, demonstrating advanced domain-specialized reasoning capabilities essential for scientific assistance. Beyond model development, my work also includes critical contributions to the meta-level challenge of evaluation. In "EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants," I have formulated a comprehensive framework for assessing AI's utility and reliability in a research context, moving beyond simple accuracy metrics to evaluate factors like interpretability, consistency, and the ability to act as a genuine assistant. This holistic approach ensures that developed models are not only performant but also trustworthy and genuinely useful tools for scientific exploration.

<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>

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
