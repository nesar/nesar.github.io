---
title: "Uncertainty Quantification"
excerpt: "Research in uncertainty quantification <br/><img src='/images/research_uncertainty-quantification.png'>"
collection: portfolio
---

Using Subaru Hyper Suprime-Cam (HSC) year 1 data, we perform the first -cut cosmic shear analysis constraining both  and  Hu-Sawicki modified gravity. To generate the  cosmic shear theory vector, we use the matter power spectrum emulator trained on COLA (COmoving Lagrangian Acceleration) simulations...

## Research Figures

<div class="research-figures-grid">
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_networks_for_fluid_flow_model_page3_fig1_5f12f899.png" alt="Figure from Probabilistic neural networks for fluid flow model-order reduction and data recovery" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural networks for fluid flow model-order reduction and data reco...</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_networks_for_fluid_flow_model_page7_fig1_820b622a.png" alt="Figure from Probabilistic neural networks for fluid flow model-order reduction and data recovery" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural networks for fluid flow model-order reduction and data reco...</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_networks_for_fluid_flow_model_page8_fig1_19190f02.png" alt="Figure from Probabilistic neural networks for fluid flow model-order reduction and data recovery" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural networks for fluid flow model-order reduction and data reco...</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_networks_for_fluid_flow_model_page9_fig1_ec3efcb7.png" alt="Figure from Probabilistic neural networks for fluid flow model-order reduction and data recovery" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural networks for fluid flow model-order reduction and data reco...</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_networks_for_fluid_flow_model_page9_fig2_4779d1b5.png" alt="Figure from Probabilistic neural networks for fluid flow model-order reduction and data recovery" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural networks for fluid flow model-order reduction and data reco...</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_networks_for_fluid_flow_model_page11_fig1_432a5c8d.png" alt="Figure from Probabilistic neural networks for fluid flow model-order reduction and data recovery" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural networks for fluid flow model-order reduction and data reco...</p>
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


## Related Publications (1 papers):

- **Constraining  gravity with a -cut cosmic shear analysis of the Hyper Suprime-Cam first-year data** (2021) - Physical Review D