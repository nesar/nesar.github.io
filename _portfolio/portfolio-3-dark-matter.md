---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The field of dark matter and cosmology seeks to unravel the fundamental constituents and evolutionary history of the universe. A significant portion of the universe's matter content is hypothesized to be dark matter, an enigmatic substance that interacts gravitationally but not electromagnetically, playing a crucial role in the formation of cosmic structures. Understanding its properties is paramount to completing our standard model of cosmology. Concurrently, the study of large-scale structure – the intricate web of galaxies, clusters, and voids – provides a powerful probe into the universe's expansion history, the nature of dark energy, and the validity of general relativity on cosmological scales.

Key challenges include precisely characterizing dark matter's distribution, especially within galactic halos and across the cosmic web, and distinguishing its gravitational effects from potential modifications to general relativity. Researchers employ a variety of advanced techniques, from sophisticated N-body and hydrodynamic simulations that model the evolution of matter and galaxies, to cutting-edge observational surveys utilizing telescopes and satellite missions. These efforts aim to confront theoretical predictions with empirical data, pushing the boundaries of our understanding of cosmic origins and evolution, and ultimately addressing the profound questions surrounding the universe's ultimate fate.

My research critically advances our understanding of dark matter and its imprint on cosmic structures. I have explored the fine-grained distribution of dark matter through novel "multistream" analyses, revealing the complex internal dynamics and "caustic design" within dark matter halos and the overarching cosmic web. This work includes detailed investigations into the "topology and geometry" of these structures, moving beyond simplified models to more accurately "trace the cosmic web." Furthermore, I have contributed to constraining alternative theories of gravity, specifically $f(R)$ gravity, by applying advanced methods like "k-cut cosmic shear analysis" to Hyper Suprime-Cam data. My work also extends to developing sophisticated simulation techniques, including "Modeling Galaxy Formation in Cosmological Simulations with CRK-HACC," and leveraging machine learning approaches, exemplified by "Differentiable Predictions for Large Scale Structure with SHAMNet," to enhance cosmological model predictions.

In addition to theoretical and methodological developments, I have engaged directly with groundbreaking observational efforts. This includes involvement with the "SPHEREx Satellite Mission," which promises unprecedented spectroscopic mapping of the sky, and analysis of data from the "SPTpol Extended Cluster Survey," providing crucial insights into galaxy cluster properties and cosmology. My research also delves into galactic archaeology and structure, using stellar populations like "Red Clump Stars" to map the "Inner to Outer Milky Way" and identifying "Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in Gaia DR3" to constrain early galaxy formation processes. These diverse contributions, spanning fundamental dark matter theory, alternative gravity models, advanced simulation techniques, and the analysis of cutting-edge astronomical data, collectively aim to refine our cosmological models, enhance our ability to interpret complex observational datasets, and ultimately illuminate the nature of dark matter and the universe's cosmic evolution.

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
