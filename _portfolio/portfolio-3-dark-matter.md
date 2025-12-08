---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter, an elusive and non-baryonic component of the universe, plays a pivotal role in the formation and evolution of cosmic structures. Its gravitational influence is believed to be the primary driver behind the formation of the vast cosmic web, an intricate network of dark matter haloes, filaments, and voids that permeates the universe and provides the scaffolding upon which galaxies coalesce and evolve. Understanding the properties and distribution of dark matter, the dynamics of the cosmic web, and the processes of galaxy formation within these structures are central goals of modern cosmology, requiring a synergy of advanced theoretical modeling, high-resolution cosmological simulations, and precise observational measurements.

The study of dark matter and cosmology also extends to probing the fundamental laws of gravity itself, particularly on cosmological scales. Alternative theories of gravity, such as $f(R)$ gravity, propose modifications to Einstein's General Relativity that could manifest in the growth of cosmic structures and the distribution of matter. Constraining these theories through observational data, such as weak gravitational lensing, provides crucial tests for the standard cosmological model and offers pathways to uncover the nature of gravity and the universe's evolution. Upcoming missions, like SPHEREx, are designed to provide unprecedented insights into galaxy evolution and large-scale structure, further enhancing our ability to test these fundamental models.

My research extensively explores the complex interplay between dark matter, cosmic structure formation, and galaxy evolution, employing a combination of cutting-edge cosmological simulations and rigorous analyses of observational data. I have contributed to the development and application of advanced simulation tools, such as the CRK-HACC code, to model galaxy formation in a cosmological context, enabling detailed investigations into how baryonic physics interacts with the dark matter distribution. A significant aspect of my work focuses on characterizing the architecture of the dark matter web and its constituent dark matter haloes through a "multistream view," which has allowed for a deeper understanding of their topology, geometry, and the intricate caustic design inherent within these structures.

Furthermore, I have actively engaged in leveraging observational datasets to test and refine cosmological models. This includes conducting a $k$-cut Cosmic Shear Analysis of the Hyper Suprime-Cam First-Year Data to place robust constraints on $f(R)$ gravity, thereby contributing to the ongoing effort to test General Relativity on cosmological scales. My involvement with missions like the SPHEREx Satellite Mission and surveys such as the SPTpol Extended Cluster Survey reflects my commitment to utilizing future and existing large-scale observational data to trace the cosmic web and characterize its properties, ensuring that our theoretical frameworks are continually challenged and informed by the most precise empirical evidence available. Through these efforts, I aim to unravel the mysteries of dark matter and advance our understanding of the fundamental principles governing the cosmos.

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
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
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
