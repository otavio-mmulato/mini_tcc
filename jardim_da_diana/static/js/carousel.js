// static/js/carousel.js

document.addEventListener('DOMContentLoaded', () => {
    const track = document.getElementById('products-carousel');
    const nextButton = document.getElementById('next-btn');
    const prevButton = document.getElementById('prev-btn');

    // Se o carrossel ou os produtos não existirem, o script para.
    if (!track || !nextButton || !prevButton || track.children.length === 0) {
        if (track && track.children.length === 0) {
            track.innerHTML = '<p>Nenhum produto em destaque no momento.</p>';
            if(nextButton) nextButton.style.display = 'none';
            if(prevButton) prevButton.style.display = 'none';
        }
        return;
    }

    let currentIndex = 0;

    const updateCarousel = () => {
        const card = track.querySelector('.product-card');
        const gap = parseFloat(getComputedStyle(track).gap) || 24; // 24px = 1.5rem (padrão)
        const cardWidth = card.offsetWidth;
        const scrollAmount = cardWidth + gap;
        const totalCards = track.children.length;
        const wrapperWidth = track.parentElement.offsetWidth;
        const visibleCards = Math.floor((wrapperWidth + gap) / scrollAmount);

        track.style.transform = `translateX(-${currentIndex * scrollAmount}px)`;

        // Desabilita os botões quando chega ao fim ou ao início
        prevButton.disabled = currentIndex === 0;
        nextButton.disabled = currentIndex >= totalCards - visibleCards;
    };

    nextButton.addEventListener('click', () => {
        currentIndex++;
        updateCarousel();
    });

    prevButton.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    });

    // Atualiza o carrossel caso a janela seja redimensionada
    window.addEventListener('resize', updateCarousel);
    
    // Chamada inicial para configurar os botões corretamente
    updateCarousel();
});