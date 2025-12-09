---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The burgeoning field of foundation models represents a transformative paradigm in artificial intelligence, offering immense potential to revolutionize scientific discovery across diverse domains. These large-scale models, pre-trained on vast datasets, demonstrate remarkable capabilities in understanding, generating, and reasoning with complex information. In data-rich scientific disciplines such as astronomy and cosmology, the application of foundation models is particularly promising, addressing the challenges of analyzing petabytes of multi-modal data, interpreting specialized scientific literature, and performing intricate domain-specific reasoning tasks.

Scientific data often presents unique complexities, including heterogeneous formats (images, spectra, time series, simulations), the need for deep domain expertise for interpretation, and the sheer volume requiring automated yet intelligent processing. Traditional AI approaches often necessitate bespoke model development for each specific task. Foundation models offer a powerful alternative by adapting their pre-trained general knowledge to specialized scientific contexts through techniques like fine-tuning and prompt engineering, thereby enabling more efficient and comprehensive data analysis, hypothesis generation, and even interactive scientific inquiry.

My research has centered on pioneering the development and application of domain-specialized foundation models to address critical challenges in astronomy and cosmology. I have focused on building AI systems capable of understanding complex scientific data and language, facilitating accelerated discovery and intelligent assistance for researchers. This work spans the creation of multi-modal foundation models explicitly designed for handling diverse cosmological simulation data, enabling a holistic analysis of various data representations from large-scale simulations.

A significant contribution has been in training Large Language Models (LLMs) to acquire deep scientific domain knowledge. For instance, I have developed methodologies to effectively "teach LLMs to speak spectroscopy," allowing them to interpret and reason over highly specialized spectroscopic data, a cornerstone of astronomical observation. The AstroMLab series of projects further demonstrates this capability, with specialized LLMs, including an 8B-parameter model achieving GPT-4o level performance and a 70B-parameter model setting benchmark-topping results in astronomy Q&A, showcasing the power of domain-specialized reasoning models. Additionally, I have developed smart assistants like InferA, designed to navigate and extract meaningful insights from intricate cosmological ensemble data. Crucially, I have also established a rigorous methodology, EAIRA, for evaluating AI models as scientific research assistants, ensuring their reliability and utility in accelerating the scientific discovery process. These efforts are poised to provide powerful new tools for scientists, enhancing their ability to explore the universe.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants</div>
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
