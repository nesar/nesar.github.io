---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The field of artificial intelligence, particularly foundation models, is rapidly transforming scientific research by offering unprecedented capabilities for data interpretation, hypothesis generation, and discovery. Scientific disciplines, especially astronomy and cosmology, generate vast, complex, and heterogeneous datasets spanning numerical simulations, observational measurements, textual literature, and specialized sensory data like spectroscopy.

Extracting meaningful insights from this data deluge presents significant challenges, necessitating specialized models capable of understanding domain-specific language, complex data structures, and reasoning effectively within scientific paradigms. Generic foundation models often fall short, highlighting the critical need for domain-specific adaptation and multi-modal integration to truly augment human researchers' capabilities and foster new discoveries.

My work significantly advances this field by developing and evaluating domain-specialized foundation models tailored for scientific discovery, with a particular emphasis on astronomy and cosmology. I have pioneered multi-modal foundation models capable of integrating and reasoning across diverse data types, exemplified by my "Multi-modal Foundation Model for Cosmological Simulation Data." My research focuses on enhancing the reasoning capabilities of large language models (LLMs) for scientific applications, achieving "benchmark-topping performance" and "GPT-4o level performance" in astronomy Q&A with domain-specialized 8B and 70B-parameter models, as detailed in the AstroMLab series. This also includes enabling LLMs to interpret highly specialized data, such as "Teaching LLMs to Speak Spectroscopy," allowing them to derive insights from complex spectral signatures.

Beyond traditional Q&A, my contributions extend to novel applications like "Predicting New Concept-Object Associations in Astronomy by Mining the Literature," demonstrating AI's potential to uncover previously unknown scientific relationships. To facilitate efficient data access and analysis in complex scientific environments, I have developed techniques for "Searching the Pareto Front: Multi-Objective Retrieval for Heterogeneous Scientific Modalities." Furthermore, my work includes the development of practical AI research assistants, such as "InferA: A Smart Assistant for Cosmological Ensemble Data," and the establishment of robust methodologies (EAIRA) for "Evaluating AI Models as Scientific Research Assistants." This comprehensive body of work underscores the transformative potential of specialized foundation models in accelerating the pace of scientific discovery and providing powerful, reliable tools for researchers.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/searching-the-pareto-front-multi-objective-retriev_plot_1_b46d2d57.png" alt="Figure from Searching the Pareto Front: Multi-Objective Retrieval for Heterogeneous Scientific Modalities" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Searching the Pareto Front: Multi-Objective Retrieval for Heterogeneous Scientific Modalities</div>
  </div>
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
