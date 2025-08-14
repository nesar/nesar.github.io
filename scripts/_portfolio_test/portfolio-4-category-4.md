---
title: "Machine Learning in Astrophysical Discovery"
excerpt: "Research in machine learning in astrophysical discovery"
collection: portfolio
---

The formation of the first stars, known as Population III or primordial stars, marks a crucial epoch in cosmic history, bridging the dark ages after the Big Bang with the onset of cosmic reionization. These stars, formed from pristine hydrogen and helium, significantly influenced the early universe by emitting the first light, heating the intergalactic medium, and forging the first heavy elements. Simulating their formation and evolution is computationally intensive, requiring detailed hydrodynamical and chemical models across vast cosmological scales, making it challenging to explore the full parameter space of astrophysical initial conditions and environmental factors.

Machine learning, particularly deep learning, offers a transformative approach to overcome these computational bottlenecks and extract complex insights from high-dimensional astrophysical datasets. By learning intricate patterns and relationships within simulation outputs, machine learning models can accelerate predictions, classify phenomena, and identify subtle correlations that might elude traditional analysis methods. This paradigm shift enables researchers to explore previously inaccessible regions of parameter space, improve the resolution of large-scale simulations, and significantly enhance our understanding of cosmic structure formation and evolution.

My research focuses on leveraging advanced machine learning techniques to accelerate and enhance our understanding of fundamental processes in cosmology, specifically the emergence of the first stars. I have developed a deep convolutional neural network (CNN) model designed to predict localized primordial star formation. This model is trained on large-scale cosmological simulation data, learning the intricate interplay of gravitational collapse, gas dynamics, and chemical processes that lead to the birth of the universe's earliest luminous objects within specific regions. The CNN can efficiently identify and predict the precise locations where primordial stars are likely to form, a critical step for understanding their clustering and impact on the early universe.

This methodology represents a significant technical contribution, providing a fast and accurate surrogate for expensive hydrodynamical simulations. By deploying this CNN, I can rapidly assess the likelihood and spatial distribution of primordial star formation across a wide range of cosmological scenarios and initial conditions. The immediate impact of this work is the ability to generate large statistical samples of primordial star-forming regions, which is crucial for predicting observational signatures for next-generation telescopes and for understanding the early universe's reionization process. Ultimately, this work pushes the boundaries of predictive astrophysics, enabling more comprehensive exploration of the cosmic dawn.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/predicting-localized-primordial-star-formation-wit_plot_1_20ccb55a.png" alt="Figure from Predicting Localized Primordial Star Formation with Deep Convolutional Neural Networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Predicting Localized Primordial Star Formation with Deep Convolutional Neural Networks</div>
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
