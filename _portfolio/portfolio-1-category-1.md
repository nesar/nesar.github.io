---
title: "Cosmology & Large Scale Structure Physics"
excerpt: "Research in cosmology & large scale structure physics"
collection: portfolio
---

Cosmology and Large Scale Structure (LSS) physics is a vibrant field dedicated to unraveling the fundamental constituents and evolutionary history of the universe. It investigates how gravity molds the cosmos, from the initial quantum fluctuations in the early universe to the complex "cosmic web" of galaxies, clusters, and voids observed today. A central challenge lies in understanding the nature of dark matter and dark energy, which dominate the universe's mass-energy budget, and in testing the validity of general relativity on cosmological scales through models like modified gravity.

Researchers in this area employ a diverse array of observational techniques, including analyses of the cosmic microwave background, galaxy surveys, weak gravitational lensing (cosmic shear), and the Sunyaev-Zel'dovich effect. These observations are then confronted with theoretical predictions derived from N-body simulations and sophisticated analytical models. A key objective is to precisely constrain cosmological parameters, probe deviations from the standard Lambda-CDM model, and elucidate the intricate dynamics of structure formation. This often necessitates the development of advanced statistical and computational methods to extract maximal information from increasingly large and complex datasets.

My research significantly contributes to these efforts by developing and applying cutting-edge methodologies to address key questions in cosmology. I have focused on testing fundamental physics, such as constraining alternative theories of gravity. For instance, my work includes a $k$-cut cosmic shear analysis of Hyper Suprime-Cam data to place robust limits on $f(R)$ modified gravity models. Furthermore, I have extensively explored the intricate architecture of the dark matter web and its constituent haloes. My investigations involve developing a "multistream view" to understand the fine-grained structure, the "caustic design," and the underlying topology and geometry of these cosmic structures, which are crucial for interpreting galaxy formation and evolution. I have also contributed to major observational surveys, such as the SPTpol Extended Cluster Survey, enabling the detection and characterization of galaxy clusters through their thermal Sunyaev-Zel'dovich signatures.

A substantial part of my contribution lies in pioneering the application of advanced machine learning and deep neural network techniques to tackle complex problems in LSS. I have developed SHAMNet for differentiable predictions of large-scale structure, allowing for more efficient parameter inference and physical understanding. My work also includes physical benchmarking for AI-generated cosmic web models, ensuring their scientific fidelity, and developing deep neural networks for accurate peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect. Additionally, I have created matter power spectrum emulators for $f(R)$ modified gravity cosmologies, providing fast and precise theoretical predictions essential for large-scale data analysis. These developments collectively enhance our ability to extract cosmological information from observations, bridge the gap between theory and observation, and accelerate our understanding of the universe's evolution and its fundamental constituents.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from Topology and geometry of the dark matter web: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Topology and geometry of the dark matter web: a multistream view</div>
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
