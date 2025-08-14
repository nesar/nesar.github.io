---
title: "General AI/ML Methodologies for Science"
excerpt: "Research in general ai/ml methodologies for science"
collection: portfolio
---

The integration of artificial intelligence and machine learning methodologies is rapidly transforming scientific research, offering unprecedented capabilities for accelerating discovery and knowledge synthesis. Scientific domains are characterized by vast and ever-growing bodies of literature, complex experimental data, and intricate theoretical frameworks, making it challenging for human researchers to keep pace with all relevant information. AI/ML techniques provide powerful tools for navigating this complexity, enabling efficient information retrieval, sophisticated data analysis, and the generation of novel hypotheses.

A critical area within this paradigm involves leveraging large language models (LLMs) to act as intelligent research assistants. However, for AI models to be truly valuable in high-stakes scientific contexts, they must be capable of precise knowledge extraction, demonstrate high fidelity to source material, and operate with verifiable reliability. This necessitates not only the development of advanced systems that can efficiently process and synthesize scientific information but also robust methodologies for systematically evaluating their performance, ensuring their outputs are accurate, relevant, and trustworthy for the rigorous demands of scientific inquiry.

My work in this area addresses these fundamental challenges by developing sophisticated AI/ML methodologies specifically tailored for scientific application. I have developed HiPerRAG: High-Performance Retrieval Augmented Generation for Scientific Insights, which significantly advances the capability of AI models to effectively interact with and derive value from vast scientific corpora. This methodology focuses on optimizing the retrieval and generation processes to ensure rapid and accurate synthesis of complex scientific information, thereby accelerating the identification of patterns, connections, and insights that might otherwise remain hidden within disparate sources. HiPerRAG is engineered for scalability and efficiency, making it a powerful tool for navigating the immense volume of scientific literature.

Complementing this, I have also established EAIRA: a Methodology for Evaluating AI Models as Scientific Research Assistants. Recognizing the imperative for reliability and trustworthiness in scientific tools, EAIRA provides a systematic and rigorous framework for assessing the performance, accuracy, and utility of AI models when deployed in a scientific research assistant capacity. This methodology defines metrics and protocols for evaluating an AI's ability to retrieve relevant information, answer complex scientific queries, and provide accurate summaries, ensuring that these AI tools meet the stringent quality standards required for scientific exploration and discovery. My work with EAIRA aims to build confidence in AI-assisted research, providing a critical foundation for the responsible integration of these technologies into scientific workflows.

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
