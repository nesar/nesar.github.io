---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The burgeoning volume and complexity of scientific data, particularly in fields such as cosmology and astrophysics, present significant challenges for researchers seeking to extract knowledge and make new discoveries. Large-scale simulations generate petabytes of multi-modal data, while advanced observatories collect intricate spectra and images daily. Interpreting this wealth of information, formulating hypotheses, and answering complex scientific questions increasingly demand advanced computational tools that can process, understand, and reason over diverse data types.

Foundation models, including large language models (LLMs) and multi-modal models, have emerged as powerful paradigms for addressing these challenges. While initially trained on broad internet data, their potential for scientific applications lies in their ability to generalize, understand context, and perform complex reasoning. However, general-purpose models often lack the specialized domain knowledge, the capability to interpret specific scientific data formats (e.g., spectroscopic plots, cosmological density fields), and the rigorous reasoning skills required for scientific inquiry. This necessitates the development of domain-specialized foundation models that are adept at understanding scientific language, data, and methodologies.

My research focuses on pioneering the application and specialization of foundation models to accelerate discovery and enhance research workflows in astronomy and cosmology. I have developed innovative methodologies and deployed specialized AI agents that demonstrate benchmark-topping performance in understanding complex astronomical data and answering scientific questions. For instance, I created multi-modal foundation models specifically designed to interpret cosmological simulation data, bridging the gap between raw numerical outputs and high-level scientific concepts. Furthermore, I have engineered novel techniques to "teach LLMs to speak spectroscopy," enabling these models to comprehend and reason over intricate spectroscopic data, which are fundamental to astrophysical analysis.

A significant portion of my work has involved developing and evaluating the AstroMLab series of domain-specialized reasoning models, including AstroMLab 1, AstroMLab 3, and AstroMLab 4. These models, ranging from an efficient 8B-parameter model achieving GPT-4o level performance in astronomy Q&A to a robust 70B-parameter variant, set new performance benchmarks for scientific reasoning within the astronomical domain. Beyond model development, I have also established critical evaluation methodologies, such as EAIRA, which provides a rigorous framework for assessing the efficacy of AI models as scientific research assistants. This comprehensive approach, combining advanced model development with robust evaluation, culminates in practical tools like InferA, a smart assistant designed to aid researchers in navigating and interpreting complex cosmological ensemble data, ultimately enhancing scientific productivity and accelerating discovery.

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
