---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The rapid advancements in artificial intelligence, particularly in the realm of Foundation Models (FMs) and Large Language Models (LLMs), are poised to revolutionize scientific research across various disciplines. These powerful models, pre-trained on vast datasets, demonstrate remarkable capabilities in understanding, generating, and reasoning with human language. However, their direct application in specialized scientific domains often requires significant adaptation, given the unique ontologies, complex data modalities (text, images, simulations), and highly specific reasoning tasks inherent to fields like astrophysics, cosmology, and spectroscopy. The challenge lies in developing FMs that can not only comprehend scientific literature but also interpret complex numerical simulations, observational data, and specialized technical languages, thereby acting as truly intelligent research assistants.

Addressing this gap necessitates the creation of domain-specialized Foundation Models capable of robust performance across multi-modal scientific data and intricate reasoning tasks. Current research efforts are focused on bridging the divide between general-purpose AI and the demands of scientific inquiry by developing architectures and training methodologies that imbue FMs with deep domain knowledge and the ability to process diverse data types. This involves fine-tuning, specialized pre-training, and the integration of novel techniques to enhance their capacity for scientific question-answering, data exploration, and the nuanced interpretation required for scientific discovery, ultimately aiming to accelerate research workflows and uncover new insights from vast and complex datasets.

My research extensively explores the development and application of domain-specialized Foundation Models and Large Language Models to accelerate scientific discovery, primarily within astrophysics and cosmology. I have spearheaded the AstroMLab series, including AstroMLab 1, 3, and 4, which demonstrates the progressive enhancement of LLMs for astronomy question-answering. This work culminated in the development of a 70B-parameter domain-specialized reasoning model that achieves benchmark-topping performance, even surpassing generalist models like GPT-4o in specific astronomy tasks. A key technical contribution involved training these models to "speak spectroscopy," enabling them to interpret and reason about highly specialized scientific data formats, thus bridging the gap between natural language understanding and complex data analysis.

Furthermore, I have developed multi-modal Foundation Models specifically tailored for analyzing complex cosmological simulation data, as detailed in my work on "InferA: A Smart Assistant for Cosmological Ensemble Data" and the "Multi-modal Foundation Model for Cosmological Simulation Data." These models integrate textual, numerical, and visual information to provide intelligent assistance for data exploration and analysis. A critical aspect of this research involves establishing rigorous evaluation methodologies. Through EAIRA: "Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants," I have created robust frameworks for assessing the scientific utility and reliability of these AI agents. My work provides powerful tools that act as scientific research assistants, enabling more efficient data interpretation, complex query resolution, and ultimately fostering new discoveries by making vast, intricate scientific information more accessible and actionable.

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
