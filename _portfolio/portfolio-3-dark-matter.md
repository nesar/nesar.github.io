---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The study of dark matter and cosmology is fundamental to understanding the universe's structure, evolution, and underlying physical laws. Dark matter, comprising approximately 27% of the universe's mass-energy budget, dictates the formation and distribution of cosmic structures, from galaxies to the vast cosmic web. Key challenges in this field include identifying the precise nature of dark matter, accurately mapping its distribution across cosmic scales, and rigorously testing alternative theories of gravity that might explain observed cosmic acceleration without recourse to dark energy. Researchers in this area employ a combination of sophisticated cosmological simulations, advanced statistical analyses of observational data, and novel theoretical frameworks to address these profound questions.

The formation of the cosmic web—a complex network of voids, sheets, filaments, and dark matter halos—is a direct consequence of gravitational instability acting on dark matter. Understanding its topology, geometry, and internal structure, particularly the intricate multi-stream substructure within dark matter halos, is crucial for modeling galaxy formation and evolution. Furthermore, comparing predictions from General Relativity and its modifications (such as $f(R)$ gravity) against precise observational probes like cosmic shear provides stringent tests of our cosmological model. The advent of artificial intelligence (AI) also presents transformative opportunities to accelerate cosmological simulations and data analysis, necessitating rigorous physical benchmarking methodologies to ensure scientific accuracy.

My research significantly contributes to these frontiers by developing and applying innovative computational and analytical techniques. I have conducted pioneering work in constraining modified theories of gravity, specifically $f(R)$ gravity, by performing a $k$-cut cosmic shear analysis of data from the Hyper Suprime-Cam First-Year Survey. This method offers a robust way to isolate cosmological signals and set tighter constraints on deviations from General Relativity. A core focus of my work also involves unraveling the intricate multi-stream nature of dark matter flows. I have developed methods to characterize the caustic design of the dark matter web and dark matter haloes, providing a multi-stream view of their topology and geometry, which is essential for understanding the highly non-linear gravitational collapse that forms these structures.

Furthermore, I have developed and applied sophisticated cosmological simulations, such as CRK-HACC, to model galaxy formation within the evolving cosmic web, providing a more accurate representation of baryonic processes in complex dark matter environments. Recognizing the burgeoning role of machine learning in cosmology, I have also contributed to the development of robust physical benchmarking strategies for AI-evolved cosmological structure formation. This ensures that AI-generated models and simulations accurately reproduce key physical properties of the cosmic web and its constituents, thereby maintaining scientific fidelity. Through these contributions, my work provides enhanced tools for tracing the cosmic web, improves our understanding of dark matter dynamics, and strengthens the foundations for future cosmological discoveries.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from Topology and geometry of the dark matter web: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Topology and geometry of the dark matter web: a multistream view</div>
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
