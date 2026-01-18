---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The rapid advancements in artificial intelligence, particularly the development of foundation models and Large Language Models (LLMs), present transformative opportunities for scientific research. These sophisticated models, capable of processing and generating human-like text, understanding complex patterns, and performing intricate reasoning tasks, are poised to revolutionize how scientists interact with vast and intricate datasets. In fields like astronomy and cosmology, where data volumes are immense and analytical tasks often require deep domain expertise, leveraging these AI paradigms can significantly accelerate discovery and overcome traditional analytical bottlenecks.

A critical challenge lies in adapting these general-purpose foundation models to the highly specialized and often nuanced language and data structures of scientific disciplines. This adaptation requires not only fine-tuning models on domain-specific corpora but also developing multi-modal architectures that can interpret diverse data types, such as spectroscopic measurements, simulation outputs, and observational imagery, alongside textual information. Furthermore, robust methodologies are essential for evaluating the scientific utility and trustworthiness of AI models acting as research assistants, ensuring they provide accurate, interpretable, and verifiable insights.

My work extensively addresses these challenges by pioneering the development and application of specialized foundation models for scientific inquiry, particularly within astronomy and cosmology. I have spearheaded efforts to create multi-modal foundation models capable of understanding complex cosmological simulation data, demonstrated through projects like InferA, a smart assistant designed to interpret cosmological ensemble datasets. A core focus has been "teaching" LLMs the intricate language of scientific data, such as spectroscopy, by developing novel techniques for domain adaptation that enable these models to grasp specialized concepts and perform advanced reasoning, going beyond simple fact retrieval.

Through the AstroMLab series, I have developed and benchmarked domain-specialized reasoning models that achieve state-of-the-art performance in astronomy Q&A. For instance, AstroMLab 3, an 8B-parameter model, demonstrates performance on par with GPT-4o in astronomy tasks, highlighting the efficiency and effectiveness of domain specialization. Further pushing these boundaries, AstroMLab 4, a 70B-parameter model, has achieved benchmark-topping results, showcasing superior reasoning capabilities tailored for complex scientific questions. Crucially, I have established a rigorous methodology, EAIRA, for evaluating AI models as scientific research assistants, providing a framework to assess their scientific integrity and practical utility. These contributions democratize access to advanced analytical capabilities, accelerate scientific discovery, and lay the groundwork for a new generation of intelligent scientific research tools.

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
