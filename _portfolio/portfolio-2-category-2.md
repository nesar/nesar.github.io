---
title: "Machine Learning for Astrophysical Data Analysis"
excerpt: "Research in machine learning for astrophysical data analysis"
collection: portfolio
---

Modern astronomy is characterized by an unprecedented deluge of data from ground-based and space-borne observatories, presenting both immense opportunities and significant challenges. Extracting meaningful scientific insights from these vast and complex datasets often exceeds the capabilities of traditional analytical methods. Machine learning (ML) has thus emerged as a transformative paradigm, offering powerful tools to automate data processing, identify subtle patterns, classify objects, and detect anomalies across various astronomical domains.

The application of machine learning in astrophysics spans a wide array of research areas. This includes the development of sophisticated models for analyzing spectroscopic data, which are crucial for understanding the composition and dynamics of celestial objects. Machine learning techniques are also vital for processing and interpreting astronomical images, enabling tasks such as galaxy morphological classification, the efficient detection of rare or transient phenomena, and the precise deconvolution of instrumental effects like the Point Spread Function. Furthermore, the advent of large language models (LLMs) is revolutionizing how astronomical knowledge is accessed, analyzed, and disseminated, promising to enhance discovery and education within the field.

My research extensively explores and expands the frontiers of machine learning applications in astrophysics, with a particular focus on developing innovative methodologies for complex data challenges. A significant portion of my work centers on domain-specialized large language models for astronomy. Through the AstroMLab series, I have engineered models, including 70B and 8B parameter variants, that achieve benchmark-topping performance in astronomy question-answering and reasoning, often surpassing general-purpose LLMs and reaching GPT-4o level capabilities for specific tasks. I have also focused on "Teaching LLMs to Speak Spectroscopy," enabling these models to interpret complex spectroscopic data, and developed SYTH-Z, a machine learning approach using synthetic spectra for robust probabilistic redshift estimation.

My contributions further extend to advancing machine learning for comprehensive astronomical image analysis. I have developed generative adversarial networks (GANs) for efficient anomaly detection in galaxy images from surveys like Hyper Suprime-Cam, identifying novel celestial objects. My work explores galaxy morphology "Beyond the Hubble Sequence" using unsupervised machine learning, uncovering new classifications and insights into galaxy evolution. Additionally, I designed a modular deep learning pipeline for strong gravitational lens detection and modeling, crucial for probing dark matter, and employed neural networks for accurate Point Spread Function deconvolution to enhance image fidelity. These efforts collectively push the boundaries of astronomical discovery, making complex datasets more interpretable and enabling the automated identification of crucial scientific targets.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 1: Who Wins Astronomy Jeopardy!?" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 1: Who Wins Astronomy Jeopardy!?</div>
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
