---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Modern cosmology faces profound questions regarding the composition and evolution of the universe. A significant puzzle is the existence of dark matter, an elusive substance that accounts for approximately 27% of the universe's mass-energy budget. Its presence is inferred through overwhelming gravitational evidence across various scales, from galaxy rotation curves to gravitational lensing in galaxy clusters and the cosmic microwave background anisotropies. Despite this evidence, dark matter does not interact with light or other electromagnetic radiation, making it invisible to conventional telescopes. The leading theoretical candidates for dark matter are Weakly Interacting Massive Particles (WIMPs), hypothetical particles that could interact via the weak nuclear force and gravity, offering a potential explanation for its non-baryonic nature.

Complementing the search for dark matter is the quest to understand the universe's earliest moments. The inflationary paradigm proposes a period of exponential expansion immediately after the Big Bang, resolving several cosmological problems and providing the seeds for large-scale structure formation. This epoch left indelible imprints on the Cosmic Microwave Background (CMB), the faint afterglow of the Big Bang. Precise measurements of the CMB's temperature and polarization anisotropies serve as powerful probes into the physics of inflation, allowing scientists to constrain models of the early universe, investigate the nature of primordial fluctuations, and search for signatures of primordial gravitational waves.

My research significantly contributes to both these critical areas of modern physics. In the search for dark matter, I have been involved in the direct detection effort to identify WIMP particles. Specifically, my work has focused on leveraging data from the LZ (LUX-ZEPLIN) experiment, a leading liquid xenon detector designed to observe the exceedingly rare interactions between WIMPs and atomic nuclei. Through rigorous data analysis, event discrimination, and background characterization, I have contributed to setting some of the most stringent constraints on the WIMP-nucleon scattering cross-section, significantly reducing the allowed parameter space for these dark matter candidates and guiding the next generation of theoretical models and experimental designs.

Concurrently, I have explored the fundamental physics of the early universe by analyzing cosmic microwave background data. My contributions involve developing and applying sophisticated statistical techniques to extract cosmological parameters from CMB anisotropy measurements, with a particular focus on constraining inflationary models. By meticulously analyzing patterns in CMB temperature and polarization, I have worked to probe the existence and characteristics of primordial gravitational waves, often parameterized by the tensor-to-scalar ratio (r). This work provides crucial empirical tests for various inflationary scenarios, helping to refine our understanding of the universe's initial conditions and the high-energy physics governing its birth.

<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>

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
