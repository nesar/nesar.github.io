---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Cosmology seeks to understand the origin, evolution, and large-scale structure of the universe, with dark matter playing a pivotal, yet elusive, role. Approximately 85% of the universe's matter content is dark matter, an invisible substance whose gravitational influence is essential for explaining the formation and dynamics of galaxies and the vast cosmic web. Key research in this field involves probing the nature of dark matter, mapping its distribution, and understanding how it shapes the universe's structure over cosmic time. This endeavor often necessitates the development of sophisticated theoretical models and high-resolution computational simulations to predict observable phenomena.

Investigators in dark matter and cosmology also leverage vast amounts of observational data from ground-based telescopes and space missions. These surveys capture light from distant galaxies, cosmic microwave background radiation, and individual stars, providing crucial insights into the universe's expansion history, the distribution of matter, and the properties of exotic objects. Advanced statistical and data analysis techniques are essential for extracting cosmological constraints from these complex datasets, allowing for rigorous testing of fundamental physics, including general relativity and alternative theories of gravity. This synergistic approach, combining theory, simulation, and observation, is vital for unraveling the universe's profound mysteries.

My research significantly contributes to this field by developing and applying advanced computational and analytical tools to understand dark matter and cosmic structure formation. I have focused on modeling galaxy formation within cosmological simulations, notably utilizing frameworks like CRK-HACC, and benchmarking novel techniques such as AI-evolved cosmological structure formation to ensure their physical validity. A critical aspect of my work involves employing multi-stream and caustic analyses to explore the intricate internal dynamics and topology of dark matter structures, providing a detailed portrait of the cosmic web's substructure, which is crucial for understanding its observational signatures and impact on galaxy evolution.

Complementing my simulation work, I have extensively engaged with observational data from major astronomical surveys. For instance, I developed methodologies for constraining modified gravity theories, such as $f(R)$ gravity, using a $k$-cut cosmic shear analysis applied to data from the Hyper Suprime-Cam. My work also includes leveraging large datasets from missions like $Gaia$ to identify unique stellar populations, such as Carbon-Enhanced Metal-Poor (CEMP) star candidates and a photometric sample of 2.6 million Red Clump stars, which serve as ancient tracers of early galaxy formation and galactic structure. Additionally, I have contributed to characterizing distant galaxy clusters through surveys like SPTpol and am involved with future missions such as SPHEREx, ensuring that advanced data analysis techniques are prepared to extract maximal cosmological information. This comprehensive approach, spanning theoretical modeling, high-resolution simulations, and detailed observational data analysis, aims to advance our understanding of dark matter, gravity, and the universe's evolutionary history.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/modeling-galaxy-formation-in-cosmological-simulati_plot_1_8c54e222.png" alt="Figure from Modeling Galaxy Formation in Cosmological Simulations with CRK-HACC" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Modeling Galaxy Formation in Cosmological Simulations with CRK-HACC</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-spherex-satellite-mission_plot_1_630d5d67.png" alt="Figure from The SPHEREx Satellite Mission" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The SPHEREx Satellite Mission</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/carbon-enhanced-metal-poor-star-candidates-from-bp_plot_1_17c64dee.png" alt="Figure from Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3</div>
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
