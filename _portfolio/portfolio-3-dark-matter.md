---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Cosmology endeavors to unravel the fundamental nature and evolution of the universe, with dark matter standing as a pivotal, yet elusive, component of the standard cosmological model. This mysterious substance, which interacts primarily through gravity, dictates the formation and intricate architecture of the cosmic web – the vast network of galaxy clusters, filaments, and voids that define the large-scale structure of the cosmos. Understanding the distribution and dynamics of dark matter within this cosmic web is crucial for deciphering how galaxies and larger structures assembled over cosmic time. Observational techniques such as weak gravitational lensing, large-scale galaxy surveys, and analyses of the cosmic microwave background provide essential data for probing this dark matter scaffolding and validating theoretical predictions.

Despite its observational evidence, the precise particle nature of dark matter remains unknown, and its gravitational effects are often intertwined with cosmic acceleration attributed to dark energy. This has spurred investigations into alternative cosmological models, such as modified gravity theories (e.g., f(R) gravity), which propose alterations to Einstein's General Relativity on cosmological scales. These theories offer potential explanations for cosmic phenomena without necessarily invoking dark energy, or by modifying the gravitational interaction of dark matter. Discriminating between these competing paradigms necessitates robust observational constraints derived from increasingly precise and expansive cosmological surveys.

My research significantly contributes to addressing these fundamental questions by developing and applying advanced methodologies to probe the distribution and nature of dark matter, analyze the intricate structure of the cosmic web, and refine techniques for testing cosmological models. For instance, I have employed a novel *k-cut cosmic shear analysis* on data from the Hyper Suprime-Cam to place stringent constraints on *f(R) gravity*, limiting potential deviations from General Relativity. Furthermore, my work extensively characterizes the dark matter web through *multistream views*, revealing its complex *topology and geometry* and elucidating the internal dynamics and *caustic design* of *dark matter haloes*.

I have also focused on enhancing the accuracy and reliability of observational probes. This includes *reducing model error using optimised galaxy selection* for improved *weak lensing cluster mass estimation*, which is critical for precise cosmological parameter inference. My investigations span the full range of cosmic scales, contributing to major efforts such as the *SPTpol Extended Cluster Survey* and the future *SPHEREx Satellite Mission*, which promises unprecedented spectroscopic insights into cosmic evolution. Moreover, I have explored the intersection of astrophysics and artificial intelligence, conducting *physical benchmarking for AI-generated cosmic web* simulations to ensure their scientific fidelity, and have mapped the Milky Way's structure from its inner regions to the outer halo using a comprehensive *photometric sample of 2.6 million Red Clump stars*. This broad research portfolio integrates theoretical insights, sophisticated data analysis, and an forward-looking approach to future instrumentation to continually advance our understanding of the universe's dark side.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-spherex-satellite-mission_plot_1_630d5d67.png" alt="Figure from The SPHEREx Satellite Mission" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The SPHEREx Satellite Mission</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/physical-benchmarking-for-ai-generated-cosmic-web_plot_1_11f44910.png" alt="Figure from Physical Benchmarking for AI-Generated Cosmic Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Physical Benchmarking for AI-Generated Cosmic Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
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
