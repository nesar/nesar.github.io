---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe on its largest scales is dominated by dark matter, an enigmatic substance that does not interact with light but exerts gravitational influence crucial for the formation of cosmic structures. The standard cosmological model, Lambda-CDM, posits that dark matter constitutes approximately 27% of the universe's energy density, providing the gravitational scaffolding upon which galaxies and galaxy clusters form. Understanding the nature of dark matter and its intricate role in cosmic evolution remains one of the foremost challenges in modern astrophysics.

Observations and simulations reveal that dark matter organizes into a vast, interconnected network known as the Cosmic Web, comprising dense galaxy clusters, filamentary structures, sheet-like walls, and expansive voids. Probing this cosmic architecture is essential for testing cosmological models, constraining the properties of dark matter, and investigating potential deviations from General Relativity, such as alternative theories of gravity like $f(R)$ gravity. Precision cosmology relies on sophisticated analytical and computational techniques, often leveraging large-scale astronomical surveys and advanced statistical methods to decipher the universe's fundamental constituents and evolutionary pathways.

My research extensively explores the fundamental properties and dynamics of dark matter, focusing on the formation and evolution of dark matter halos and the Cosmic Web. I have developed and applied novel techniques, such as the "multistream view," to characterize the complex internal structures and kinematics within dark matter halos and the surrounding Cosmic Web. This approach, detailed in papers like "Dark matter haloes: a multistream view" and "Topology and geometry of the dark matter web: a multistream view," provides a deeper understanding of the hierarchical assembly of structures and the intricate "caustic design" that governs the density and velocity fields within these systems, as explored in "The Caustic Design of the Dark Matter Web" and "Multi-stream portrait of the Cosmic web." My work on "Tracing the cosmic web" further contributes to mapping and analyzing these large-scale structures.

Beyond understanding dark matter's standard behavior, I have also engaged in constraining alternative gravitational theories. For instance, my work on "Constraining $f(R)$ Gravity with a $k$-cut Cosmic Shear Analysis of the Hyper Suprime-Cam First-Year Data" demonstrates the application of cutting-edge weak lensing techniques to observational data, providing robust constraints on modified gravity models. Furthermore, I contribute to unraveling the complex interplay between dark matter and baryonic matter, using advanced computational tools like CRK-HACC for "Modeling Galaxy Formation in Cosmological Simulations." My research also incorporates machine learning, as seen in "Uncovering Physical Drivers of Dark Matter Halo Structures with Auxiliary-Variable-Guided Generative Models," to predict and understand halo properties, and applies "Optimised Galaxy Selection" to reduce model error in weak lensing cluster mass estimation. My involvement in missions like SPHEREx and surveys such as SPTpol highlights my commitment to leveraging future observational data.

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
