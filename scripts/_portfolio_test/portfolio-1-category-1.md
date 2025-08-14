---
title: "Domain-Specific LLMs for Astronomy"
excerpt: "Research in domain-specific llms for astronomy"
collection: portfolio
---

The rapidly evolving field of Large Language Models (LLMs) has demonstrated immense potential across various domains, yet their application in highly specialized scientific disciplines like astronomy presents unique challenges. General-purpose LLMs, while possessing broad knowledge, often struggle with the nuanced terminology, complex reasoning, and factual precision required for deep scientific inquiry. This can lead to superficial answers, subtle inaccuracies, or even "hallucinations" when confronted with intricate astronomical questions or advanced research topics.

To address these limitations, research has increasingly focused on the development of domain-specific LLMs. These specialized models are meticulously trained or fine-tuned on vast corpuses of domain-specific data, enabling them to internalize the unique lexical, conceptual, and inferential structures of a particular field. The goal is to create AI systems that can provide highly accurate, contextually relevant, and scientifically rigorous responses, thereby serving as invaluable tools for researchers, educators, and enthusiasts within that domain. The AstroMLab series of research specifically investigates this approach within the context of astronomy, demonstrating the profound benefits of tailored AI solutions.

My work within the AstroMLab series directly tackles the challenge of building highly performant and reliable LLMs for the field of astronomy. Recognizing the limitations of general models in specialized scientific contexts, I have developed and rigorously evaluated several domain-specific large language models designed to excel in astronomical knowledge and reasoning. Early investigations, such as those explored in "AstroMLab 1: Who Wins Astronomy Jeopardy!?", highlighted the significant gap between general AI capabilities and the deep, precise understanding required for complex astronomical Q&A. This foundational work underscored the critical need for dedicated domain specialization.

Building on these insights, I developed and refined advanced methodologies for creating highly effective astronomical LLMs. In "AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model," I demonstrated that even an 8-billion-parameter model, through meticulous domain-specific fine-tuning and optimization, could achieve performance levels comparable to much larger, state-of-the-art general models like GPT-4o on astronomy-specific tasks. Further pushing the boundaries, "AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" showcases the development of a 70-billion-parameter model that not only surpasses existing benchmarks but also exhibits exceptional reasoning capabilities crucial for complex scientific inquiry. My contributions emphasize the power of specialized architecture and training data in overcoming the inherent limitations of general LLMs, offering highly accurate and reliable AI tools for the astronomy community.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
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
