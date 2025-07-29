---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter constitutes roughly 85% of the universe's matter content and plays a pivotal role in the formation and evolution of cosmic structures. While it does not interact electromagnetically, its gravitational influence is paramount, driving the formation of the Cosmic Web – a vast, intricate network of filaments, sheets, and voids that permeates the universe. This large-scale structure provides the scaffolding for galaxies and galaxy clusters, making its detailed understanding crucial for comprehending cosmic evolution. Numerical simulations, particularly N-body simulations, are the primary tools for modeling the gravitational collapse of dark matter, yet interpreting the complex dynamics within these structures requires sophisticated theoretical frameworks.

Traditional approaches often treat dark matter as a single, collisionless fluid. However, as structures collapse and merge, dark matter particles decouple and cross orbits, leading to a multi-valued velocity field where multiple streams of particles can coexist at a single spatial point. Understanding this multi-stream nature is key to accurately characterizing the internal dynamics, density profiles, and substructure of the Cosmic Web, including the dense dark matter haloes where galaxies reside. Unraveling the intricate geometry and topology of this web, and identifying specific features like caustics – singular regions where streams converge – offers deeper insights into the highly non-linear process of gravitational structure formation.

My research systematically investigates the intricate architecture of the Cosmic Web, moving beyond simplified fluid approximations by embracing a "multistream view" of dark matter dynamics. I have developed novel methodologies to characterize the multiple velocity components inherent in the non-linear phases of gravitational collapse. Specifically, my work, including "The Caustic Design of the Dark Matter Web," focuses on identifying and analyzing caustics, which are fundamental singularities arising from the folding of phase space during structure formation. This approach allows for a precise mapping of the high-density, multi-stream regions that define the skeletal framework of the dark matter web.

Building on this, my contributions in "Multi-stream portrait of the Cosmic web" and "Topology and geometry of the dark matter web: a multistream view" extend this perspective to provide a comprehensive characterization of the web's structural elements. By analyzing the multi-stream nature, I have offered new insights into the connectivity and spatial distribution of filaments, sheets, and voids, revealing how the complex interplay of streams dictates the web's topology. Furthermore, my research on "Dark matter haloes: a multistream view" applies this sophisticated framework to the densest knots of the Cosmic Web, demonstrating how the multistream nature shapes their internal structure, density profiles, and substructure. This work provides a more accurate theoretical description of the dark matter distribution, enhancing our interpretation of cosmological simulations and guiding future efforts to probe the nature of dark matter.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/multi-stream-portrait-of-the-cosmic-web_plot_1_6096c149.png" alt="Figure from Multi-stream portrait of the Cosmic web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-stream portrait of the Cosmic web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from Topology and geometry of the dark matter web: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Topology and geometry of the dark matter web: a multistream view</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
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
