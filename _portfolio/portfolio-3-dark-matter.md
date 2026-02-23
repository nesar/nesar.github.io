---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Cosmology seeks to understand the origin, evolution, and composition of the universe, with dark matter being a pivotal component, constituting approximately 27% of its energy density. This enigmatic substance, undetectable by light, profoundly influences the formation and dynamics of galaxies and the large-scale cosmic web – a vast network of filaments, walls, and voids where galaxies reside. Unraveling dark matter's properties is central to understanding structure formation.

Researchers explore dark matter's distribution, substructure, and interactions through N-body simulations, which model its gravitational evolution, and large-scale observational surveys that map galaxies and clusters. These studies characterize dark matter halos, where galaxies form, and the cosmic web's intricate topology. Beyond dark matter, modern cosmology also tests fundamental laws of gravity, comparing General Relativity with alternative theories using precise measurements like cosmic shear and galaxy cluster statistics. The advent of massive astronomical datasets necessitates advanced data analysis techniques, including artificial intelligence and machine learning, to extract subtle cosmological signals and identify rare astrophysical objects, pushing the boundaries of discovery.

My research significantly contributes to these areas, particularly in understanding dark matter and the cosmic web. I have extensively explored the fundamental nature of dark matter structures, developing sophisticated multi-stream models to analyze the kinematics and substructure within dark matter halos and the cosmic web. This includes investigating the caustic design of the dark matter web, analyzing the topology and geometry of these multi-stream features, and precisely tracing the filaments and voids that define the large-scale structure. This work offers crucial insights into how dark matter aggregates and influences galaxy formation.

Furthermore, I have applied these insights to broader cosmological questions. My work includes constraining alternative gravity theories like $f(R)$ gravity using k-cut cosmic shear analysis of Hyper Suprime-Cam data, and modeling galaxy formation in cosmological simulations with CRK-HACC. I have also leveraged large observational datasets, from photometric samples of Milky Way Red Clump Stars to the SPTpol Extended Cluster Survey, and explored AI/ML opportunities for collaborations like the Rubin LSST Dark Energy Science Collaboration. Additionally, I contribute to mission development for the SPHEREx Satellite Mission and identify unique stellar populations, such as Carbon-Enhanced Metal-Poor stars from $Gaia$ DR3 spectra, which provide crucial empirical data for galactic evolution and dark matter studies.

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
