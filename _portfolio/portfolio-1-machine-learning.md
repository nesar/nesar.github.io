---
title: "Machine Learning & AI"
excerpt: "Research in machine learning & ai <br/><img src='/images/research_machine-learning.png'>"
collection: portfolio
---

Summary: General-purpose large language models, despite their broad capabilities,
often struggle with specialized domain knowledge, a limitation particularly
pronounced in more accessible, lower-parameter versions. This gap hinders their
deployment as effective agents in demanding fields such as ast...

## Research Figures

<div class="research-figures-grid">
  <div class="research-figure">
    <img src="/images/research/figures/modular_deep_learning_analysis_of_galaxy-scale_str_page2_fig1_08332ab9.png" alt="Figure from Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images" onclick="openModal(this)">
    <p class="figure-caption">From: Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/modular_deep_learning_analysis_of_galaxy-scale_str_page8_fig1_83695984.png" alt="Figure from Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images" onclick="openModal(this)">
    <p class="figure-caption">From: Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/modular_deep_learning_analysis_of_galaxy-scale_str_page8_fig2_7db0c93a.png" alt="Figure from Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images" onclick="openModal(this)">
    <p class="figure-caption">From: Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images</p>
  </div>
</div>

<style>
.research-figures-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.research-figure {
  text-align: center;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  transition: transform 0.2s ease;
}

.research-figure:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.research-figure img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.research-figure img:hover {
  opacity: 0.9;
}

.figure-caption {
  font-size: 0.85em;
  color: #6c757d;
  margin-top: 0.5rem;
  line-height: 1.3;
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
  width: 80%;
  max-width: 700px;
  padding-top: 5%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}
</style>

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
</script>

## Related Publications (36 papers):

- **AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a
  70B-Parameter Domain-Specialized Reasoning Model** (2025) - Preprint
- **EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific
  Research Assistants** (2025) - Preprint
- **Constraining Early Dark Energy Models with Power Spectra Emulators** (2025) - Bulletin of the American Physical Society
- **AstroMLab 1: Who wins astronomy jeopardy!?** (2025) - Astronomy and Computing
- **Snowmass2021-Letter of Interest Scientific AI Approaches in Computational Cosmology** (2025) - Preprint
- **GAN-based Event-level Inverse Mapper (GEIM)-An Application on Quantum Chromodynamics Global Analysis** (2025) - Preprint
- **Deconvolution of Astronomical Images with Deep Neural Networks** (2025) - Preprint
- **Data-Efficient Dimensionality Reduction and Surrogate Modeling of High-Dimensional Stress Fields** (2025) - Journal of Mechanical Design
- **AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a
  Specialized 8B-Parameter Large Language Model** (2024) - Preprint
- **Benchmarking AI-evolved cosmological structure formation and expanding dimensions through parallelization frameworks** (2024) - APS April Meeting Abstracts