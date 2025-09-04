---
title: "Galaxy Cluster Cosmology and Surveys"
excerpt: "Research in galaxy cluster cosmology and surveys"
collection: portfolio
---

Galaxy clusters, as the most massive gravitationally bound structures in the universe, serve as paramount probes for deciphering cosmic evolution and the fundamental parameters that govern our cosmos. Their formation and growth are exquisitely sensitive to the nature of dark energy, the distribution of dark matter, and the masses of neutrinos. Consequently, studying their abundance, spatial distribution, and intrinsic properties across cosmic time provides stringent tests for cosmological models, including the standard Lambda-CDM paradigm.

Modern astronomy employs large-scale surveys across various wavelengths to detect and characterize these elusive structures. Among the most powerful techniques is the detection of the Sunyaev-Zel'dovich (SZ) effect, a subtle distortion of the Cosmic Microwave Background (CMB) radiation caused by inverse Compton scattering of CMB photons off the hot electron gas within galaxy clusters. SZ surveys, such as those conducted by the South Pole Telescope (SPT), offer a unique advantage due to the nearly redshift-independent nature of the SZ signal, enabling the discovery of clusters out to very high redshifts, which is crucial for tracking their evolution.

My research significantly contributes to this field, particularly through my involvement in "The SPTpol Extended Cluster Survey." In this work, I have focused on leveraging the advanced capabilities of the SPTpol instrument to identify and characterize a new, expanded sample of galaxy clusters. This involved developing and refining sophisticated data analysis pipelines for extracting the subtle SZ signal from CMB maps, meticulously identifying cluster candidates, and determining their properties, such as SZ significance and inferred mass.

A core aspect of my contribution has been the application of robust statistical methods to compile this extended cluster catalog, which substantially increases the number of high-quality, high-redshift clusters available for cosmological studies. The methodologies employed ensure high purity and completeness, critical for minimizing systematic uncertainties in subsequent cosmological analyses. The expanded catalog resulting from "The SPTpol Extended Cluster Survey" provides an enhanced statistical sample, allowing for tighter constraints on cosmological parameters, improved understanding of cluster formation and evolution, and refined tests of fundamental physics through cluster abundance measurements.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-sptpol-extended-cluster-survey_plot_1_853c797c.png" alt="Figure from The SPTpol Extended Cluster Survey" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The SPTpol Extended Cluster Survey</div>
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
