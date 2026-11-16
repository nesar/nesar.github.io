---
title: "Dark Matter, Cosmology & Large-Scale Structure"
excerpt: "Research in dark matter, cosmology & large-scale structure"
collection: portfolio
---

The universe's large-scale structure, from the intricate network of the cosmic web to dense galaxy clusters and individual dark matter halos, provides crucial insights into the fundamental nature of cosmology and gravity. Understanding how these structures form and evolve requires a comprehensive approach, integrating advanced theoretical models, sophisticated numerical simulations, and precise observational data. A key mystery at the heart of this understanding is dark matter, the enigmatic substance believed to constitute approximately 85% of the universe's matter content, whose gravitational influence shapes the cosmic architecture. Researchers in this field aim to unravel the properties of dark matter, constrain alternative theories of gravity, and accurately model the complex processes governing structure formation.

Efforts extend to mapping the distribution of dark matter across cosmic scales, from the internal structure of halos to the vast filaments and voids of the cosmic web. This involves developing robust methods to analyze observational data from wide-field surveys and dedicated satellite missions, as well as refining cosmological simulations to capture the full dynamic range of structure formation. Furthermore, exploring the internal dynamics and substructures of dark matter halos is essential for understanding galaxy formation and evolution within these gravitational wells. The field also investigates deviations from the standard cosmological model (Lambda-CDM), such as modified theories of gravity, by testing their predictions against high-precision cosmological probes.

My research significantly contributes to these efforts by developing and applying cutting-edge methodologies to illuminate the nature of dark matter and the cosmic web. I have utilized cosmic shear analysis, specifically a k-cut approach, with data from wide-field surveys like Hyper Suprime-Cam (HSC) to place stringent constraints on modified gravity theories, such as $f(R)$ gravity. Complementary to cosmological probes, I have also mapped the Milky Way's structure using a photometric sample of 2.6 million Red Clump stars, providing a detailed view from its inner to outer regions. A major focus has been on understanding the complex topology and geometry of the dark matter web, employing a novel multi-stream view to characterize its filamentary and nodal structures, as well as the internal dynamics of dark matter haloes through their caustic design.

Beyond analytical techniques, I have advanced the use of numerical simulations and machine learning. My work includes modeling galaxy formation within cosmological simulations using codes like CRK-HACC, refining our understanding of how galaxies populate dark matter haloes. To delve deeper into halo properties, I have developed auxiliary-variable-guided generative models, a machine learning approach, to uncover the physical drivers behind diverse dark matter halo structures. Furthermore, I am actively involved in the analysis and scientific exploitation of data from leading observational initiatives, including the SPHEREx satellite mission and the SPTpol Extended Cluster Survey, applying novel methods to trace the cosmic web and extract cosmological parameters from these rich datasets. These contributions collectively advance our ability to test fundamental cosmological models and decode the universe's dark components.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
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
