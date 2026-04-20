---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The advent of foundation models, particularly large language models (LLMs) and multi-modal AI, has opened new frontiers for scientific discovery by offering unprecedented capabilities in data analysis, knowledge extraction, and intelligent querying. Within scientific domains, researchers face the challenge of processing vast and complex datasets, from high-resolution simulations to multi-wavelength observational data. Applying these advanced AI paradigms to scientific contexts requires specialized models capable of understanding domain-specific language, handling diverse data modalities, and performing intricate reasoning tasks that traditionally demand expert human insight.

The focus of this research area is to bridge the gap between general-purpose AI and the highly specialized needs of scientific research, particularly within astronomy and cosmology. This involves developing sophisticated AI systems that can serve as intelligent assistants, capable of interpreting scientific literature, analyzing complex data structures, and answering nuanced research questions. The objective is to accelerate the pace of scientific discovery by enabling more efficient data exploration, hypothesis generation, and knowledge synthesis, ultimately democratizing access to complex scientific information and tools for a broader community of researchers.

My work has systematically explored the application and advancement of foundation models for scientific research, predominantly in astronomy. I have developed the AstroMLab series of domain-specialized large language models, beginning with initial explorations into astronomy Q&A with AstroMLab 1. This progression led to AstroMLab 3, an 8B-parameter model achieving GPT-4o level performance in astronomy, and subsequently AstroMLab 4, a 70B-parameter domain-specialized reasoning model that has demonstrated benchmark-topping performance in complex astronomy Q&A tasks. A key aspect of this effort includes specific methodologies for teaching LLMs to understand and "speak" specialized scientific languages, such as spectroscopy, enabling them to interpret and generate insights from spectral data.

Furthermore, I have developed a multi-modal foundation model specifically designed for cosmological simulation data, integrating information across various modalities including images, tabular data, and associated textual descriptions to provide a comprehensive understanding of complex simulations. This model underpins InferA, a smart assistant tailored for navigating and querying cosmological ensemble data, significantly enhancing researchers' ability to explore vast datasets. Recognizing the critical need for rigorous assessment, I established EAIRA, a methodology for robustly evaluating AI models as scientific research assistants, ensuring their reliability and utility in real-world scientific applications. Through these contributions, my research aims to equip scientists with powerful, domain-aware AI tools that enhance data accessibility, accelerate discovery, and set new performance benchmarks for intelligent scientific assistants.

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
