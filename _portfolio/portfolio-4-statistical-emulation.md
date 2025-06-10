---
title: "Statistical Emulation & Inference"
excerpt: "Research in statistical emulation & inference <br/><img src='/images/research_statistical-emulation.png'>"
collection: portfolio
---

Developing statistical emulators and surrogate models for cosmological simulations, including power spectrum emulation and reduced-order modeling techniques.

## Research Figures

<div class="research-figures-grid">
  <div class="research-figure">
    <img src="/images/research/figures/application_of_probabilistic_modeling_and_automate_page11_fig2_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)">
    <p class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework f...</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_network-based_reduced-order_s_page3_fig1_bb04a767.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/application_of_probabilistic_modeling_and_automate_page9_fig2_a4ac7ae7.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)">
    <p class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework f...</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_network-based_reduced-order_s_page4_fig1_42cb185f.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</p>
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

## Related Publications ({sum(len(p['figures']) for p in papers)} figures from {len(papers)} papers):

- **Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field** (11 figures)
- **Probabilistic neural network-based reduced-order surrogate for fluid flows** (3 figures)
