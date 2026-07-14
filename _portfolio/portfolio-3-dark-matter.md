---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark Matter, constituting approximately 27% of the Universe's mass-energy budget, is a central mystery in modern cosmology, dictating the formation and evolution of large-scale structures. Within the standard Lambda-CDM model, dark matter gravitationally collapses into a complex network—the cosmic web—comprising massive halos hosting galaxies, interconnected by vast filaments, and punctuated by underdense voids. Investigating dark matter's properties and its influence on the cosmic web offers crucial insights into the Universe's fundamental constituents, its expansion history, and the formation of all visible structures.

Progress in this field relies on a multi-pronged approach combining theoretical predictions, sophisticated numerical simulations, and increasingly precise observational data. Cosmological N-body and hydrodynamical simulations are indispensable tools, enabling researchers to model the non-linear evolution of dark matter and baryonic matter. Simultaneously, cutting-edge astronomical surveys, employing techniques like weak gravitational lensing, cosmic shear, and galaxy cluster detection, provide empirical evidence to test cosmological models and constrain alternative gravity theories. Advanced statistical and machine learning methodologies are increasingly integrated to extract information and make robust predictions from these complex datasets.

My research significantly contributes to deciphering the intricate architecture of the dark matter cosmic web and its constituent halos. I have pioneered a "multistream view" to meticulously analyze the internal dynamics and substructure of dark matter halos and the broader cosmic web, as highlighted in works like "Dark matter haloes: a multistream view" and "Topology and geometry of the dark matter web: a multistream view." This approach, complemented by investigations into the "caustic design" of the cosmic web, provides a deeper understanding of its topological and geometric properties. Concurrently, I have contributed to advanced simulation capabilities, such as "Modeling Galaxy Formation in Cosmological Simulations with CRK-HACC," to accurately model the interplay between dark matter and baryonic processes, crucial for understanding galaxy formation within these environments.

A key focus of my recent work involves leveraging artificial intelligence and machine learning to accelerate and enhance cosmological research. I have developed innovative "auxiliary-variable-guided generative models" to uncover physical drivers of dark matter halo structures, and introduced "differentiable predictions for large scale structure with SHAMNet," enabling more efficient parameter inference. Rigorous "benchmarking AI-evolved cosmological structure formation" and "physical benchmarking for AI-generated cosmic web" are integral to validating these novel methods. Furthermore, I apply these sophisticated tools to observational cosmology, utilizing data from projects such as Hyper Suprime-Cam and SPTpol. My work includes employing "k-cut cosmic shear analysis" to "constrain f(R) gravity" theories and developing "optimised galaxy selection" techniques to reduce model error in "weak lensing cluster mass estimation," thereby refining cosmological parameters and alternative gravity models.

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
