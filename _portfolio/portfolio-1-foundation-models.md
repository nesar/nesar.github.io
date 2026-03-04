---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The rapid expansion of scientific data across disciplines, particularly in astronomy, presents both unprecedented opportunities and significant challenges for discovery. Foundation models, pre-trained on vast datasets and capable of emergent abilities, offer a transformative paradigm for navigating this complexity. These powerful AI systems can process, interpret, and generate human-like text, understand various data modalities, and perform complex reasoning tasks. However, general-purpose foundation models often fall short in highly specialized scientific domains due to a lack of domain-specific knowledge, reasoning capabilities, and the ability to seamlessly integrate diverse scientific data types, such as numerical simulations, spectroscopic observations, and dense research literature.

Addressing these limitations requires the development of tailored methodologies and domain-specialized foundation models capable of operating as intelligent scientific research assistants. Such models must excel at tasks ranging from extracting novel concept-object associations from burgeoning scientific literature to interpreting multi-modal cosmological simulation data. They need to understand complex observational data, like spectroscopy, and provide accurate, contextualized answers to intricate scientific queries. The goal is to bridge the gap between abstract theoretical frameworks and the practical needs of researchers, enabling more efficient knowledge discovery and data interpretation in fields grappling with information overload.

My research directly confronts these challenges by developing advanced, domain-specialized foundation models and methodologies specifically engineered for astronomy and scientific research. My work focuses on adapting and enhancing the capabilities of large language models (LLMs) to serve as robust, high-performing scientific research assistants, moving beyond the limitations of general-purpose AI. I have developed a portfolio of systems and benchmarks, collectively demonstrating the immense potential of integrating AI into scientific workflows, from automating literature review to providing expert-level Q&A capabilities for complex scientific inquiries.

I have specifically developed the AstroMLab series, including AstroMLab 3 and AstroMLab 4, which leverage specialized training to achieve benchmark-topping performance in astronomy question-answering, even reaching GPT-4o level capabilities with an 8B-parameter model. My contributions extend to teaching LLMs to "speak" spectroscopy, enabling them to interpret complex spectral data, and creating multi-modal foundation models specifically for cosmological simulation data. Furthermore, I developed InferA, a smart assistant designed for cosmological ensemble data, and a robust methodology, EAIRA, for evaluating AI models as scientific research assistants, ensuring their scientific rigor and utility. My work also includes pioneering methods for predicting new concept-object associations in astronomy by mining the scientific literature, thereby accelerating the pace of scientific discovery and making complex scientific knowledge more accessible and actionable for researchers.

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
