---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a transformative approach to artificial intelligence in scientific applications, particularly in astronomy and astrophysics. This research area focuses on developing specialized large language models (LLMs) that can understand and reason about domain-specific scientific content. The work encompasses comprehensive evaluation methodologies for AI models in scientific contexts, benchmark development for astronomical question-answering, and the creation of robust frameworks for assessing AI performance in research assistance tasks.

The research demonstrates significant advances in model specialization, showing that domain-focused models can achieve performance comparable to much larger general-purpose systems. The evaluation frameworks developed provide crucial infrastructure for responsible AI deployment in scientific workflows, establishing standards for reliability and accuracy assessment.

My work in this area has centered on developing the AstroMLab series of models, which showcase the effectiveness of domain specialization in achieving superior performance on astronomy-related tasks. I have also contributed to establishing rigorous evaluation methodologies through the EAIRA project, providing frameworks that enable systematic assessment of AI capabilities as research assistants. These contributions help bridge the gap between general AI capabilities and the specific needs of scientific research communities.

## Representative Research Figures

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/EAIRA_Establishing_a_Methodology_for_Evaluating_AI_plot_1_adce1f78.png" alt="Figure from EAIRA Establishing a Methodology for Evaluating AI" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA Establishing a Methodology for Evaluating AI</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/EAIRA_Establishing_a_Methodology_for_Evaluating_AI_plot_2_205db31f.png" alt="Figure from EAIRA Establishing a Methodology for Evaluating AI" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA Establishing a Methodology for Evaluating AI</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/EAIRA_Establishing_a_Methodology_for_Evaluating_AI_plot_3_1c174bef.png" alt="Figure from EAIRA Establishing a Methodology for Evaluating AI" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA Establishing a Methodology for Evaluating AI</div>
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

/* Modal styles */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 90%;
  max-width: 1000px;
  max-height: 90vh;
  object-fit: contain;
  margin-top: 2%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.3s ease;
}

.close:hover {
  color: #bbb;
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

// Close modal when clicking outside the image
window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}

// Close modal with escape key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeModal();
  }
});
</script>
