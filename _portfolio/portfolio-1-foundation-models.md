---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The rapid proliferation of data in astrophysics and cosmology presents both an unprecedented opportunity and a significant challenge. Modern astronomical surveys and high-resolution simulations generate petabytes of complex, multi-modal information spanning images, spectra, numerical data, and textual research. Extracting meaningful insights from this vast and intricate landscape often exceeds the capacity of traditional analytical methods and human expert review, creating a bottleneck for scientific discovery.

Foundation models, with their ability to learn broad representations and complex patterns from diverse data, are emerging as a transformative paradigm to address these challenges. These models offer the potential to integrate heterogeneous scientific information, automate tedious analysis tasks, and facilitate hypothesis generation. By moving beyond conventional statistical approaches, specialized foundation models can enable deeper understanding, predict phenomena, and accelerate the pace of scientific understanding across various sub-domains of astronomy and cosmology.

My research focuses on developing and deploying cutting-edge foundation models specifically tailored for astronomical and cosmological research, establishing them as intelligent scientific research assistants. I have engineered domain-specialized Large Language Models (LLMs) and multi-modal architectures that possess a deep understanding of complex scientific concepts and data. This work involves innovating techniques for adapting general-purpose AI to the unique complexities and often resource-limited nature of scientific datasets.

Through the "AstroMLab" series, I have pioneered methodologies for training and rigorously evaluating these specialized models, achieving benchmark-topping performance in critical astronomical tasks. For instance, AstroMLab 3 demonstrated GPT-4o level capabilities in astronomy Q&A and reasoning with a compact 8-billion-parameter model, while AstroMLab 4 further advanced these capabilities with a 70-billion-parameter domain-specialized reasoning model. A key technical contribution includes "Teaching LLMs to Speak Spectroscopy," enabling these models to interpret, analyze, and reason over complex spectroscopic data, a cornerstone of astronomical observation. Furthermore, I developed "InferA," a smart assistant specifically designed for navigating and extracting insights from vast cosmological ensemble datasets. To ensure the scientific utility and reliability of these AI tools, I established "EAIRA," a systematic methodology for evaluating AI models as scientific research assistants, providing a robust framework for assessing their impact. This portfolio also includes the development of multi-modal foundation models specifically engineered to interpret and analyze complex cosmological simulation data, integrating diverse data types for a holistic scientific understanding.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/infera-a-smart-assistant-for-cosmological-ensemble_plot_1_590fdcf1.png" alt="Figure from InferA: A Smart Assistant for Cosmological Ensemble Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: InferA: A Smart Assistant for Cosmological Ensemble Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
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
