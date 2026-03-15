---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe's large-scale structure, from galaxy clusters to vast cosmic voids, is primarily sculpted by the invisible influence of dark matter. Constituting approximately 27% of the universe's energy density, dark matter's precise nature remains one of the most significant mysteries in modern astrophysics and cosmology. Its gravitational effects are crucial for the formation and evolution of galaxies and the intricate network known as the Cosmic Web. Understanding dark matter's distribution, dynamics, and interaction with baryonic matter is paramount to developing a complete picture of cosmic evolution.

Cosmologists employ a combination of observational data from telescopes and sophisticated N-body simulations to probe dark matter and the Cosmic Web. These investigations aim to test and refine the standard Lambda-CDM model, which describes a universe dominated by dark energy and cold dark matter, and to explore alternative cosmological models, such as modified theories of gravity like f(R) gravity. Techniques like cosmic shear analysis, cluster surveys, and the detailed study of dark matter halo properties provide crucial constraints on these models, pushing the boundaries of our understanding of fundamental physics. The growing complexity and volume of both simulated and observed data necessitate the development of cutting-edge analytical and computational methodologies.

My research significantly contributes to this field through the development and application of advanced computational and analytical techniques. I have pioneered the use of a k-cut cosmic shear analysis to constrain f(R) gravity models using data from surveys like Hyper Suprime-Cam. My work delves into the intricate structure of dark matter, exploring the "caustic design" of the Cosmic Web and developing a "multistream view" to understand the topology and geometry of dark matter haloes and the larger Cosmic Web, offering a more granular perspective on structure formation. Furthermore, I have contributed to developing sophisticated simulation frameworks like CRK-HACC for modeling galaxy formation and have been involved in future missions such as the SPHEREx satellite, which promises to revolutionize our understanding of the universe's early history and evolution.

A core aspect of my contributions lies in leveraging artificial intelligence and machine learning to address complex cosmological challenges. I have developed auxiliary-variable-guided generative models to uncover the physical drivers of dark matter halo structures and have benchmarked AI-evolved cosmological structure formation, pushing the capabilities of predictive simulations. My work includes "Differentiable Predictions for Large Scale Structure with SHAMNet," a novel approach for combining machine learning with physically motivated models, and physical benchmarking for AI-generated Cosmic Web simulations for accuracy. These innovative techniques not only provide new avenues for modeling the Cosmic Web but also offer robust physical benchmarks for assessing the fidelity of AI-generated cosmological data, ultimately enhancing our ability to trace the Cosmic Web and extract cosmological parameters from extensive surveys like the SPTpol Extended Cluster Survey.

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
