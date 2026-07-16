---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models are rapidly transforming the landscape of scientific research, offering unprecedented capabilities for processing, interpreting, and reasoning over vast and complex datasets. In fields like astronomy and cosmology, which generate terabytes of observational and simulation data annually, these advanced AI systems are becoming indispensable tools. Traditional analytical methods often struggle with the sheer scale, multi-modal nature, and inherent complexity of astrophysical information, necessitating a new generation of intelligent assistants capable of understanding domain-specific language, recognizing intricate patterns across diverse data types, and performing sophisticated scientific reasoning.

The development of specialized foundation models is particularly crucial because general-purpose AI, while powerful, frequently lacks the nuanced domain expertise, interpretability, and robust performance required for rigorous scientific inquiry. These domain-adapted models are engineered to handle the unique challenges of scientific data, from high-dimensional cosmological simulations to spectral measurements and text-based scientific literature. Their aim is to accelerate discovery, empower researchers with intelligent assistants, and unlock new insights by automating complex data analysis, answering intricate scientific questions, and even generating novel hypotheses.

My research focuses on developing and rigorously evaluating highly specialized foundation models tailored for the unique demands of astronomy and cosmology. I have spearheaded the AstroMLab series, demonstrating the profound impact of domain-specialized Large Language Models. For instance, AstroMLab 3, an 8-billion-parameter model, achieved GPT-4o level performance in astronomy question-answering, while AstroMLab 4, leveraging a 70-billion-parameter architecture, set new benchmarks in domain-specialized reasoning. These advancements were critically evaluated using novel frameworks like "Who Wins Astronomy Jeopardy!?", ensuring robust assessment of their knowledge and reasoning capabilities.

Beyond text-based reasoning, my work extends to multi-modal foundation models for complex scientific data. This includes the development of multi-modal foundation models specifically designed to interpret cosmological simulation data, and projects like InferA, a smart assistant for navigating and analyzing vast cosmological ensemble datasets. A key contribution involves "Teaching LLMs to Speak Spectroscopy," establishing methodologies for these models to understand and interpret spectral data, a cornerstone of astrophysical analysis. Furthermore, I developed EAIRA, a comprehensive methodology for systematically evaluating AI models as scientific research assistants, ensuring their scientific validity and practical utility. These efforts underscore the potential for AI to act as indispensable partners, significantly accelerating scientific discovery and fostering new insights across diverse astrophysical datasets.

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
