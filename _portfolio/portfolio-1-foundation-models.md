---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The increasing complexity and sheer volume of data in scientific domains, particularly astronomy, present both unprecedented opportunities and significant challenges for discovery. Foundation models, representing a paradigm shift in artificial intelligence, offer powerful capabilities for processing, understanding, and generating information across diverse modalities. These models, pre-trained on vast datasets, can be adapted to perform a wide array of tasks, from natural language understanding to scientific data interpretation, promising to accelerate discovery by automating complex analytical tasks and revealing hidden patterns.

In astronomy, the need for advanced AI is particularly acute, given the petabytes of data from observatories, intricate cosmological simulations, and a rapidly expanding body of scientific literature. Traditional analytical methods often struggle to keep pace with this deluge, leading to bottlenecks in data interpretation and knowledge synthesis. This research portfolio addresses these challenges by developing and evaluating novel AI methodologies tailored for astronomical research, encompassing domain-specific large language models, multi-modal foundation models capable of integrating diverse data types, and sophisticated tools. The core focus is on pushing AI's ability to reason, generate insights, and interact with scientific data in ways that significantly augment human capabilities.

My work has concentrated on building specialized foundation models that transcend general-purpose AI limitations, achieving domain-specific reasoning crucial for scientific advancement. I have developed a series of "AstroMLab" models (AstroMLab 1, 3, 4), demonstrating benchmark-topping performance in astronomy Q&A and achieving GPT-4o level capabilities with an 8B-parameter model, further scaled to a 70B-parameter domain-specialized reasoning model. This involved teaching LLMs to "speak spectroscopy," enabling deep understanding and interpretation of complex spectral data, a cornerstone of astronomical analysis. Beyond language, I have contributed to developing a multi-modal foundation model specifically designed for cosmological simulation data, integrating diverse data types like images, numerical outputs, and associated text for a holistic understanding.

Furthermore, my research explores innovative applications such as "Predicting New Concept-Object Associations in Astronomy by Mining the Literature," leveraging AI to extract novel relationships and hypotheses directly from scientific publications. To aid researchers in navigating complex datasets, I have developed "InferA: A Smart Assistant for Cosmological Ensemble Data," an interactive tool for insights from large-scale simulations. Crucially, recognizing the need for rigorous assessment, I have also established a comprehensive methodology for evaluating AI models as scientific research assistants through "EAIRA," ensuring these advanced tools are not only powerful but also reliable and trustworthy collaborators in the scientific process. These contributions collectively aim to redefine the role of AI in scientific discovery, transforming how astronomers interact with data, literature, and complex simulations.

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
