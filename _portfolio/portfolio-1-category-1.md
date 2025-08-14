---
title: "Domain-Specialized LLMs for Astronomy"
excerpt: "Research in domain-specialized llms for astronomy"
collection: portfolio
---

The burgeoning volume of data in modern astronomy presents both immense opportunities and significant challenges. Traditional methods of knowledge retrieval and analysis struggle to keep pace with the influx of information from telescopes, simulations, and theoretical models. While general-purpose Large Language Models (LLMs) have demonstrated impressive capabilities across many domains, their application in highly specialized scientific fields like astronomy often falls short. These general models frequently exhibit limitations such as a propensity for hallucination, a lack of deep domain-specific understanding, and an inability to perform complex scientific reasoning, leading to inaccuracies or superficial responses.

Addressing these shortcomings requires a targeted approach: the development of domain-specialized LLMs. Such models are meticulously trained on vast, curated datasets of scientific literature, observational data descriptions, theoretical frameworks, and expert Q&A in astronomy. This specialized training imbues them with a nuanced comprehension of astronomical concepts, terminology, and methodologies that general models cannot achieve. The goal is to create AI tools that not only retrieve facts but can also understand the intricate relationships between celestial phenomena, perform complex calculations, and even assist in the formulation of hypotheses, thereby truly augmenting human expertise and accelerating scientific discovery.

My research directly addresses this critical need by developing advanced domain-specialized Large Language Models specifically tailored for the field of astronomy, encapsulated in the AstroMLab series. Through this work, I have focused on achieving high performance and efficiency, even with more compact models. For instance, AstroMLab 3 showcases a specialized 8-billion-parameter model that achieves performance levels comparable to general-purpose models like GPT-4o in astronomical contexts, demonstrating that expert-level accuracy can be attained without requiring the immense computational resources of much larger models. Early work, highlighted in AstroMLab 1, laid the groundwork by exploring the capabilities and limitations of existing models in astronomical knowledge retrieval, akin to a scientific "Jeopardy!" challenge.

Building upon these foundations, my most recent work, AstroMLab 4, introduces a 70-billion-parameter domain-specialized reasoning model engineered for unparalleled performance in astronomy question-answering. This model represents a significant leap forward, not merely in knowledge recall but in its sophisticated reasoning capabilities, achieving benchmark-topping performance across complex astronomical queries. My contributions involve the development of novel fine-tuning methodologies, the creation of robust evaluation benchmarks, and the demonstration of these models' ability to process and synthesize highly technical astronomical information. This research significantly advances the state-of-the-art in AI for scientific discovery, making expert astronomical knowledge more accessible and efficient for researchers, educators, and the public alike, thereby accelerating the pace of astronomical inquiry.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png" alt="Figure from AstroMLab 1: Who Wins Astronomy Jeopardy!?" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: AstroMLab 1: Who Wins Astronomy Jeopardy!?</div>
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
