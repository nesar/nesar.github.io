---
title: "Cosmology & Large-Scale Structure"
excerpt: "Research in cosmology & large-scale structure"
collection: portfolio
---

Cosmology and large-scale structure research endeavors to understand the origin, evolution, and fundamental constituents of the Universe. A central focus is the intricate cosmic web, a vast network of dark matter haloes, filaments, and voids, which serves as the scaffolding for baryonic matter and galaxy formation. Investigating its properties provides crucial insights into the interplay of gravity, dark matter, and dark energy, the enigmatic components believed to constitute the majority of the Universe's mass-energy budget.

Key challenges in this field include precisely characterizing the distribution and dynamics of dark matter, distinguishing between the standard cosmological model and alternative theories like modified gravity, and developing robust methods to extract cosmological parameters from complex observational data. Methodologies range from high-resolution N-body simulations of cosmic structures to advanced statistical analyses of probes such as cosmic shear, galaxy surveys, and Sunyaev-Zel'dovich (SZ) effect measurements. These efforts are vital for testing General Relativity on cosmological scales and unveiling the nature of dark energy.

My research significantly advances our understanding of dark matter, the cosmic web, and the constraints on cosmological models. I have extensively investigated the multi-stream nature of dark matter, exploring how the complex kinematics of dark matter streams shape the topology and geometry of the cosmic web, and detailing the caustic design of dark matter haloes and filaments. This multi-stream view offers a deeper insight into the phase-space structure of dark matter, providing novel approaches for tracing and characterizing cosmic structures beyond simple density fields. Furthermore, I have contributed to large observational efforts such as the SPTpol Extended Cluster Survey, applying these theoretical frameworks to real-world data.

A substantial part of my work focuses on testing fundamental physics and developing cutting-edge computational tools. I have played a key role in constraining alternative gravity theories, specifically $f(R)$ gravity, using a $k$-cut cosmic shear analysis of Hyper Suprime-Cam data, thereby placing stringent limits on deviations from General Relativity. To efficiently explore vast parameter spaces, I developed a sophisticated matter power spectrum emulator for $f(R)$ modified gravity cosmologies. Complementing this, I have pioneered the application of machine learning, including differentiable predictions for large-scale structure with SHAMNet, and developed physical benchmarking techniques for AI-generated cosmic web simulations. These innovations demonstrate the power of AI to accelerate cosmological research while ensuring physical consistency, providing critical tools and analyses for current and future surveys, and pushing the boundaries of our understanding of the Universe.

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
