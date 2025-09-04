---
title: "Galactic & Stellar Astronomy, and Astronomical LLMs"
excerpt: "Research in galactic & stellar astronomy, and astronomical llms"
collection: portfolio
---

The field of Galactic and Stellar Astronomy is dedicated to understanding the structure, formation, and evolution of our Milky Way galaxy and the myriad stars residing within it. This endeavor involves analyzing vast observational datasets, from photometric surveys that map stellar populations to spectroscopic data that reveals detailed stellar properties, chemical compositions, and kinematics. Researchers in this area employ sophisticated data analysis techniques to characterize stellar types like red clump stars or rare metal-poor stars, thereby piecing together the complex history and dynamics of our galactic neighborhood.

In parallel, the rapidly advancing domain of Astronomical Large Language Models (LLMs) is revolutionizing how astronomical knowledge is managed and accessed. These specialized artificial intelligence systems are trained on extensive scientific literature and data to comprehend, generate, and reason about complex astronomical concepts. By providing intelligent interfaces for querying vast amounts of information, astronomical LLMs are poised to accelerate scientific discovery, streamline research workflows, and make intricate astrophysical knowledge more broadly accessible to both experts and enthusiasts.

My research contributions significantly span both these vital areas, from probing the fundamental structure and stellar populations of the Milky Way to engineering cutting-edge AI tools for astronomical inquiry. In Galactic and Stellar Astronomy, I have engaged in large-scale data analysis to map our home galaxy. Notably, I have constructed a comprehensive photometric sample of 2.6 million Red Clump stars, enabling detailed investigations into the Milky Way's inner and outer disk structure. Furthermore, my work has utilized *Gaia* DR3 BP/RP Spectra to identify candidates for Carbon-Enhanced Metal-Poor (CEMP) stars, which serve as crucial tracers for understanding early stellar evolution and the chemical enrichment history of the galaxy.

A significant portion of my recent efforts has focused on developing and refining Astronomical LLMs through the AstroMLab series. My initial work, "AstroMLab 1: Who Wins Astronomy Jeopardy!?", established early benchmarks for LLM performance in astronomy Q&A. Building on this foundation, I led the development of specialized models that demonstrate remarkable capabilities; "AstroMLab 3" showcased an 8B-parameter model achieving GPT-4o level performance in astronomy, highlighting the efficiency and power of domain-specialization. This was further advanced in "AstroMLab 4," where a 70B-parameter domain-specialized reasoning model achieved benchmark-topping performance in complex astronomy question-answering. Crucially, my work extends beyond mere textual understanding; in "Teaching LLMs to Speak Spectroscopy," I developed methodologies to enable LLMs to directly interpret and analyze spectroscopic data, effectively bridging the gap between advanced language models and fundamental scientific observations. These contributions collectively enhance our ability to extract knowledge and insights from the ever-growing astronomical data landscape.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model</div>
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
