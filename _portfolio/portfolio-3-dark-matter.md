---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter constitutes approximately 27% of the universe's mass-energy content and is the dominant component responsible for the formation and evolution of cosmic structures, including galaxies, galaxy clusters, and the intricate network known as the Cosmic Web. Despite its overwhelming gravitational influence, the fundamental nature of dark matter remains one of the most significant mysteries in modern cosmology. Research in this field aims to precisely map its distribution, understand its properties, and test the theoretical frameworks that describe its interaction with ordinary matter and the fabric of spacetime, including exploring alternative theories of gravity that might explain cosmic acceleration or structure formation without invoking new dark components.

The Cosmic Web, characterized by dense clusters interconnected by filaments, separated by vast voids, is the largest known structure in the universe and provides a powerful laboratory for testing cosmological models. Observational techniques like weak gravitational lensing, particularly cosmic shear, offer direct probes of the total mass distribution, including dark matter. Complementary approaches involve analyzing the distribution of baryonic matter (like galaxies and galaxy clusters) and individual stars to infer the underlying dark matter halo structure, or through surveys of galaxy clusters which serve as the most massive bound systems in the Cosmic Web and are highly sensitive to cosmological parameters.

My research significantly contributes to unraveling the mysteries of dark matter and the cosmic web. I have developed and applied advanced techniques to constrain cosmological models and characterize the universe's large-scale structure. For instance, my work has involved using cosmic shear analysis, particularly a k-cut approach with Hyper Suprime-Cam (HSC) data, to test and constrain modified gravity theories like f(R) gravity, providing crucial insights into the nature of gravity on cosmological scales and the potential for deviations from General Relativity.

Furthermore, I have employed novel analytical methods to dissect the intricate structure of the dark matter web. This includes developing "multistream views" to understand the topology, geometry, and caustic design of dark matter haloes and the cosmic web itself, offering a detailed portrait of these fundamental cosmic structures. My work also extends to utilizing large photometric samples, such as 2.6 million Red Clump stars, to map the dark matter distribution within the Milky Way, and leveraging extended cluster surveys like SPTpol to probe the most massive structures and trace the cosmic web. These diverse approaches enhance our understanding of dark matter's role in the formation and evolution of the universe.

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
