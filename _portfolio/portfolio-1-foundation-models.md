---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation Models represent a transformative paradigm in artificial intelligence, leveraging vast datasets and intricate architectures to learn generalized representations applicable across a multitude of downstream tasks. In scientific research, this approach holds immense promise for tackling the burgeoning volume and complexity of data, accelerating discovery, and augmenting human intellect. These models excel at identifying patterns, extracting knowledge, and performing sophisticated reasoning over diverse data types, including text, imagery, and numerical simulations, thereby offering powerful tools for hypothesis generation and data-driven insights.

Within fields like astronomy and cosmology, the application of Foundation Models is particularly impactful due to the sheer scale, multi-modal nature, and intricate interconnections of available data—from petabytes of observational imagery and spectroscopic measurements to high-resolution cosmological simulations and an ever-expanding body of scientific literature. By developing AI systems capable of seamlessly integrating and interpreting these disparate data sources, researchers can overcome traditional barriers to discovery, automate laborious analysis tasks, and uncover novel relationships that might elude conventional methods.

My research has been dedicated to pioneering the development and application of domain-specialized Foundation Models for astronomy and cosmology. I have focused on building highly performant Large Language Models (LLMs) that can understand and reason about complex astronomical phenomena, as demonstrated by the AstroMLab series. This work has involved training models, including an 8B-parameter specialized LLM achieving GPT-4o level performance and a 70B-parameter reasoning model, to excel in astronomy Q&A benchmarks. A key technical contribution lies in "Teaching LLMs to Speak Spectroscopy," enabling these models to interpret and reason directly from specialized data formats critical to astronomical analysis, moving beyond mere text processing. Furthermore, I have explored knowledge graph mining techniques for "Predicting New Concept-Object Associations in Astronomy by Mining the Literature," showcasing how LLMs can uncover novel scientific connections from vast textual corpora.

Beyond text-based reasoning, I have developed multi-modal Foundation Models specifically designed to integrate and interpret diverse cosmological simulation data, including images, spectra, and numerical outputs. This capability is crucial for tools like "InferA: A Smart Assistant for Cosmological Ensemble Data," which aims to provide intuitive, AI-driven support for navigating and analyzing complex simulation datasets. Recognizing the critical need for robust validation, I have also established "EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants," providing a rigorous framework to assess the reliability and utility of these advanced AI systems in accelerating scientific workflows and supporting researchers in their quest for new discoveries.

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
