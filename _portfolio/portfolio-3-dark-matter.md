---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The field of cosmology seeks to understand the origin, evolution, and large-scale structure of the universe. A cornerstone of modern cosmology is the Lambda-CDM model, which posits a universe dominated by dark energy and cold dark matter. While this model has successfully explained a wide range of observations, the fundamental nature of dark matter and dark energy remains one of the most significant unsolved puzzles in physics. Investigating these cosmic components requires a multi-pronged approach, combining theoretical modeling, high-resolution cosmological simulations, and precise observational data from sky surveys.

A key avenue for probing dark matter and modified gravity theories lies in studying the formation and evolution of large-scale structure. Gravitational collapse of initial density fluctuations leads to the intricate "cosmic web," a network of filaments, walls, and voids that hosts galaxies and galaxy clusters. Within this web, dark matter halos form as dense concentrations of dark matter, serving as the gravitational scaffolding for galaxy formation. Understanding the substructure, phase-space dynamics, and topological properties of these halos and the broader cosmic web provides crucial tests for fundamental physics models, including deviations from General Relativity or alternative dark matter candidates.

My research significantly contributes to deciphering the intricate architecture and physical drivers of dark matter structures. I have extensively utilized multi-stream analysis and caustic design principles to characterize the dark matter web and individual halos, revealing their complex phase-space substructure and topological properties. This work, including contributions to "The Caustic Design of the Dark Matter Web," "Dark matter haloes: a multistream view," "Topology and geometry of the dark matter web: a multistream view," and "Multi-stream portrait of the Cosmic web," advances our understanding of non-linear structure formation and the dynamics of dark matter on small scales. Furthermore, I have developed innovative approaches, such as employing auxiliary-variable-guided generative models, to uncover the underlying physical drivers that dictate dark matter halo structures, pushing the boundaries of machine learning applications in astrophysics.

Beyond characterizing dark matter structures, my work also tests the foundational theories governing cosmic evolution and develops tools for next-generation cosmological investigations. I have contributed to constraining alternative gravity theories, specifically $f(R)$ gravity, using advanced statistical techniques like $k$-cut cosmic shear analysis applied to data from the Hyper Suprime-Cam First-Year survey. This directly addresses the nature of dark energy by placing limits on deviations from General Relativity. My contributions extend to the development and application of advanced cosmological simulation codes, such as CRK-HACC, for modeling complex processes like galaxy formation. Crucially, I am also involved in preparing for and analyzing data from major observational efforts, including the SPHEREx Satellite Mission and the SPTpol Extended Cluster Survey, ensuring that theoretical advancements are rigorously tested against the latest cosmic observations and that new data is maximally exploited for cosmological insights.

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
