---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The fields of dark matter and cosmology seek to unravel the fundamental composition and evolution of our universe. A significant portion of the cosmos remains mysterious, primarily in the form of dark matter and dark energy, which dictate the universe's large-scale structure. Understanding how the unseen dark matter orchestrates the formation of cosmic structures, from vast filaments of the cosmic web to dense dark matter halos where galaxies reside, is a central challenge. Researchers employ a combination of theoretical models, precision cosmological observations, and sophisticated numerical simulations to probe these enigmatic components and test the prevailing Lambda-CDM cosmological model or explore alternative theories of gravity.

Investigating the properties of dark matter, its distribution, and its interactions with baryonic matter is crucial for a complete picture of cosmic evolution. This involves mapping the intricate cosmic web, analyzing the internal structure of dark matter halos, and studying how galaxies populate these structures. Complementary approaches include using gravitational lensing (cosmic shear) to probe the distribution of matter directly, analyzing large catalogs of galaxies and galaxy clusters, and developing advanced computational tools to simulate the universe's evolution from the Big Bang to the present day. These efforts collectively aim to constrain cosmological parameters, test fundamental physics, and trace the universe’s history.

My research extensively explores the nature and distribution of dark matter across cosmic scales and its implications for cosmology. I have developed novel methods to characterize the intricate substructures within dark matter halos and the wider cosmic web, employing a "multi-stream view" to understand the detailed dynamics and "caustic design" of dark matter. My work delves into the "topology and geometry of the dark matter web," providing new insights into how these structures form and evolve. Furthermore, I have contributed to constraining alternative theories of gravity, such as $f(R)$ gravity, by analyzing observational data through techniques like "k-cut cosmic shear analysis" of Hyper Suprime-Cam data.

In addressing the complex interplay between dark matter and observable galaxies, I have advanced the state-of-the-art in cosmological simulations and modeling. This includes developing "CRK-HACC" for detailed "modeling of galaxy formation in cosmological simulations" and pioneering machine learning approaches like "auxiliary-variable-guided generative models" to uncover physical drivers of dark matter halo structures. I have also introduced "SHAMNet" for "differentiable predictions for large-scale structure," enhancing our ability to link theoretical models directly to observational data. My contributions extend to significant observational projects, including efforts for the "SPHEREx Satellite Mission," analyzing data from the "SPTpol Extended Cluster Survey," and characterizing the Milky Way's structure using a "photometric sample of 2.6 million Red Clump Stars." These diverse efforts collectively push the boundaries of our understanding of dark matter, gravity, and the universe’s structure.

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
