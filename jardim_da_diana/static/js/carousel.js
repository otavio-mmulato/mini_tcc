document.addEventListener('DOMContentLoaded', () => {
    const track = document.getElementById('products-carousel');
    const nextButton = document.getElementById('next-btn');
    const prevButton = document.getElementById('prev-btn');

    if (!track || !nextButton || !prevButton || track.children.length === 0) {
        if (track && track.children.length === 0) {
            track.innerHTML = '<p style="padding: 0 2rem; text-align: center; width: 100%;">Nenhum produto em destaque no momento.</p>';
        }
        if (nextButton) nextButton.style.display = 'none';
        if (prevButton) prevButton.style.display = 'none';
        return;
    }

    let originalCards = Array.from(track.children);
    let cardCount = originalCards.length;
    let itemsToClone = Math.ceil(5 / (100 / parseFloat(track.querySelector('.product-card-link').style.width || 85))) || 5;
    itemsToClone = Math.min(cardCount, itemsToClone);

    // --- 1. LÓGICA DE CLONAGEM PARA EFEITO INFINITO ---
    // Clona os primeiros itens e adiciona ao final
    for (let i = 0; i < itemsToClone; i++) {
        track.appendChild(originalCards[i].cloneNode(true));
    }
    // Clona os últimos itens e adiciona no início
    for (let i = cardCount - 1; i >= cardCount - itemsToClone; i--) {
        track.prepend(originalCards[i].cloneNode(true));
    }

    let currentIndex = itemsToClone;
    let isTransitioning = false;
    let isDragging = false;
    let startPos = 0;
    let currentTranslate = 0;
    let prevTranslate = 0;
    let animationID;

    // --- 2. FUNÇÕES DE MOVIMENTO ---
    const getCardWidth = () => track.querySelector('.product-card-link').offsetWidth;
    const getGap = () => parseFloat(getComputedStyle(track).gap) || 24;

    function setPositionByIndex() {
        currentTranslate = currentIndex * -(getCardWidth() + getGap());
        prevTranslate = currentTranslate;
        track.style.transform = `translateX(${currentTranslate}px)`;
    }

    function setTransition(active = true) {
        track.style.transition = active ? 'transform 0.5s ease-out' : 'none';
    }

    // Posicionamento inicial
    setTransition(false);
    setPositionByIndex();

    // --- 3. EVENTOS DOS BOTÕES ---
    nextButton.addEventListener('click', () => moveTo(currentIndex + 1));
    prevButton.addEventListener('click', () => moveTo(currentIndex - 1));

    function moveTo(index) {
        if (isTransitioning) return;
        isTransitioning = true;
        currentIndex = index;
        setTransition(true);
        setPositionByIndex();
    }

    // --- 4. "MÁGICA" DO LOOP INFINITO ---
    track.addEventListener('transitionend', () => {
        isTransitioning = false;
        if (currentIndex <= itemsToClone - 1) {
            setTransition(false);
            currentIndex += cardCount;
            setPositionByIndex();
        }
        if (currentIndex >= cardCount + itemsToClone) {
            setTransition(false);
            currentIndex -= cardCount;
            setPositionByIndex();
        }
    });
    
    // --- 5. LÓGICA DE ARRASTAR (DRAG & SWIPE) ---
    track.addEventListener('mousedown', dragStart);
    track.addEventListener('touchstart', dragStart, { passive: true });

    track.addEventListener('mousemove', drag);
    track.addEventListener('touchmove', drag, { passive: true });

    track.addEventListener('mouseup', dragEnd);
    track.addEventListener('mouseleave', dragEnd);
    track.addEventListener('touchend', dragEnd);

    function dragStart(event) {
        if (isTransitioning) return;
        isDragging = true;
        startPos = getPositionX(event);
        animationID = requestAnimationFrame(animation);
        setTransition(false);
    }

    function drag(event) {
        if (isDragging) {
            const currentPosition = getPositionX(event);
            currentTranslate = prevTranslate + currentPosition - startPos;
        }
    }

    function dragEnd(event) {
        if (!isDragging) return;
        isDragging = false;
        cancelAnimationFrame(animationID);

        const movedBy = currentTranslate - prevTranslate;

        // Se moveu mais de 50px, passa para o próximo slide
        if (movedBy < -50 && currentIndex < cardCount + itemsToClone) moveTo(currentIndex + 1);
        else if (movedBy > 50 && currentIndex > 0) moveTo(currentIndex - 1);
        else moveTo(currentIndex); // Volta para a posição original
    }
    
    function getPositionX(event) {
        return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX;
    }
    
    function animation() {
        track.style.transform = `translateX(${currentTranslate}px)`;
        if (isDragging) requestAnimationFrame(animation);
    }
    
    // Recalcula a posição ao redimensionar a janela
    window.addEventListener('resize', () => {
        setTransition(false);
        setPositionByIndex();
    });
});