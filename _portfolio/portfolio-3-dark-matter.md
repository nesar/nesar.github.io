---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter constitutes approximately 85% of the universe's matter content, playing a pivotal role in the formation and evolution of cosmic structures, from galaxies to vast galaxy clusters and the intricate cosmic web. Its enigmatic nature, invisible to electromagnetic radiation, presents one of the most significant challenges in modern astrophysics and cosmology. Understanding the distribution, dynamics, and fundamental properties of dark matter is crucial for accurately modeling the universe's expansion history, the growth of large-scale structure, and the processes driving galaxy formation.

Researchers tackle these challenges through a multifaceted approach combining sophisticated numerical simulations, extensive observational surveys, and advanced theoretical frameworks. Cosmological simulations, particularly N-body and hydrodynamical simulations, are indispensable tools for evolving the universe from its early state to the present day, revealing how gravity shapes the cosmic web and how baryons interact within dark matter halos. Concurrently, large-scale observational surveys, such as weak lensing and galaxy redshift surveys, provide crucial data to test theoretical predictions, constrain cosmological parameters, and probe fundamental physics, including alternative theories of gravity.

My research program focuses on developing and applying cutting-edge methodologies to unravel the mysteries of dark matter and cosmic structure formation. I have significantly contributed to advancing cosmological simulations, including modeling galaxy formation within the CRK-HACC framework. A key aspect of my work involves pioneering the integration of artificial intelligence and machine learning techniques into cosmological studies. This includes benchmarking AI-evolved cosmological structure formation, employing physical benchmarking for AI-generated cosmic web models, and developing differentiable prediction tools like SHAMNet to accelerate theoretical predictions and reduce model errors for large-scale structure.

Furthermore, I have actively engaged in extracting cosmological constraints from observational data. This includes analyzing weak lensing signals from surveys like Hyper Suprime-Cam, where I contributed to constraining modified gravity theories such as $f(R)$ gravity using a $k$-cut cosmic shear analysis. My work also addresses improving the accuracy of observational measurements, for instance, by reducing model error through optimized galaxy selection for weak lensing cluster mass estimation in surveys like SPTpol. A substantial part of my research delves into the intricate architecture of the dark matter web, exploring its topology and geometry through a multi-stream view and analyzing the caustic design of dark matter halos, providing a detailed understanding of the dynamic processes underpinning cosmic structure. I have also contributed to defining the scientific potential of future missions like SPHEREx.

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
    <img src="/images/research/figures/physical-benchmarking-for-ai-generated-cosmic-web_plot_1_11f44910.png" alt="Figure from Physical Benchmarking for AI-Generated Cosmic Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Physical Benchmarking for AI-Generated Cosmic Web</div>
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
