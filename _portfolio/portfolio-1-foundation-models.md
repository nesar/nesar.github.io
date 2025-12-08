---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a transformative paradigm in artificial intelligence, characterized by their immense scale, pre-training on vast and diverse datasets, and remarkable adaptability to a wide array of downstream tasks. These models, including large language models, vision transformers, and multi-modal architectures, have demonstrated unprecedented capabilities in understanding, generating, and reasoning across various data modalities. Their emergence has profoundly impacted fields ranging from natural language processing and computer vision to healthcare and creative arts, promising to fundamentally reshape human-computer interaction and problem-solving.

The application of foundation models holds immense potential for accelerating scientific discovery, but it also presents unique challenges. Scientific domains often involve highly specialized terminology, complex data structures such as simulation outputs, spectroscopic data, and astronomical images, and the critical need for rigorous, verifiable reasoning. Developing foundation models capable of effectively assisting researchers requires not only adapting general AI principles but also crafting domain-specific architectures, training regimes, and comprehensive evaluation methodologies that respect the precision and depth inherent in scientific inquiry. This includes enabling models to interpret diverse data types and act as intelligent research assistants capable of complex reasoning.

My research portfolio focuses on harnessing the power of foundation models to revolutionize scientific research, particularly within astronomy and cosmology, and more broadly, as intelligent scientific research assistants. I have developed and investigated novel approaches to enable these powerful AI systems to understand, interpret, and generate insights from complex scientific data. This work has included creating domain-specialized foundation models that demonstrate benchmark-topping performance in astronomy Q&A, as highlighted in AstroMLab 4, and achieving GPT-4o level capabilities with significantly smaller, more efficient 8B-parameter models specifically trained for astronomy in AstroMLab 3. My aim is to bridge the gap between general-purpose AI and the intricate demands of specialized scientific disciplines, enhancing both performance and accessibility.

To achieve these advancements, I have contributed specific technical innovations and methodologies. This includes developing a multi-modal foundation model specifically tailored for cosmological simulation data, enabling a holistic understanding of complex astrophysical phenomena by integrating various data types. I have also focused on specialized training techniques, such as "Teaching LLMs to Speak Spectroscopy," which fine-tunes models to interpret and reason about highly technical spectroscopic data. Furthermore, my work introduces InferA, a smart assistant for cosmological ensemble data, and explores agentic AI architectures like ArgoLOOM for fundamental physics research, spanning from quarks to cosmos. Recognizing the critical need for rigorous assessment, I established EAIRA, a methodology for systematically evaluating AI models as scientific research assistants. These efforts are designed to create intelligent tools that enhance data interpretation, accelerate knowledge synthesis, and ultimately drive new discoveries in fundamental physics and astronomy.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 1: Who Wins Astronomy Jeopardy!?" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 1: Who Wins Astronomy Jeopardy!?</div>
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
