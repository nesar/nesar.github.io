---
title: "Other Research"
excerpt: "Research in other research <br/><img src='/images/research_other-research.png'>"
collection: portfolio
---

Additional research projects including computational methods, data analysis techniques, and interdisciplinary applications.

## Research Figures

<div class="research-figures-grid">
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

## Related Publications:

- **GAN-based Event-level Inverse Mapper (GEIM)-An Application on Quantum Chromodynamics Global Analysis** (2025) - Preprint
- **Learning Relationships Between Disparate Representations of Objects with Transformers and Contrastive Losses** (2024) - Authorea Preprints
- **2023 AI Testbed Expeditions Report** (2023) - Preprint
- **VizieR Online Data Catalog: CEMP in Gaia DR3 (Lucey+, 2023)** (2023) - VizieR Online Data Catalog
- **Carbon-enhanced metal-poor star candidates from BP/RP spectra in Gaia DR3** (2023) - Monthly Notices of the Royal Astronomical Society
- **Differentiable Predictions for Large Scale Structure with SHAMNet** (2022) - The Open Journal of Astrophysics
- **Over 2.7 Million Carbon-Enhanced Metal-Poor stars from BP/RP Spectra in $ Gaia $ DR3** (2022) - arXiv e-prints
- **Constraining  gravity with a -cut cosmic shear analysis of the Hyper Suprime-Cam first-year data** (2021) - Physical Review D
- **VizieR Online Data Catalog: The SPTpol Extended Cluster Survey (Bleem+, 2020)** (2020) - VizieR Online Data Catalog
- **The SPTPoL extended cluster survey** (2020) - The Astrophysical Journal Supplement Series
- **From the Inner to Outer Milky Way: A Pristine Sample of 4.3 Million Red Clump Stars** (2020) - arXiv
- **VizieR Online Data Catalog: Photometric sample of 2.6 million red clump stars (Lucey+, 2020)** (2020) - VizieR Online Data Catalog
- **From the inner to outer Milky Way: a photometric sample of 2.6 million red clump stars** (2020) - Monthly Notices of the Royal Astronomical Society
