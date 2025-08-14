---
title: "Large-Scale Structure & Galaxy Clusters"
excerpt: "Research in large-scale structure & galaxy clusters"
collection: portfolio
---

The large-scale structure (LSS) of the universe, encompassing the cosmic web of galaxies, clusters, and voids, is a fundamental pillar of modern cosmology. Its study provides critical insights into the formation and evolution of the universe, serving as a powerful probe for testing cosmological models, including the nature of dark matter and dark energy, and the initial conditions of the Big Bang. Galaxy clusters, as the most massive gravitationally bound structures in the universe, occupy the nodes of this cosmic web and are exceptional laboratories for studying structure formation.

Observing and characterizing galaxy clusters across cosmic time allows scientists to trace the growth of cosmic structure. Various observational techniques are employed for cluster detection, including X-ray emission from the hot intracluster medium, optical detection of galaxy overdensities, and the Sunyaev-Zel'dovich (SZ) effect. The SZ effect, a distortion of the cosmic microwave background (CMB) spectrum as CMB photons inverse-Compton scatter off hot electrons in the cluster gas, offers a uniquely mass-selected and redshift-independent way to find clusters, making it an invaluable tool for building large, homogeneous cluster catalogs.

My work has centered on leveraging cosmic microwave background observations, specifically using data from the South Pole Telescope (SPTpol), to conduct large-scale surveys of galaxy clusters. I have played a significant role in developing and applying advanced analysis techniques to Sunyaev-Zel'dovich (SZ) effect data to identify and characterize these massive structures. My contributions to the SPTpol Extended Cluster Survey were pivotal in expanding the catalog of SZ-selected clusters, providing a larger and more statistically powerful sample.

This involved refining the methodologies for cluster detection, meticulously validating cluster candidates, and accurately characterizing their properties, such as SZ signal strength and redshift distribution. The technical contributions ensured the robustness and purity of the resulting cluster catalog. This comprehensive work is crucial for enabling stringent cosmological analyses, including constraints on parameters like the amplitude of matter fluctuations (sigma_8) and the dark energy equation of state, as well as providing insights into the mass function and evolutionary properties of galaxy clusters. The derived cluster samples also serve as a foundation for multi-wavelength follow-up observations, further enhancing our understanding of these cosmic behemoths.

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
