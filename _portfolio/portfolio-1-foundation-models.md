---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The rapidly expanding field of foundation models is revolutionizing how complex data is analyzed and understood across scientific disciplines. In astronomy and cosmology, researchers are confronted with increasingly vast, intricate, and multi-modal datasets stemming from large-scale simulations and cutting-edge observational instruments. These datasets often contain petabytes of information across various modalities, including images, numerical tables, time series, and spectra, posing significant challenges for traditional analysis methods and human comprehension.

Foundation models, particularly Large Language Models (LLMs) and multi-modal variants, offer transformative potential by learning deep representations and emergent reasoning capabilities from massive amounts of data. Their ability to process natural language queries, interpret diverse data types, and generate scientific insights positions them as powerful assistants for accelerating discovery. The development of specialized foundation models tailored to the unique complexities of astrophysical data is crucial for unlocking new scientific understanding, streamlining research workflows, and enabling intelligent exploration of the universe.

Research in this area focuses on developing and evaluating sophisticated AI systems that can serve as intelligent research assistants for astronomers and cosmologists. This includes creating smart assistants designed to navigate and interpret complex cosmological ensemble data, as well as developing multi-modal foundation models capable of integrating and reasoning across diverse data types found in simulations. A significant thrust involves adapting and training LLMs to understand and generate insights from highly specialized scientific language and data formats, such as spectroscopic measurements, and to achieve expert-level performance in astronomy-specific question-answering tasks. Furthermore, establishing rigorous methodologies for evaluating the scientific utility and trustworthiness of these AI models is a critical component for their responsible integration into the scientific research paradigm.

My work contributes significantly to these advancements by developing and rigorously evaluating domain-specialized foundation models for astrophysics. I have led the creation of the AstroMLab series of models, which are explicitly designed for astronomy question-answering and reasoning. This includes developing 8B and 70B parameter domain-specialized reasoning models that have demonstrated benchmark-topping performance, achieving and often surpassing GPT-4o-level capabilities in complex astronomy Q&A, even outperforming humans in challenges like Astronomy Jeopardy!. A key technical contribution involved fine-tuning these LLMs with vast quantities of astrophysical texts and data, enabling them to comprehend nuanced scientific concepts and provide accurate, contextually relevant answers.

Furthermore, my research extends to addressing critical multi-modal challenges. I have developed methodologies for teaching LLMs to "speak spectroscopy," enabling them to interpret and generate insights from intricate spectroscopic data, which is vital for understanding celestial object properties. The InferA project exemplifies the creation of smart assistants for navigating vast cosmological ensemble data, facilitating interactive and intelligent data exploration. Crucially, I have also established a comprehensive framework, EAIRA, for evaluating the efficacy and reliability of AI models as scientific research assistants, ensuring their rigorous assessment against scientific standards. These efforts collectively push the boundaries of AI in scientific discovery, providing powerful, intelligent tools that significantly enhance research productivity and accelerate our understanding of the cosmos.

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
