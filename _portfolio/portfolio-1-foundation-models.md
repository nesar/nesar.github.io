---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The burgeoning field of artificial intelligence is profoundly impacting scientific discovery, particularly within data-rich domains like astronomy and cosmology. Foundation models, characterized by their immense scale and pre-training on vast datasets, offer unprecedented opportunities to accelerate research. These models, encompassing large language models (LLMs) and multi-modal variants, are being adapted to tackle complex challenges such as interpreting vast cosmological simulation data, understanding intricate spectroscopic readings, and providing intelligent assistance to researchers.

A key challenge lies in specializing these general-purpose foundation models to accurately comprehend and reason within highly technical scientific contexts. This involves overcoming issues like domain-specific jargon, the diverse formats of scientific data (images, time series, text), and the need for robust, explainable reasoning capabilities. The overarching objective is to develop AI systems that can not only process and analyze data efficiently but also serve as intelligent scientific research assistants, capable of answering complex queries, extracting profound insights, and even proposing new avenues for investigation.

My work has extensively explored the development and application of domain-specialized foundation models to address these challenges in astronomy and cosmology. I have developed multi-modal foundation models specifically tailored for cosmological simulation data, enabling the nuanced interpretation of complex ensemble datasets, as exemplified by the InferA smart assistant. A significant focus has been on "teaching LLMs to speak spectroscopy," where I have engineered models capable of understanding and generating insights from spectroscopic data, a cornerstone of astrophysical analysis. This involves advanced fine-tuning techniques and novel architectures designed to capture the intricate patterns within scientific measurements.

Furthermore, I have developed a series of specialized Large Language Models, notably within the AstroMLab suite, demonstrating benchmark-topping performance in astronomy Q&A. For instance, AstroMLab 3 and AstroMLab 4, leveraging 8-billion and 70-billion parameter domain-specialized reasoning models respectively, have achieved and surpassed GPT-4o level performance in highly specialized astronomical knowledge domains. This work, initiated with foundational benchmarks like "Who Wins Astronomy Jeopardy!?", underscores the effectiveness of domain adaptation for superior performance. Critically, I have also established a rigorous methodology for evaluating AI models as scientific research assistants (EAIRA), ensuring that these intelligent systems not only perform well but also contribute meaningfully and reliably to the scientific research workflow, setting new standards for AI utility in scientific discovery.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
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
