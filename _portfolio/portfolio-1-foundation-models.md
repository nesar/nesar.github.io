---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The burgeoning field of astrophysics and cosmology generates an unprecedented volume and complexity of data, ranging from multi-wavelength observational datasets to vast cosmological simulations. Extracting meaningful scientific insights from this data deluge presents significant computational and analytical challenges. Traditional data analysis methods often struggle with the scale, dimensionality, and multi-modal nature of these datasets, necessitating advanced artificial intelligence (AI) solutions capable of sophisticated data interpretation, pattern recognition, and complex scientific reasoning.

The development of foundation models, particularly large language models (LLMs) and multi-modal AI systems, offers a transformative approach to accelerate scientific discovery in these domains. However, generic foundation models, trained on broad internet data, often lack the specialized knowledge, nuanced reasoning capabilities, and domain-specific modalities required for expert-level performance in highly technical scientific fields. There is a critical need for domain-specialized AI architectures that can not only process and understand scientific literature but also interpret complex numerical data, spectral information, and simulation outputs, effectively bridging the gap between raw data and scientific hypotheses.

My work focuses on pioneering the development, application, and rigorous evaluation of domain-specialized foundation models tailored for astrophysics and cosmology. I have developed a suite of models designed to tackle the unique challenges of scientific data analysis and accelerate research workflows, emphasizing both technical performance and robust scientific utility. My approach involves creating sophisticated AI systems capable of advanced reasoning, multi-modal data integration, and expert-level scientific question answering.

Through the AstroMLab series, I have engineered specialized large language models that achieve state-of-the-art performance in astronomy. AstroMLab 3, an 8-billion-parameter model, demonstrated GPT-4o-level capabilities in complex astronomy Q&A and reasoning tasks, significantly outperforming generic models. Expanding on this, AstroMLab 4, a 70-billion-parameter domain-specialized reasoning model, achieved benchmark-topping performance, showcasing the power of fine-tuning large models on extensive astronomical knowledge. My research also extends to multi-modal challenges, exemplified by the "Multi-modal Foundation Model for Cosmological Simulation Data," which integrates diverse data types, and "Teaching LLMs to Speak Spectroscopy," which addresses the critical need for AI to interpret complex spectral information. Furthermore, I developed InferA, a smart assistant specifically designed for cosmological ensemble data, providing practical solutions for navigating vast simulation outputs. Complementing these developments, the EAIRA methodology establishes a robust framework for evaluating AI models as credible scientific research assistants, ensuring their reliability and utility in the scientific discovery process.

These contributions demonstrate the feasibility and immense potential of domain-specialized foundation models to revolutionize scientific research. By developing models that excel at complex reasoning, multi-modal data interpretation, and provide practical assistance in data analysis, my work sets new benchmarks for AI performance in astrophysics and establishes a clear path towards integrating intelligent assistants into the core of scientific exploration.

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
