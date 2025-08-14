---
title: "AI Methodologies & Evaluation for Science"
excerpt: "Research in ai methodologies & evaluation for science"
collection: portfolio
---

The application of artificial intelligence to scientific research holds immense promise for accelerating discovery, synthesizing vast amounts of information, and assisting researchers in complex tasks. As the volume of scientific literature continues to grow exponentially, researchers face significant challenges in identifying relevant information, extracting insights, and discerning novel connections across diverse domains. AI-driven solutions, particularly those involving advanced natural language processing, are emerging as critical tools to navigate this complexity, streamline knowledge acquisition, and foster innovation within the scientific community.

However, the integration of AI into the scientific workflow is not without its challenges. Ensuring the accuracy, reliability, and interpretability of AI-generated insights is paramount in a field where precision and trustworthiness are non-negotiable. This necessitates the development of robust methodologies for both building high-performing AI systems tailored for scientific data and rigorously evaluating their efficacy and safety. Establishing clear benchmarks and evaluation frameworks is crucial to validate the utility of AI models as scientific research assistants and to guide their responsible deployment.

My research focuses on addressing these critical needs by developing cutting-edge AI methodologies specifically designed for scientific applications and creating robust frameworks for their evaluation. I have developed HiPerRAG, a High-Performance Retrieval Augmented Generation system tailored for extracting and synthesizing scientific insights. This work contributes to advancing the state-of-the-art in RAG by optimizing the retrieval and generation components for the unique characteristics of scientific literature, including complex terminology, intricate relationships, and diverse data formats. HiPerRAG aims to significantly enhance researchers' ability to rapidly glean actionable insights from large scientific corpora, thereby accelerating hypothesis generation and discovery.

Furthermore, recognizing the imperative for reliable AI in scientific contexts, I have established EAIRA: a comprehensive Methodology for Evaluating AI Models as Scientific Research Assistants. This work provides a systematic framework for assessing the performance, reliability, and utility of AI systems intended to support scientific endeavors. EAIRA defines key metrics and protocols necessary to rigorously evaluate AI models’ capabilities in tasks such as literature review, data synthesis, and experimental design, ensuring that these tools meet the high standards required for scientific integrity and advancement. My contributions in HiPerRAG and EAIRA collectively advance the development and responsible integration of AI to empower the next generation of scientific breakthroughs.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/hiperrag-high-performance-retrieval-augmented-gene_plot_1_969c22b8.png" alt="Figure from HiPerRAG: High-Performance Retrieval Augmented Generation for Scientific Insights" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: HiPerRAG: High-Performance Retrieval Augmented Generation for Scientific Insights</div>
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
