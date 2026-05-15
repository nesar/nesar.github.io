---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Modern scientific fields like astronomy and cosmology generate vast, complex datasets, from high-fidelity simulations of the universe's evolution to diverse observational data across various electromagnetic spectra. Extracting meaningful insights, identifying subtle patterns, and answering sophisticated research questions from this data demands significant computational resources and highly specialized human expertise, often bottlenecking the pace of scientific discovery.

Foundation models offer a powerful paradigm for addressing these challenges. Their ability to learn from immense amounts of data and generalize across diverse tasks makes them uniquely suited for complex scientific domains, integrating various modalities such as images, time-series, and textual representations. Developing robust and reliable AI tools that can effectively assist researchers, automate analytical tasks, and even propose new hypotheses is a critical endeavor for accelerating scientific progress in this data-driven era.

This research portfolio pioneers the application and specialization of foundation models to tackle these grand challenges in astronomical and cosmological research. A core emphasis is placed on developing models that are not only powerful but also scientifically accurate, interpretable, and capable of operating as true scientific research assistants. This involves tailoring general-purpose AI architectures to the specific semantic and structural complexities of scientific data, establishing rigorous evaluation methodologies, and pushing the boundaries of what AI can achieve in scientific contexts.

My work has systematically explored and advanced the use of foundation models in astronomy and cosmology, from fundamental model development to practical application and evaluation. I have developed multi-modal foundation models specifically designed to interpret complex cosmological simulation data, leading to tools like InferA, a smart assistant for navigating and extracting insights from cosmological ensemble data. Through the AstroMLab series (AstroMLab 1, 3, and 4), I created highly specialized large language models for astronomy Q&A. These efforts culminated in an 8B-parameter model achieving GPT-4o level performance and a 70B-parameter domain-specialized reasoning model that consistently delivers benchmark-topping performance in answering intricate astronomy questions.

Furthermore, I addressed the challenging integration of highly specialized data types into these models, demonstrated by "Teaching LLMs to Speak Spectroscopy," which enables language models to interpret and reason about complex spectral data—a cornerstone of astronomical analysis. Recognizing the critical need for scientific rigor, I established EAIRA, a comprehensive methodology for evaluating AI models specifically as scientific research assistants, ensuring their reliability and trustworthiness. These contributions collectively aim to equip the scientific community with advanced AI tools capable of accelerating discovery and transforming the landscape of data-intensive research.

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
