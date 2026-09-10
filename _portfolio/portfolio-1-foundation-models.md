---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The rapidly evolving field of foundation models represents a paradigm shift in artificial intelligence, offering powerful, pre-trained models capable of performing a wide array of tasks across various domains. These models, often trained on vast quantities of data, develop emergent capabilities that can be fine-tuned or adapted for specific applications, significantly accelerating research and development. In scientific disciplines, particularly astrophysics and cosmology, the application of foundation models holds immense promise for tackling challenges associated with increasingly complex and voluminous datasets, from high-resolution simulations to observational data spanning multiple modalities. The development of specialized AI tools that can interpret, analyze, and even reason about scientific phenomena is crucial for advancing our understanding of the universe.

The integration of foundation models into scientific workflows necessitates addressing unique domain-specific challenges. This includes developing architectures capable of processing multi-modal scientific data—such as image, spectroscopic, and tabular information—and training large language models (LLMs) to comprehend the highly specialized vocabulary, intricate theories, and nuanced reasoning patterns inherent to fields like cosmology. Furthermore, the rigorous evaluation of these AI models is paramount, requiring new methodologies to ensure their reliability, accuracy, and utility as genuine scientific research assistants. Benchmarking not only their performance on specific tasks but also their capacity for scientific discovery and their adherence to physical principles is essential for their adoption in professional scientific environments.

My research portfolio centers on pioneering the development and application of foundation models specifically tailored for cosmology and astrophysics. I have developed multi-modal foundation models designed to process and interpret complex cosmological simulation data, enabling more efficient analysis and discovery from large ensembles. A significant thrust of my work involves transforming general-purpose LLMs into highly specialized scientific assistants. For instance, I have developed techniques for "Teaching LLMs to Speak Spectroscopy," allowing them to interpret and generate insights from intricate spectral data, a cornerstone of astronomical observation. This specialization is exemplified by projects like AstroMLab 3 and 4, where I designed and trained domain-specialized reasoning models, including a 70B-parameter model, achieving benchmark-topping performance in astronomy Q&A, often surpassing generalist models like GPT-4o with significantly smaller parameter counts.

Beyond model development, my work establishes critical methodologies for evaluating the scientific utility of these AI systems. I introduced EAIRA, a framework for evaluating AI models as scientific research assistants, and performed "Physical Benchmarking for AI-Generated Cosmic Web" to ensure that AI-evolved cosmological structures adhere to fundamental physical laws. My efforts with "InferA: A Smart Assistant for Cosmological Ensemble Data" underscore the practical application of these models in real-world research settings, streamlining data exploration and hypothesis generation. Collectively, these contributions demonstrate a comprehensive approach to integrating advanced AI into scientific discovery, from foundational model architecture and domain specialization to robust evaluation and practical application, ultimately accelerating the pace of astrophysical and cosmological research.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
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
