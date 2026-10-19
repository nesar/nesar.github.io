---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a transformative paradigm in artificial intelligence, offering immense potential for generalization across a wide array of tasks. These large-scale, pre-trained models, predominantly leveraging transformer architectures, have showcased impressive capabilities in areas such as natural language processing and computer vision. However, their direct application to complex scientific domains—characterized by unique data modalities, intricate relationships, and a stringent demand for accuracy and interpretability—presents significant challenges. Adapting these powerful models for scientific discovery necessitates specialized approaches that can effectively integrate domain-specific knowledge and handle diverse data types, ranging from high-resolution simulations to nuanced observational measurements.

The pursuit of advanced scientific AI therefore involves developing sophisticated methodologies for training, fine-tuning, and rigorously evaluating foundation models to function as effective tools for researchers. This includes addressing the critical need for models capable of complex reasoning, seamless multi-modal data integration, and precise interpretation of domain-specific language and phenomena. Research in this area focuses on creating specialized models that not only deeply understand the intricacies of scientific data but also provide reliable assistance in tasks such as advanced data analysis, hypothesis generation, and sophisticated question answering, thereby significantly accelerating the pace of scientific exploration and discovery.

My research extensively explores the development and application of domain-specialized foundation models, particularly within astrophysics and cosmology, to overcome these inherent limitations. I have developed multi-modal foundation models specifically designed to interpret complex cosmological simulation data, integrating diverse data types to extract deeper, interconnected insights into cosmic structures. A significant part of my work involves effectively "teaching" large language models (LLMs) to understand and generate domain-specific information, as demonstrated by efforts in enabling LLMs to "speak spectroscopy," thereby making them highly proficient in analyzing and interpreting the nuanced spectroscopic data crucial for astrophysical understanding.

Furthermore, I have led the development of the AstroMLab series of models, which exemplify how specialized training and architectural considerations can yield benchmark-topping performance in astronomy-focused Q&A. For instance, AstroMLab 3, an 8B-parameter model, achieved performance comparable to advanced general-purpose models like GPT-4o in astronomy tasks, showcasing the efficiency of domain specialization. This line of research culminated in AstroMLab 4, a 70B-parameter domain-specialized reasoning model, which has set new benchmarks in astronomy Q&A. Beyond model development, I established EAIRA, a robust methodology for evaluating AI models as scientific research assistants, ensuring their reliability and utility in real-world research settings and paving the way for trustworthy AI integration into scientific workflows.

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
