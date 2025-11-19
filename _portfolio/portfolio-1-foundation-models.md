---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The advent of foundation models, particularly large language models (LLMs), has inaugurated a transformative era across numerous disciplines. In scientific research, these models offer unparalleled opportunities to distill complex information, process vast datasets, generate hypotheses, and accelerate discovery. However, the unique challenges of scientific data—ranging from highly specialized jargon and symbolic representations to multi-modal data streams from simulations and observatories—necessitate the development of bespoke methodologies to unlock the full potential of these powerful AI systems.

A significant frontier lies in equipping these models with the capability to deeply understand and reason within scientific domains, such as astrophysics and cosmology. This involves not only training them on domain-specific corpora but also enabling them to interpret raw scientific data, process multi-modal inputs, and perform complex quantitative reasoning. The goal is to move beyond mere information retrieval towards creating intelligent research assistants capable of genuine scientific inquiry, accelerating the analysis of massive datasets from cosmological simulations, spectroscopic observations, and other experimental setups.

Crucial to this endeavor is the establishment of robust frameworks for evaluating AI models as scientific research assistants. This requires methodologies that go beyond traditional NLP benchmarks, assessing their capacity for scientific reasoning, data interpretation, and problem-solving within real-world scientific contexts. Specialized domain adaptation techniques, efficient fine-tuning strategies, and the development of benchmarks reflecting the intricacies of scientific workflows are paramount for fostering AI systems that can genuinely assist in pushing the boundaries of human knowledge.

My research at the intersection of foundation models and scientific discovery focuses on pioneering these specialized AI systems and methodologies. I have developed multi-modal foundation models specifically designed to interpret complex cosmological simulation data, enabling deeper insights into the universe's evolution. A core contribution has been "teaching LLMs to speak spectroscopy," bridging the gap between natural language understanding and the intricate patterns of astronomical spectra, thereby making specialized data more accessible for analysis and interpretation. Through projects like "InferA," I have engineered smart assistants for cosmological ensemble data, automating and streamlining complex analytical tasks.

Furthermore, my "AstroMLab" series has demonstrated the profound impact of domain-specialized reasoning models. I have achieved benchmark-topping performance in astronomy Q&A with a 70B-parameter model, and notably, reached GPT-4o level performance in astronomy with a significantly smaller, specialized 8B-parameter LLM, highlighting the efficiency and power of domain adaptation. My work also extends to establishing rigorous evaluation methodologies, such as EAIRA, for assessing AI models as true scientific research assistants. Most recently, with ArgoLOOM, I am developing agentic AI for fundamental physics, creating intelligent systems that can navigate complex experimental setups and theoretical frameworks from quarks to cosmos, fundamentally advancing scientific exploration.

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
