---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a paradigm shift in artificial intelligence, offering highly adaptable general-purpose models capable of performing a wide range of tasks across various domains. Their immense potential to revolutionize scientific discovery is rapidly becoming apparent, as researchers explore their application in handling complex datasets, performing intricate analyses, and generating novel insights. However, the specialized nature of scientific inquiry, characterized by unique data modalities, highly technical language, and the critical need for robust reasoning and interpretability, presents significant challenges for general-purpose models.

The frontier of applying foundation models in science is focused on overcoming these hurdles through domain-specific adaptation and multi-modal integration. This involves developing models that can effectively process and synthesize diverse scientific data formats, such as cosmological simulations, astronomical images, spectroscopic readings, and textual research papers. The goal is to move beyond simple pattern recognition to enable sophisticated scientific reasoning, hypothesis generation, and intelligent assistance for researchers, thereby accelerating the pace of discovery in fields ranging from astrophysics and cosmology to fundamental physics.

My research specifically addresses these challenges by developing and deploying specialized foundation models tailored for scientific applications. I have spearheaded efforts to create multi-modal foundation models capable of interpreting complex cosmological simulation data, integrating diverse data types like images, numerical catalogs, and time-series information to facilitate deeper understanding. A key aspect of my work involves teaching Large Language Models (LLMs) to master scientific language and reasoning, as exemplified by developing models that "speak spectroscopy" and specialized LLMs for astronomy that achieve benchmark-topping performance in Q&A tasks.

Through projects like AstroMLab, I have demonstrated that highly specialized, smaller-parameter models (e.g., an 8B-parameter model) can achieve performance levels comparable to or even surpass much larger general-purpose models like GPT-4o in domain-specific tasks, thereby enhancing efficiency and accessibility. My contributions extend to building practical smart assistants such as InferA for cosmological ensemble data, and exploring agentic AI architectures like ArgoLOOM for fundamental physics investigations from quarks to cosmos. Crucially, I have also established methodologies, such as EAIRA, for rigorously evaluating AI models as scientific research assistants, ensuring their reliability and utility in the scientific workflow. This work collectively advances the state-of-the-art in AI for science, offering powerful tools to accelerate discovery and provide intelligent support to researchers.

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
