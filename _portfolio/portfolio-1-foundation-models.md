---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models, particularly Large Language Models (LLMs), represent a transformative advancement in artificial intelligence, exhibiting unprecedented capabilities in understanding, generating, and reasoning across diverse modalities. These models, pre-trained on vast and varied datasets, serve as foundational components that can be adapted to a wide array of downstream tasks through fine-tuning or prompt engineering. While initially demonstrating remarkable proficiency in general language and image tasks, their potential to accelerate discovery and innovation in specialized scientific domains is increasingly recognized, necessitating tailored development to address the unique complexities of scientific data and knowledge.

Scientific research, particularly in fields like astrophysics, is characterized by immense volumes of complex, multi-modal data, ranging from high-dimensional observational measurements to large-scale cosmological simulations. Interpreting these intricate datasets, formulating hypotheses, and deriving novel insights often requires deep domain expertise and significant computational resources. The development of specialized foundation models that can accurately process, analyze, and reason about scientific information presents a critical avenue for automating discovery, assisting researchers, and making complex scientific knowledge more accessible. This specialization involves adapting model architectures and training methodologies to specific data types, domain ontologies, and the nuanced reasoning patterns inherent to scientific inquiry.

My research focuses on developing and deploying specialized foundation models to tackle the unique challenges and opportunities within astrophysics and cosmology. I have pioneered the creation of multi-modal foundation models specifically designed to interpret complex cosmological simulation data, integrating diverse data types to provide a holistic understanding of cosmic evolution. Furthermore, I have addressed the critical need for LLMs to comprehend and articulate scientific measurements, successfully teaching LLMs to "speak spectroscopy" – enabling them to interpret and reason about spectral data, which is fundamental to understanding the composition and dynamics of celestial objects.

This work culminates in the AstroMLab series, where I have systematically developed and benchmarked domain-specialized Large Language Models for astronomy. AstroMLab 1 established the foundational benchmarks for astronomical knowledge retrieval, while AstroMLab 3 demonstrated the capability to achieve GPT-4o level performance in astronomy with a highly optimized 8-billion parameter model. Expanding on this, AstroMLab 4 showcased benchmark-topping performance in astronomy Q&A by developing a 70-billion parameter domain-specialized reasoning model, pushing the boundaries of what specialized LLMs can achieve in complex scientific question-answering tasks. These developments represent a significant step towards creating expert-level AI assistants capable of accelerating scientific discovery and knowledge dissemination in astrophysics.

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
