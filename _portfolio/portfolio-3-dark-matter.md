---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The study of dark matter and cosmology addresses fundamental questions about the universe's composition, evolution, and large-scale structure. Observations reveal that most of the universe's matter content is an enigmatic, non-luminous substance called dark matter, which dictates the formation and distribution of galaxies and galaxy clusters. Furthermore, the accelerated expansion of the universe points to the existence of dark energy, while deviations from General Relativity may also play a role in cosmic dynamics. Research in this domain bridges theoretical physics, numerical simulations, and cutting-edge astronomical observations to probe the nature of dark matter, test cosmological models, and unveil the processes that shape the cosmic web.

Understanding these cosmic phenomena requires sophisticated computational tools and extensive observational surveys. Cosmological simulations are crucial for modeling the gravitational collapse of dark matter, the formation of haloes, and the intricate structure of the cosmic web. Concurrently, large-scale surveys, utilizing techniques like cosmic shear, weak lensing, and stellar photometry/spectroscopy, provide the empirical data necessary to constrain theoretical models, map the distribution of matter, and identify rare objects that offer unique insights into galactic and extragalactic evolution. A key challenge lies in developing robust methodologies to extract cosmological information from these complex datasets and rigorously test competing theories of gravity and dark matter.

My research has significantly contributed to understanding the fundamental nature and distribution of dark matter and its role in shaping the cosmos. I have developed and applied advanced cosmological simulations, such as CRK-HACC, to model galaxy formation and the intricate structure of dark matter haloes and the cosmic web. A core focus has been to characterize these structures using novel methods, including a "multistream view" that reveals the fine-grained substructure of dark matter haloes and the Cosmic Web's filamentary and sheet-like architecture. Furthermore, I explored the "caustic design" of the dark matter web and utilized sophisticated topological and geometrical analyses to quantify its properties, providing deeper insights into the gravitational dynamics that underpin the large-scale structure. I also pioneered the use of auxiliary-variable-guided generative models to uncover the physical drivers behind dark matter halo structures, leveraging machine learning to enhance our understanding of these crucial cosmic building blocks.

Beyond simulations, my work involves rigorous observational data analysis to test cosmological models and search for exotic phenomena. I have utilized "k-cut cosmic shear analysis" of Hyper Suprime-Cam (HSC) data to place strong constraints on alternative theories of gravity, specifically $f(R)$ models. My work has also mapped the Milky Way's structure using a photometric sample of 2.6 million Red Clump stars and identified Carbon-Enhanced Metal-Poor (CEMP) star candidates from Gaia DR3 BP/RP spectra, crucial for understanding early universe stellar populations. These observational efforts, often integrated with major missions like SPHEREx and SPTpol, complement my simulation-based research. My contributions thus span theoretical modeling, advanced numerical simulations, and detailed observational analyses, providing a comprehensive approach to addressing key questions in dark matter and cosmology.

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
