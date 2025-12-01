---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models, characterized by their massive scale, extensive pre-training on broad data, and adaptability to diverse downstream tasks, are revolutionizing artificial intelligence. While profoundly powerful, their application in specialized scientific domains presents unique challenges. These include the necessity for precise quantitative reasoning, robust interpretability, and the ability to process diverse, highly technical data modalities. Adapting these general-purpose models to scientific research requires addressing issues of domain-specific language, multi-modal data integration, and complex causal inference, moving beyond general knowledge to expert-level scientific understanding.

In fields such as astronomy and cosmology, researchers confront immense datasets ranging from observational measurements to high-fidelity simulations, often presenting as images, spectra, and numerical tables. Extracting novel insights, predicting phenomena, and accelerating discovery necessitates AI models that can not only process vast quantities of information but also understand underlying physical principles. This demand drives research into developing domain-specialized foundation models capable of advanced scientific reasoning, data interpretation, and even acting as intelligent research assistants. Crucially, establishing rigorous methodologies for evaluating the scientific utility and trustworthiness of these AI systems is paramount for their responsible integration into the scientific workflow.

My research specifically addresses these challenges by developing and deploying sophisticated foundation models tailored for scientific discovery, particularly within astronomy and fundamental physics. I have engineered multi-modal foundation models capable of interpreting complex cosmological simulation data, bridging diverse data types to uncover hidden relationships. A significant focus has been on empowering large language models (LLMs) to master specialized scientific languages, exemplified by my work in "Teaching LLMs to Speak Spectroscopy," which enables quantitative analysis of astronomical data. I have also developed InferA, a smart assistant designed to navigate and extract insights from complex cosmological ensemble data, automating traditionally labor-intensive tasks.

Furthermore, my work has pushed the boundaries of LLM performance in specialized scientific question-answering. Through projects like AstroMLab, I have demonstrated benchmark-topping performance in astronomy Q&A using domain-specialized reasoning models, including a 70B-parameter model and an 8B-parameter model achieving GPT-4o level performance in astronomy-specific tasks. This showcases that carefully specialized smaller models can rival or exceed larger general-purpose models in specific domains, offering significant advantages in computational efficiency. To ensure scientific rigor, I established EAIRA, a robust methodology for evaluating AI models as scientific research assistants, assessing their capabilities in hypothesis generation and data interpretation. My most recent work extends into ArgoLOOM, exploring agentic AI frameworks for fundamental physics, aiming to create autonomous AI systems that drive scientific inquiry from quarks to cosmos.

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
