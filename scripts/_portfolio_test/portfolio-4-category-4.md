---
title: "Machine Learning in Astrophysical Simulations"
excerpt: "Research in machine learning in astrophysical simulations"
collection: portfolio
---

Astrophysical simulations are indispensable tools for unraveling the complex processes that govern the universe, from galaxy formation and black hole evolution to the cosmic web and the earliest epochs. These simulations model the intricate interplay of gravity, hydrodynamics, radiation, and magnetic fields across vast cosmic scales and billions of years. However, achieving high fidelity and resolving intricate physical phenomena often comes at an immense computational cost, requiring supercomputing resources and extensive runtimes, which can limit the scope of parameter space exploration and the detailed study of rare events.

The emerging synergy between machine learning (ML) and astrophysical simulations offers a transformative approach to overcome these computational bottlenecks and extract deeper insights from vast datasets. Machine learning techniques, including deep learning, reinforcement learning, and dimensionality reduction, are increasingly employed to accelerate simulations, build surrogate models, classify astrophysical objects, identify rare events, and infer complex physical parameters. This interdisciplinary field promises to revolutionize our ability to understand cosmic evolution by enabling more efficient analysis, discovery, and prediction, opening new avenues for scientific inquiry.

My research contributes to this pivotal intersection, specifically focusing on applying advanced machine learning techniques to illuminate the mysteries of the early universe. I have developed a novel framework that leverages Deep Convolutional Neural Networks (CNNs) to predict localized primordial star formation. This application is critical for understanding the epoch of reionization and the origins of the first luminous structures, which are foundational to cosmic evolution but are exceedingly difficult to resolve in traditional simulations due to their sensitivity to initial conditions and the immense dynamic range required.

Specifically, I utilized the pattern recognition capabilities of CNNs to analyze simulated cosmological gas properties, such as density, temperature, and metallicity, identifying the precise locations within vast cosmic volumes where the unique conditions for primordial star collapse are met. By training these networks on high-resolution hydrodynamic simulations, I demonstrated that CNNs can accurately and rapidly predict these rare formation sites. This methodology not only significantly accelerates the identification of key astrophysical events, bypassing computationally expensive high-resolution re-simulations of entire regions, but also enables more comprehensive exploration of the parameter space governing the formation of the first stars, ultimately deepening our understanding of the universe's earliest epochs.

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
