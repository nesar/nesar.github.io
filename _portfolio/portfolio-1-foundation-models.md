---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The rapid advancements in artificial intelligence, particularly in large language models (LLMs) and multi-modal foundation models, are profoundly transforming scientific research. These powerful AI systems demonstrate immense potential for accelerating discovery by processing vast, complex datasets, identifying patterns, and assisting with intricate reasoning tasks, thereby pushing the boundaries of human understanding across various scientific domains.

In fields like astronomy and cosmology, researchers contend with immense data volumes from simulations and observations, alongside highly specialized terminology and data formats. Adapting general-purpose foundation models to these contexts presents significant challenges, requiring their specialization to proficiently handle unique scientific data modalities. This involves tailoring models for cosmological simulation outputs, astronomical images, and spectroscopic measurements, ensuring they can understand technical information, engage in scientific inquiry, and provide reliable support for complex research questions.

My research directly addresses these challenges by developing and deploying highly specialized foundation models for astronomy and cosmology. I spearheaded the creation of "InferA," a smart assistant designed to navigate and interpret vast cosmological ensemble data for efficient exploration. I also developed a multi-modal foundation model specifically for cosmological simulation data, integrating and analyzing diverse data types from images to numerical results. My work further includes "Teaching LLMs to Speak Spectroscopy," empowering these models to understand, analyze, and generate insights from this cornerstone of astronomical research. Through the "AstroMLab" series, I systematically advanced domain-specialized reasoning models for astronomy, progressing from initial explorations to "AstroMLab 3," achieving GPT-4o level performance in astronomy Q&A with an efficient 8B-parameter LLM. Building upon this, "AstroMLab 4" further developed a 70B-parameter domain-specialized reasoning model that achieved benchmark-topping performance in astronomy Q&A, setting new standards for AI proficiency in scientific domains.

Beyond developing these powerful AI tools, I established a robust methodology for evaluating AI models as scientific research assistants with "EAIRA." This framework is vital for assessing the reliability, accuracy, and utility of advanced AI systems in genuine scientific contexts. My overall contributions not only enhance research efficiency and democratize access to complex data analysis, but also set new benchmarks for AI integration in scientific discovery, paving the way for AI-augmented scientific exploration.

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
