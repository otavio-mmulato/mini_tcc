document.addEventListener('DOMContentLoaded', () => {
    const track = document.getElementById('products-carousel');
    const nextButton = document.getElementById('next-btn');
    const prevButton = document.getElementById('prev-btn');

    // Se o carrossel ou os produtos não existirem, o script para.
    if (!track || !nextButton || !prevButton || track.children.length === 0) {
        if (track && track.children.length === 0) {
            track.innerHTML = '<p>Nenhum produto em destaque no momento.</p>';
            if (nextButton) nextButton.style.display = 'none';
            if (prevButton) prevButton.style.display = 'none';
        }
        return;
    }

    const originalCards = Array.from(track.children);
    let cardCount = originalCards.length;
    let isMoving = false; // Flag para evitar cliques múltiplos durante a transição

    // 1. Clonar os itens para criar o efeito infinito
    // Adiciona os clones do final no início
    originalCards.slice().reverse().forEach(card => {
        track.prepend(card.cloneNode(true));
    });
    // Adiciona os clones do início no final
    originalCards.slice().forEach(card => {
        track.append(card.cloneNode(true));
    });

    let currentIndex = cardCount; // Começa no primeiro item da lista original

    function updatePosition(withTransition = true) {
        const card = track.querySelector('.product-card');
        const gap = parseFloat(getComputedStyle(track).gap) || 24;
        const cardWidth = card.offsetWidth;
        const scrollAmount = cardWidth + gap;

        // Aplica a transição ou a remove para o "salto" instantâneo
        track.style.transition = withTransition ? 'transform 0.5s ease-in-out' : 'none';
        track.style.transform = `translateX(-${currentIndex * scrollAmount}px)`;
    }

    // Posicionamento inicial sem animação
    updatePosition(false);

    // 2. Lógica dos botões
    nextButton.addEventListener('click', () => {
        if (isMoving) return;
        isMoving = true;
        currentIndex++;
        updatePosition();
    });

    prevButton.addEventListener('click', () => {
        if (isMoving) return;
        isMoving = true;
        currentIndex--;
        updatePosition();
    });

    // 3. A "mágica" do loop infinito
    // Ouve o evento que marca o fim da transição CSS
    track.addEventListener('transitionend', () => {
        isMoving = false; // Permite o próximo clique

        // Se o carrossel chegou no final da lista (nos clones do início)
        if (currentIndex >= cardCount * 2) {
            currentIndex = cardCount; // Volta para o primeiro item original
            updatePosition(false); // Salto instantâneo, sem animação
        }

        // Se o carrossel chegou no início da lista (nos clones do final)
        if (currentIndex <= cardCount - 1) {
            currentIndex = cardCount * 2 - 1; // Volta para o último item original
            updatePosition(false); // Salto instantâneo, sem animação
        }
    });

    // Atualiza o carrossel caso a janela seja redimensionada
    window.addEventListener('resize', () => updatePosition(false));
});