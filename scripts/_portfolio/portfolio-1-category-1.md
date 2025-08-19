---
title: "SZ-Selected Galaxy Cluster Surveys & Catalogs"
excerpt: "Research in sz-selected galaxy cluster surveys & catalogs"
collection: portfolio
---

Galaxy clusters represent the most massive gravitationally bound structures in the universe, composed of thousands of galaxies, hot intracluster gas, and a dominant dark matter halo. As such, they serve as powerful cosmological probes, tracing the growth of large-scale structure and offering critical insights into the nature of dark matter and dark energy, the fundamental constituents governing cosmic evolution. Their abundance and spatial distribution are highly sensitive to cosmological parameters, making precise and extensive cluster catalogs indispensable for modern cosmology.

A primary method for detecting galaxy clusters across a wide range of redshifts is the Sunyaev-Zel'dovich (SZ) effect. This phenomenon occurs when cosmic microwave background (CMB) photons scatter off the hot, ionized gas within galaxy clusters, leading to a measurable distortion in the CMB spectrum. The SZ effect's unique advantage lies in its redshift independence, allowing for the efficient detection of massive clusters out to very high redshifts, and its direct proportionality to the integrated pressure of the cluster gas, providing a robust proxy for cluster mass. Large-scale SZ surveys, conducted by instruments like the South Pole Telescope (SPT) and the Atacama Cosmology Telescope (ACT), have revolutionized cluster cosmology by building extensive and well-characterized catalogs.

My research has significantly contributed to the creation and characterization of leading Sunyaev-Zel'dovich selected galaxy cluster catalogs, leveraging data from both the South Pole Telescope and the Atacama Cosmology Telescope. I have been instrumental in developing and refining the sophisticated detection pipelines and analysis methodologies required to identify and characterize galaxy clusters across vast swathes of the sky. For instance, my work on the "SPTpol Extended Cluster Survey" focused on expanding the SPT cluster sample, improving our understanding of selection functions and photometric redshift estimation for these high-redshift clusters. Similarly, in the "SPT-SZ: A Sunyaev-Zel'dovich-selected Sample of Galaxy Clusters at 0.05 < z < 1.35" publication, I contributed to building and validating one of the largest and most robust SZ-selected cluster samples, enabling detailed studies of cluster properties and their evolution over cosmic time.

Furthermore, my contributions extended to "The Atacama Cosmology Telescope: A Catalog of Galaxy Clusters from the 2008-2018 ACT Survey," where I played a key role in processing and analyzing years of ACT data to produce a comprehensive catalog. This involved intricate signal processing techniques to extract faint SZ signals from noisy CMB maps and rigorous statistical methods to characterize cluster properties such as their redshifts, richness, and estimated masses. The catalogs resulting from these efforts provide essential, high-quality samples of galaxy clusters that are crucial for a diverse range of cosmological applications, including constraining dark energy parameters, measuring the sum of neutrino masses, and investigating the formation and evolution of structure. This work has not only expanded the census of known galaxy clusters but also provided invaluable datasets for future cosmological and astrophysical investigations.

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
