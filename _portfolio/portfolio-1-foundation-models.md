---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Scientific research, particularly in fields like astrophysics, is increasingly confronted with vast and complex datasets, ranging from high-resolution cosmological simulations to intricate observational spectra. Extracting meaningful insights, identifying patterns, and formulating new hypotheses from this deluge of information presents significant challenges for human researchers. This landscape necessitates the development of advanced artificial intelligence solutions capable of augmenting human intellect and accelerating the pace of discovery across scientific domains.

Foundation models, including large language models (LLMs) and multi-modal architectures, are emerging as transformative tools in this context. Their ability to learn rich representations from massive datasets, coupled with their powerful reasoning and generative capabilities, positions them as ideal candidates for scientific data interpretation, automated question answering, and intelligent assistance. However, adapting these general-purpose models to specialized scientific domains requires sophisticated methodologies to imbue them with domain-specific knowledge, handle diverse data types (text, images, numerical tables, spectra), and ensure scientific accuracy and reliability.

My research addresses these critical needs by developing and applying cutting-edge foundation models to various scientific domains, with a primary focus on astrophysics. I have engineered multi-modal foundation models specifically designed to interpret and analyze complex cosmological simulation data, as demonstrated in my work on "Multi-modal Foundation Model for Cosmological Simulation Data." This has culminated in the creation of intelligent assistants like InferA, a smart assistant tailored for cosmological ensemble data, enabling more intuitive exploration and hypothesis generation within vast datasets. This work involves developing methodologies to effectively integrate diverse data modalities and leverage their reasoning capabilities for scientific inquiry.

Furthermore, a significant portion of my work centers on advancing the capabilities of large language models for scientific question answering and reasoning. Through projects like AstroMLab 1, 3, and 4, I have developed highly specialized, domain-aware LLMs, including models with up to 70 billion parameters, that achieve benchmark-topping performance in astronomy Q&A. These models not only outperform general-purpose LLMs but have also demonstrated GPT-4o level performance with significantly smaller architectures (e.g., 8B parameters) due to specialized training on curated scientific corpora and novel fine-tuning techniques. Beyond textual data, I have also pioneered methods for "Teaching LLMs to Speak Spectroscopy," enabling these models to interpret and reason about complex spectral data, which is fundamental to astrophysical analysis. Recognizing the paramount importance of reliability in scientific AI, I established a rigorous methodology in EAIRA for evaluating AI models as scientific research assistants, ensuring their utility and trustworthiness in scientific discovery.

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
