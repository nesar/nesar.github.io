---
title: "AI & LLMs as Scientific Research Assistants"
excerpt: "Research in ai & llms as scientific research assistants"
collection: portfolio
---

The advent of Artificial Intelligence and Large Language Models (LLMs) is rapidly transforming the landscape of scientific research, offering unprecedented capabilities to process vast datasets, identify complex patterns, and generate insights. In an era characterized by an exponential increase in scientific literature and experimental data, these intelligent systems are becoming indispensable tools for augmenting human cognition and accelerating discovery. They hold the promise of democratizing access to specialized knowledge and automating tedious, time-consuming tasks, thereby allowing researchers to focus on higher-level conceptual challenges.

Developing AI and LLM agents that can effectively function as reliable scientific research assistants presents unique challenges. These include the necessity for deep domain-specific understanding, the ability to perform complex reasoning beyond simple information retrieval, and the capacity to interact with and interpret specialized data formats and scientific language. Furthermore, robust methodologies are required to rigorously evaluate their performance and ensure their reliability in critical scientific contexts. Research in this area focuses on engineering models that not only exhibit high factual accuracy but also demonstrate sophisticated problem-solving skills tailored to specific scientific disciplines, such as astrophysics and cosmology.

My work extensively addresses these challenges by developing and evaluating AI and LLM agents specifically designed to function as high-performance scientific research assistants. I have focused on creating domain-specialized models that excel in complex scientific reasoning and data interpretation. For instance, the AstroMLab series demonstrates this capability, with AstroMLab 3 achieving GPT-4o level performance and AstroMLab 4 establishing benchmark-topping results in astronomy Q&A using specialized 8B and 70B-parameter models, respectively. This involved not just fine-tuning, but architecting models that can deeply understand and generate scientific discourse. Beyond general knowledge, I have also developed specialized tools like InferA, a smart assistant tailored for navigating and analyzing complex cosmological ensemble data, and explored methodologies for "Teaching LLMs to Speak Spectroscopy," enabling them to interpret highly technical, domain-specific scientific language.

A crucial aspect of my research involves establishing rigorous frameworks for assessing these AI assistants. To this end, I led the development of EAIRA, a comprehensive methodology designed for Evaluating AI Models as Scientific Research Assistants, ensuring that their performance is systematically benchmarked and validated against scientific standards. My contributions also include pioneering work in defining the capabilities of these models, as explored in AstroMLab 1 which investigated their proficiency in nuanced scientific question-answering. Collectively, this research provides both the theoretical underpinnings and practical implementations for building intelligent agents that can significantly augment human researchers, handle vast quantities of specialized data, and accelerate the pace of scientific discovery in complex fields like astrophysics.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/infera-a-smart-assistant-for-cosmological-ensemble_plot_1_590fdcf1.png" alt="Figure from InferA: A Smart Assistant for Cosmological Ensemble Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: InferA: A Smart Assistant for Cosmological Ensemble Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants</div>
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
