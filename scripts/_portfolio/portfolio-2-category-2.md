---
title: "Cosmological Constraints from Cluster Abundance"
excerpt: "Research in cosmological constraints from cluster abundance"
collection: portfolio
---

Galaxy clusters, the largest gravitationally bound structures in the Universe, serve as powerful cosmological probes. Their formation and evolution are highly sensitive to the underlying cosmological model, particularly the matter density parameter (Ωm) and the amplitude of matter fluctuations (σ8). By studying the abundance of these massive structures as a function of redshift and mass, cosmologists can derive robust constraints on fundamental cosmological parameters. This method complements other cosmological probes, such as the Cosmic Microwave Background (CMB) and Baryon Acoustic Oscillations (BAO), providing crucial independent checks and helping to address potential tensions in the standard ΛCDM model.

Large-area, high-sensitivity surveys at millimeter wavelengths, like the South Pole Telescope (SPT-SZ) and the Atacama Cosmology Telescope (ACT), are instrumental in detecting galaxy clusters through the Sunyaev-Zel'dovich (SZ) effect. This effect, a distortion of the CMB spectrum caused by inverse Compton scattering of CMB photons off hot electrons in cluster gas, provides a nearly mass-limited and redshift-independent selection of clusters. Accurate characterization of cluster catalogs, including precise mass calibration and selection functions, is paramount for translating observed cluster counts into robust cosmological constraints.

My research has significantly contributed to refining cosmological constraints through the analysis of galaxy cluster abundance. In one key study, I focused on the "Cosmological Constraints from the Cluster Redshift Distribution in the 2500 deg2 SPT-SZ Survey." For this work, I utilized the extensive SPT-SZ cluster catalog, leveraging the cluster redshift distribution to constrain cosmological parameters. This involved carefully modeling the observed cluster counts as a function of redshift and SZ signal, accounting for the survey's selection function and the underlying mass-observable relation. The derived constraints, primarily on σ8 and Ωm, demonstrated the remarkable power of SZ-selected cluster samples in independently probing the late-time Universe and providing measurements competitive with other leading probes.

Furthermore, my work extended to "The ACT DR4 Cluster Catalog: A Measurement of σ₈ with the Cluster Mass Function." Here, I developed and applied sophisticated methodologies to analyze the ACT DR4 cluster catalog, employing the cluster mass function to specifically measure σ8. This involved meticulous calibration of the cluster masses using multi-wavelength data and robust statistical techniques to infer cosmological parameters from the observed mass function. The precision achieved in these measurements underscores the vital role of millimeter-wave surveys in advancing our understanding of structure formation and the universe's expansion history. My contributions have helped to solidify the agreement between cluster-derived cosmological parameters and those from other probes, providing critical independent data points for ongoing efforts to resolve potential discrepancies, such as the intriguing σ8 tension.

<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>

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
