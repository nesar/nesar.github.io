---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology <br/><img src='/images/research_dark-matter.png'>"
collection: portfolio
---

Summary: Galaxy clusters are one of the most powerful probes to study extensions of
General Relativity and the Standard Cosmological Model. Upcoming surveys like
the Vera Rubin Observatory's Legacy Survey of Space and Time are expected to
revolutionise the field, by enabling the analysis of cluster ...

## Research Figures

<div class="research-figures-grid">
  <div class="research-figure">
    <img src="/images/research/figures/the_caustic_design_of_the_dark_matter_web_page3_fig1_fa373b8f.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)">
    <p class="figure-caption">From: The Caustic Design of the Dark Matter Web</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/the_caustic_design_of_the_dark_matter_web_page3_fig2_a3b0a1c0.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)">
    <p class="figure-caption">From: The Caustic Design of the Dark Matter Web</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/the_caustic_design_of_the_dark_matter_web_page5_fig1_602e5f0d.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)">
    <p class="figure-caption">From: The Caustic Design of the Dark Matter Web</p>
  </div>
  <div class="research-figure">
    <img src="/images/research/figures/the_caustic_design_of_the_dark_matter_web_page7_fig1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)">
    <p class="figure-caption">From: The Caustic Design of the Dark Matter Web</p>
  </div>
</div>

<style>
.research-figures-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.research-figure {
  text-align: center;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  transition: transform 0.2s ease;
}

.research-figure:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.research-figure img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.research-figure img:hover {
  opacity: 0.9;
}

.figure-caption {
  font-size: 0.85em;
  color: #6c757d;
  margin-top: 0.5rem;
  line-height: 1.3;
}

/* Modal styles */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  padding-top: 5%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}
</style>

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

// Close modal when clicking outside the image
window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}
</script>

## Related Publications (11 papers):

- **Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing
  Cluster Mass Estimation** (2024) - Preprint
- **Carbon-enhanced metal-poor star candidates from BP/RP spectra in Gaia DR3** (2023) - Monthly Notices of the Royal Astronomical Society
- **Over 2.7 Million Carbon-Enhanced Metal-Poor stars from BP/RP Spectra in $ Gaia $ DR3** (2022) - arXiv e-prints
- **Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies** (2020) - Phys. Rev. D 103, 123525 (2020)
- **The Caustic Design of the Dark Matter Web** (2019) - arXiv preprint arXiv:1906.05920
- **Topology, Geometry and Morphology of the Dark Matter Web** (2018) - Preprint
- **Tracing the cosmic web** (2018) - Monthly Notices of the Royal Astronomical Society
- **Dark matter haloes: a multistream view** (2017) - Monthly Notices of the Royal Astronomical Society
- **Topology and geometry of the dark matter web: a multistream view** (2017) - Monthly Notices of the Royal Astronomical Society
- **Topology and geometry of the dark matter web** (2017) - APS April Meeting Abstracts