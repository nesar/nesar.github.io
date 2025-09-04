---
title: "Cosmology & Large-Scale Structure"
excerpt: "Research in cosmology & large-scale structure"
collection: portfolio
---

The study of Cosmology and Large-Scale Structure (LSS) seeks to unravel the Universe's evolution, from its initial conditions to the formation of the complex cosmic web observed today. This field critically examines the distribution of matter and energy on vast scales, predominantly shaped by the elusive dark matter and dark energy. Understanding the formation and properties of structures like galaxy clusters, filaments, and voids provides crucial insights into the fundamental laws governing the Universe, including the nature of gravity, the composition of matter, and the origin of cosmic acceleration.

Modern cosmological research relies on a synergy of theoretical modeling, high-resolution numerical simulations, and cutting-edge observational surveys. Techniques such as gravitational lensing, the Sunyaev-Zel'dovich effect, and spectroscopic surveys of galaxies and quasars are employed to map the distribution of matter, measure cosmic expansion, and probe the dynamics of large-scale structures. A significant challenge lies in disentangling standard cosmological models from potential deviations, such as modified theories of gravity, which could have profound implications for our understanding of the cosmos.

My research has focused on developing a comprehensive understanding of the dark matter web and its observational signatures. I have extensively utilized simulations to characterize the intricate substructure of dark matter, exploring the "multi-stream portrait" of the cosmic web and dark matter haloes. This work investigates the dynamics and distribution of matter, revealing how caustics form and contribute to the "caustic design" of the dark matter web. Furthermore, I have elucidated the complex "topology and geometry" of these structures, providing a detailed framework for "tracing the cosmic web" and its underlying gravitational potential.

In parallel, I have applied advanced analytical and computational methods to leverage observational data for cosmological insights. I have made significant contributions to constraining modified theories of gravity, specifically f(R) gravity, through a "k-cut cosmic shear analysis" of data from the Hyper Suprime-Cam First-Year survey. My work also includes refining observational techniques, such as "reducing model error using optimised galaxy selection" for more accurate weak lensing cluster mass estimation. Additionally, I have pioneered the use of "deep neural networks for peculiar velocity estimation from the Kinetic SZ Effect," offering a novel approach to measuring cosmic flows and contributing to large-scale surveys like "The SPTpol Extended Cluster Survey." These efforts collectively aim to enhance the precision of cosmological parameter measurements and probe the fundamental nature of gravity and dark matter.

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
