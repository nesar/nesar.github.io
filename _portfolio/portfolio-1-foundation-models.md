---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models, including large language models (LLMs) and multi-modal architectures, are rapidly emerging as transformative tools across diverse scientific disciplines. These models, pretrained on vast and varied datasets, possess an unprecedented ability to understand, generate, and reason with complex information, making them invaluable for tasks ranging from automated data analysis and hypothesis generation to knowledge synthesis and scientific communication. Their capacity to learn intricate patterns and relationships from raw data enables new paradigms for accelerating discovery and tackling challenges previously intractable with traditional computational methods.

In fields such as astronomy and cosmology, researchers are confronted with an ever-increasing volume and complexity of data originating from cutting-edge telescopes, high-fidelity simulations, and multi-wavelength observations. Extracting meaningful insights from these petabyte-scale datasets often requires sophisticated analytical techniques and significant human effort. The application of specialized foundation models offers a powerful solution by providing AI assistants capable of navigating these data landscapes, identifying subtle correlations, interpreting diverse data types, and augmenting human scientific inquiry, thereby accelerating the pace of discovery and enabling scientists to focus on higher-level reasoning.

My research extensively explores the development and application of advanced foundation models tailored for astronomical and cosmological research. I have focused on building domain-specialized reasoning models, demonstrated by the AstroMLab series, which achieved benchmark-topping performance in astronomy Q&A tasks. This includes developing an 8B-parameter specialized LLM capable of matching GPT-4o level performance in astronomy (AstroMLab 3), and scaling up to a 70B-parameter domain-specialized reasoning model (AstroMLab 4) for enhanced problem-solving capabilities. A core technical contribution involves adapting these LLMs to interpret highly specific scientific data, such as "teaching LLMs to speak spectroscopy," enabling them to process and derive insights from critical astrophysical measurement types.

Beyond text-based reasoning, I have engineered multi-modal foundation models specifically designed for cosmological simulation data, allowing for a more holistic understanding by integrating visual, numerical, and textual information. To further support scientific workflows, I developed InferA, a smart assistant tailored for efficient exploration and analysis of complex cosmological ensemble data. Recognizing the imperative for rigorous assessment in scientific AI, I also established EAIRA, a comprehensive methodology for evaluating AI models as reliable scientific research assistants. This body of work underscores a commitment to advancing the frontier of AI in science, developing robust, high-performing foundation models that enhance scientific discovery and research productivity.

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
