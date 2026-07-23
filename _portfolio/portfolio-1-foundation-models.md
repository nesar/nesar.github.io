---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a paradigm shift in artificial intelligence, characterized by their immense scale, pre-training on vast and diverse datasets, and remarkable adaptability to a wide array of downstream tasks. These models, encompassing large language models (LLMs) and multi-modal variants, have demonstrated unprecedented capabilities in understanding, generating, and reasoning across various forms of information, from natural language to images and beyond. Their emergence has spurred significant interest in leveraging their power to accelerate discovery and innovation across scientific disciplines.

Within scientific research, foundation models offer transformative potential, particularly in data-rich fields like astronomy and cosmology. The ability to process vast observational and simulated datasets, interpret complex scientific literature, and assist with hypothesis generation presents a new frontier for AI-driven discovery. However, directly applying general-purpose foundation models to specialized scientific domains poses unique challenges. These include the necessity for models to accurately interpret domain-specific terminology, handle novel data modalities such as spectroscopic charts or complex simulation outputs, and perform sophisticated scientific reasoning beyond general world knowledge.

My research addresses these critical challenges by developing and deploying specialized foundation models tailored for scientific inquiry, primarily within astronomy and cosmology. I have spearheaded the AstroMLab series, focusing on creating highly performant domain-specialized large language models for astronomy question-answering. This began with explorations into baseline capabilities ("AstroMLab 1") and progressed significantly with "AstroMLab 3," where I demonstrated how an 8-billion-parameter model, through targeted specialization, could achieve performance levels comparable to general-purpose models like GPT-4o in astronomical contexts. This work highlights the efficiency and accessibility benefits of smaller, domain-optimized models for scientific tasks.

Building upon this, "AstroMLab 4" further advanced the state-of-the-art, introducing a 70-billion-parameter domain-specialized reasoning model that established benchmark-topping performance in astronomy Q&A, showcasing the scalability of this approach for deep scientific understanding. Beyond textual reasoning, my work extends foundation model capabilities to novel scientific data types. In "Teaching LLMs to Speak Spectroscopy," I developed methodologies to enable language models to interpret and communicate about spectroscopic data, moving beyond text to directly engage with critical observational measurements. Furthermore, I have contributed to the creation of a "Multi-modal Foundation Model for Cosmological Simulation Data," designed to process and analyze the intricate, multi-faceted outputs of large-scale cosmological simulations, from visual representations to underlying numerical data. This holistic approach empowers researchers with powerful tools for accelerated scientific discovery and advanced data interpretation.

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
