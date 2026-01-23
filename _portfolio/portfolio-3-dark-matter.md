---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The existence of dark matter is a fundamental mystery in modern cosmology, profoundly influencing the formation and evolution of structures in the universe. While unseen, its gravitational effects are evident across cosmic scales, from galaxy rotation curves to the large-scale distribution of matter. The standard cosmological model, Lambda-CDM, posits that dark matter constitutes roughly 27% of the universe's mass-energy budget, providing the gravitational scaffolding for galaxies and galaxy clusters. Understanding its nature and interactions remains a central goal in astrophysics.

Research in this domain spans theoretical predictions, advanced numerical simulations, and sophisticated observational techniques. Cosmologists aim to precisely map the cosmic web – the filamentary network of dark matter and gas – and characterize the dark matter halos hosting galaxies. Efforts also focus on testing the Lambda-CDM model's validity and exploring alternative gravity theories. These investigations utilize diverse observational probes, including weak gravitational lensing, stellar population surveys, and mapping galaxy and galaxy cluster distributions.

My work significantly contributes to probing dark matter and constraining cosmological models. I have investigated the intricate dynamics of the dark matter web, characterizing its "caustic design" and "multistream portrait" to reveal complex topological and geometrical properties, offering novel insights into hierarchical structure formation. I've also been involved in modeling galaxy formation in cosmological simulations with CRK-HACC, bridging theory and observation. A key contribution involves constraining alternative theories like $f(R)$ gravity using a $k$-cut cosmic shear analysis on Hyper Suprime-Cam data.

My research further leverages extensive observational datasets, including photometric samples of millions of Red Clump stars, spectroscopic analysis of Carbon-Enhanced Metal-Poor stars from Gaia DR3, and weak lensing cluster mass estimation from surveys like SPTpol, while contributing to future missions like SPHEREx. Through these diverse projects, my work provides a comprehensive, multi-faceted approach, offering a refined picture of structure formation, tightening constraints on fundamental cosmological parameters and alternative gravity theories, and enhancing the precision of cosmological measurements. Ultimately, this advances our understanding of the universe's dark components and its grand evolutionary history.

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
