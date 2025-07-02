---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The field of Dark Matter and Cosmology stands at the forefront of modern astrophysics, seeking to unravel the fundamental constituents and evolutionary history of our universe. While the Lambda-CDM model successfully describes a vast array of cosmological observations, it posits that most of the universe's matter content is in an unknown form, dubbed "dark matter," and its accelerated expansion is driven by "dark energy." Understanding the nature of these enigmatic components, along with exploring potential deviations from General Relativity on cosmic scales, remains a paramount challenge.

To address these profound questions, researchers employ diverse observational techniques and theoretical frameworks. These include precision measurements of the large-scale structure of the universe, analysis of galaxy clusters, mapping the distribution and kinematics of stellar populations within galaxies, and identifying the earliest generations of stars. Such studies are crucial for testing alternative theories of gravity, charting the fine-grained structure of dark matter halos, and characterizing the intricate cosmic web that permeates the universe.

My research contributes significantly to these endeavors through a multi-faceted approach. I have developed and applied sophisticated techniques to probe the nature of dark matter and cosmological models. For instance, I utilized a k-cut cosmic shear analysis of Hyper Suprime-Cam (HSC) first-year data to place stringent constraints on modified gravity theories, specifically f(R) gravity, by examining distortions in the shapes of distant galaxies. Concurrently, my work extends to mapping the Milky Way's structure; I constructed a photometric sample of 2.6 million Red Clump stars to trace the distribution of stars from the inner to the outer galaxy, providing insights into our galaxy's assembly history.

Furthermore, I have made significant advancements in characterizing the fine-grained structure of the cosmic web and dark matter halos. I pioneered the application of a "multistream view" and "caustic design" formalism to understand the topology and geometry of the dark matter web, revealing the complex internal structure of halos and the surrounding cosmic filaments. This method offers a novel way to visualize and analyze the multi-stream nature of collisionless dark matter flows. My research also encompasses identifying new cosmological probes, such as the SPTpol Extended Cluster Survey, which helps identify galaxy clusters as massive structures for cosmological studies, and searching for Carbon-Enhanced Metal-Poor star candidates using BP/RP spectra from Gaia DR3, which serve as relics from the early universe, shedding light on the first stars and chemical enrichment. Through these diverse projects, my work provides crucial observational constraints and theoretical insights necessary to refine our understanding of cosmic evolution and fundamental physics.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from topology and geometry of the dark matter web a mul" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: topology and geometry of the dark matter web a mul</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from the caustic design of the dark matter web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: the caustic design of the dark matter web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_2_ec781175.png" alt="Figure from topology and geometry of the dark matter web a mul" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: topology and geometry of the dark matter web a mul</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_3_a3b0a1c0.png" alt="Figure from the caustic design of the dark matter web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: the caustic design of the dark matter web</div>
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
