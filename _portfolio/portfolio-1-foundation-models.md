---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a paradigm shift in artificial intelligence, leveraging vast datasets and intricate architectures to develop highly capable, general-purpose models. These models demonstrate unprecedented abilities in tasks such as natural language processing, image generation, and complex reasoning across diverse domains. Their emergent capabilities promise to revolutionize numerous fields by automating complex tasks, enabling advanced data analysis, and supporting discovery processes, marking a critical advancement in AI's journey towards more versatile and intelligent systems.

Within scientific disciplines, particularly astronomy and cosmology, the application of foundation models presents unique opportunities and challenges. These fields grapple with immense, multi-modal datasets derived from simulations and observations, encompassing everything from high-resolution images and complex spectral data to vast catalogs of celestial objects. Interpreting these diverse data types, understanding their interdependencies, and extracting meaningful scientific insights often requires highly specialized expertise and computationally intensive methods, posing a significant bottleneck for researchers.

The development of specialized foundation models tailored for scientific contexts offers a powerful avenue to accelerate discovery and enhance data interpretation. By adapting these advanced AI architectures to the specific nuances of scientific data and reasoning patterns, it becomes possible to create intelligent systems capable of assisting researchers with complex analytical tasks, generating hypotheses, and even simulating scientific workflows. This domain-specific adaptation is crucial for unlocking the full potential of foundation models in addressing the intricate problems inherent in scientific research.

My research directly addresses these challenges by developing and deploying novel foundation models and large language models (LLMs) specifically engineered for astronomy and cosmology. I have spearheaded the creation of the AstroMLab series, including domain-specialized reasoning models like AstroMLab 3 and AstroMLab 4, which have achieved benchmark-topping performance and even GPT-4o level capabilities in astronomy Q&A. A key focus has been on enabling LLMs to interpret specialized scientific data, demonstrated through work on teaching LLMs to understand spectroscopy and the development of multi-modal foundation models for cosmological simulation data. This involves sophisticated training methodologies, instruction tuning, and the integration of diverse data modalities to build truly intelligent scientific assistants.

The impact of this work extends to transforming how scientists interact with complex data and research questions. I have developed smart assistants such as InferA, designed to aid in the analysis of cosmological ensemble data, and explored the creation of intelligent agents that can act as scientific research assistants. Crucially, I have also established a rigorous methodology for evaluating AI models in scientific research contexts, encapsulated in the EAIRA framework, ensuring that these advanced tools are both effective and reliable. By consistently pushing the boundaries of what specialized AI can achieve in science, from outperforming human experts in astronomy jeopardy to achieving state-of-the-art performance in complex reasoning tasks, my contributions pave the way for a new era of AI-augmented scientific discovery.

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
