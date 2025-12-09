---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The distribution and evolution of dark matter constitute a cornerstone of modern cosmology, dictating the formation of structures from galaxy clusters to the vast cosmic web. This invisible component, believed to comprise approximately 27% of the universe's mass-energy budget, is essential for explaining observed galactic rotation curves, gravitational lensing phenomena, and the large-scale structure of the cosmos. Understanding the precise nature of dark matter, its gravitational interactions, and its imprint on the cosmic web – a complex network of filaments, haloes, and voids – is paramount for validating or refining the Standard Model of Cosmology, including potential modifications to General Relativity like f(R) gravity.

Research in this field relies heavily on a synergistic approach combining sophisticated cosmological simulations with robust analyses of astronomical observational data. Simulations model the gravitational growth of structures, while observational techniques such as weak gravitational lensing, surveys of stellar populations, and cluster catalogs provide crucial empirical constraints. These efforts aim to precisely map the universe's mass distribution, probe the dynamics within dark matter haloes, and test the predictions of various cosmological models and theories of modified gravity.

My work significantly contributes to this understanding by developing and applying advanced computational and analytical techniques to unravel the mysteries of dark matter and the cosmic web. I have extensively characterized the intricate structure of dark matter, exploring its "multistream view," "caustic design," and the "topology and geometry" of the cosmic web, tracing its evolution across cosmic time. To this end, I have utilized and developed tools like CRK-HACC for modeling galaxy formation in cosmological simulations and created a "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" to efficiently explore alternative gravitational theories. Furthermore, I developed SHAMNet for "Differentiable Predictions for Large Scale Structure," enhancing our ability to optimize cosmological models.

On the observational front, my research involves confronting theoretical predictions with real-world data. I have performed "Constraining f(R) Gravity with a k-cut Cosmic Shear Analysis" using data from the Hyper Suprime-Cam, demonstrating a robust method to test modified gravity theories. I have also focused on "Reducing Model Error Using Optimised Galaxy Selection" for weak lensing cluster mass estimation. My work further leverages large-scale surveys and stellar kinematics, using "Photometric Samples of Red Clump Stars" to trace mass in the Milky Way and identifying "Carbon-Enhanced Metal-Poor star candidates" from Gaia DR3 to probe early stellar populations and their dark matter environments. These contributions, alongside involvement in projects like "The SPHEREx Satellite Mission" and "The SPTpol Extended Cluster Survey," aim to provide increasingly precise constraints on dark matter properties and cosmological parameters.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
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
