---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

The field of astronomy and cosmology is characterized by an exponential growth in data volume and complexity, encompassing diverse modalities such as observational images, simulation outputs, and spectroscopic measurements. Extracting meaningful scientific insights from this deluge requires increasingly sophisticated analytical tools. Traditional data analysis methods often struggle with the scale, heterogeneity, and intricate correlations inherent in these datasets, necessitating the development of advanced artificial intelligence paradigms. Foundation models, with their remarkable emergent capabilities in understanding and generating complex information, offer a promising avenue to address these challenges.

Developing foundation models tailored for scientific domains, particularly astronomy, involves significant technical hurdles. General-purpose models often lack the specialized knowledge, nuanced reasoning abilities, and multi-modal interpretation skills required for precise scientific inquiry. Research in this area focuses on creating domain-specialized large language models (LLMs) capable of sophisticated scientific question-answering and reasoning, as well as multi-modal foundation models that can seamlessly integrate and interpret heterogeneous astronomical data types. A crucial aspect of this development is also establishing robust methodologies for evaluating these AI systems as legitimate scientific research assistants, ensuring their reliability and utility in the discovery process.

My work has centered on pioneering the application and specialization of foundation models to tackle the unique challenges within astronomy and cosmology. I have developed multi-modal foundation models specifically designed to interpret complex cosmological simulation data, enabling deeper insights into cosmic structures and evolution. A key focus has been to enhance LLMs with domain-specific knowledge, as demonstrated by "Teaching LLMs to Speak Spectroscopy," which imbues these models with the ability to understand and reason about intricate spectroscopic data. Furthermore, I have engineered "InferA," a smart assistant tailored for efficiently navigating and analyzing vast cosmological ensemble data, streamlining the process of scientific discovery.

Through the "AstroMLab" series, I have introduced a suite of domain-specialized reasoning models, progressively advancing their performance in astronomical question-answering. "AstroMLab 3," an 8B-parameter specialized LLM, achieved performance levels comparable to generalist models like GPT-4o in astronomy benchmarks, showcasing the power of domain adaptation. Building on this, "AstroMLab 4" escalated this capability further, developing a 70B-parameter domain-specialized reasoning model that established new benchmark-topping performance in comprehensive astronomy Q&A. Complementing these developments, my work on "EAIRA" established a rigorous methodology for evaluating the efficacy and reliability of AI models serving as scientific research assistants, providing a framework to assess their genuine contributions to scientific inquiry.

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
