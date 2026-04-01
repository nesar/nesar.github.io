---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The study of Dark Matter and Cosmology seeks to unravel the fundamental constituents and evolutionary history of our universe. A significant portion of the universe's mass is attributed to dark matter, an enigmatic substance detectable only through its gravitational influence, yet its precise nature remains one of the greatest challenges in modern astrophysics. Research in this field aims to understand how dark matter shapes the large-scale structure of the cosmos, from the formation of galaxies and galaxy clusters to the intricate network known as the cosmic web, and to test the standard cosmological model ($\Lambda$CDM) against various observational probes.

Key areas of investigation include mapping the distribution of dark matter through gravitational lensing, analyzing the properties and formation of dark matter halos—the gravitational "cradles" in which galaxies form—and exploring alternative theories of gravity that could modify our understanding of cosmic acceleration and structure formation. These endeavors rely heavily on sophisticated cosmological simulations, which model the gravitational evolution of matter, and on cutting-edge observational surveys that provide vast datasets across the electromagnetic spectrum, from ground-based telescopes to space missions. The integration of advanced computational techniques, including machine learning and AI, is increasingly vital for processing complex data and extracting physical insights from these simulations and observations.

My research significantly contributes to these frontiers by combining theoretical advancements with advanced computational and observational techniques. I have extensively studied the dark matter cosmic web and its substructures, using multi-stream analysis to reveal the intricate caustic designs and underlying topology and geometry of halos, thereby providing a more detailed "portrait" of the universe's filamentary structure. This work includes tracing the cosmic web and physically benchmarking AI-generated models to ensure their accuracy in representing large-scale structure formation.

I have also focused on the formation and evolution of dark matter halos and their role in galaxy formation. My work involves developing and utilizing advanced simulation codes like CRK-HACC to model galaxy formation and pioneering the use of auxiliary-variable-guided generative models to uncover the physical drivers behind dark matter halo structures. Furthermore, I apply rigorous statistical methods, such as k-cut cosmic shear analysis on Hyper Suprime-Cam data, to constrain modified gravity theories like $f(R)$ gravity, directly testing fundamental cosmological paradigms.

My contributions extend to leveraging diverse observational datasets to provide crucial constraints and context for cosmological models. This includes detailed photometric analysis of millions of Red Clump stars across the Milky Way from Gaia DR3 to understand Galactic structure, identifying Carbon-Enhanced Metal-Poor star candidates from Gaia spectra as probes of early universe stellar populations, and participating in large-scale surveys such as the SPTpol Extended Cluster Survey and the SPHEREx satellite mission, which aim to map cosmic structures and probe the universe's expansion history. Through these efforts, I strive to push the boundaries of our understanding of dark matter, the cosmic web, and the fundamental laws governing our universe.

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
