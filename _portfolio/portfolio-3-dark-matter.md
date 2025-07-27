---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter constitutes approximately 27% of the universe's energy density and plays a pivotal role in the formation and evolution of cosmic structures. This enigmatic component, which does not emit, absorb, or reflect light, interacts only through gravity. Its gravitational influence is essential for explaining the observed rotation curves of galaxies, the dynamics of galaxy clusters, and the large-scale distribution of matter across the cosmos. Understanding the nature and distribution of dark matter is one of the most pressing challenges in modern astrophysics and cosmology, driving extensive research efforts across theoretical, observational, and computational domains.

The gravitational collapse of dark matter over cosmic time has sculpted the universe into a vast, intricate network often referred to as the "cosmic web." This filamentary structure comprises dense galaxy clusters, interconnected by elongated filaments, and surrounding vast, empty voids. The cosmic web serves as the scaffolding upon which galaxies and other luminous structures form, making its study crucial for comprehending the universe's formation history. Researchers employ diverse techniques to map its topology, quantify its properties, and test fundamental cosmological models, including those that propose modifications to Einstein's theory of general relativity.

My research significantly contributes to unraveling the mysteries of dark matter and the cosmic web through a combination of sophisticated observational analyses and theoretical insights. I have directly engaged with the challenge of constraining modified theories of gravity, such as f(R) gravity, by developing and applying a k-cut cosmic shear analysis to the Hyper Suprime-Cam (HSC) First-Year data. This technique leverages the subtle distortions of distant galaxy shapes caused by gravitational lensing, providing a powerful probe of the universe's matter distribution and the underlying gravitational theory. Furthermore, my work extends to mapping the baryonic components of the cosmic web and its environments. I have utilized large photometric samples, including a robust dataset of 2.6 million Red Clump stars, to meticulously trace the structure of the Milky Way, offering crucial insights into galactic formation within the broader cosmic web context. My contributions also include participation in the SPTpol Extended Cluster Survey, instrumental in identifying the densest nodes of the cosmic web.

Beyond observational constraints, I have delved into the fundamental nature of dark matter distribution and the fine-grained structure of the cosmic web through advanced theoretical and computational frameworks. My work has involved pioneering the multi-stream view to understand the complex dynamics of dark matter haloes, revealing their intricate internal structure and the caustic design inherent within the dark matter web. This innovative approach allows for a detailed investigation into the number of dark matter streams passing through any given point, providing a more comprehensive portrait of dark matter haloes and the broader cosmic web. I have also rigorously investigated the topology and geometry of the dark matter web from this multi-stream perspective, offering novel quantitative measures for characterizing its intricate features. These theoretical developments and their application to simulations significantly advance our understanding of how dark matter particles coalesce and form the backbone of the universe's large-scale structure.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from topology and geometry of the dark matter web a mul" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: topology and geometry of the dark matter web a mul</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from the caustic design of the dark matter web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: the caustic design of the dark matter web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_2_ec781175.png" alt="Figure from topology and geometry of the dark matter web a mul" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: topology and geometry of the dark matter web a mul</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_3_a3b0a1c0.png" alt="Figure from the caustic design of the dark matter web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: the caustic design of the dark matter web</div>
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
