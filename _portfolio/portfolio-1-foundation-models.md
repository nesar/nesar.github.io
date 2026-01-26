---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The advent of foundation models, particularly large language models (LLMs) and multi-modal AI systems, marks a transformative period across various disciplines, including scientific research. These models, pre-trained on vast datasets, possess emergent capabilities for language understanding, generation, and complex reasoning. However, their direct application in highly specialized scientific domains, such as astrophysics and cosmology, often presents significant challenges due to a lack of domain-specific knowledge, the unique structure of scientific data (e.g., simulations, spectroscopic measurements), and the stringent requirements for accuracy and interpretability in scientific inquiry.

Addressing these challenges necessitates the development of specialized methodologies for adapting, fine-tuning, and evaluating foundation models to effectively serve as scientific research assistants. This research area focuses on bridging the gap between general-purpose AI and the nuanced demands of scientific discovery. Key objectives include creating models that can interpret complex scientific data, answer domain-specific questions with high fidelity, and facilitate the exploration of large scientific datasets, thereby accelerating hypothesis generation and knowledge extraction.

My work directly tackles these challenges by pioneering the adaptation and specialization of foundation models for scientific research, particularly within astrophysics and cosmology. I have developed innovative approaches to enhance AI’s capability to understand, interpret, and reason with diverse scientific data. This includes the creation of InferA, a smart assistant specifically designed for interpreting cosmological ensemble data, streamlining the analysis of complex simulation outputs. Furthermore, I have explored the development of multi-modal foundation models tailored for cosmological simulation data, integrating various data types—such as visual and numerical information—to provide a more comprehensive understanding than text-only approaches.

A significant part of my research has focused on teaching LLMs to speak the specialized languages of science. For instance, I have developed techniques for fine-tuning LLMs to effectively interpret spectroscopy, a critical diagnostic tool in astronomy, demonstrating their ability to process and reason about highly technical observational data. The AstroMLab series of papers (AstroMLab 1, 3, and 4) chronicles the development and rigorous benchmarking of domain-specialized reasoning models, ranging from 8B to 70B parameters, for astronomy Q&A. These models have achieved benchmark-topping performance, reaching and even surpassing the capabilities of general-purpose models like GPT-4o in domain-specific contexts, by leveraging specialized datasets and fine-tuning strategies. Concurrently, to ensure the reliability and utility of these AI tools, I established EAIRA (Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants), providing a robust framework for assessing AI models based on scientific accuracy, reasoning ability, and overall contribution to research. This comprehensive body of work underscores a commitment to advancing the frontier of AI for scientific discovery, developing reliable and powerful intelligent assistants for researchers.

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
