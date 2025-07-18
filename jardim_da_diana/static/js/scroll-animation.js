// Espera o conteúdo da página carregar completamente
document.addEventListener('DOMContentLoaded', () => {

    // Seleciona todos os cards de depoimento que queremos animar
    const cards = document.querySelectorAll('.testimonial-card');

    const observerOptions = {
        root: null, // observa a viewport inteira
        rootMargin: '0px',
        threshold: 0.1 // 10% de visibilidade
    };

    // Cria o observador
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            // Verifica se o elemento está entrando na tela
            if (entry.isIntersecting) {
                // Adiciona a classe 'is-visible' para ativar a animação do CSS
                entry.target.classList.add('is-visible');
                
                // (Importante) Para a observação deste elemento depois que a animação ocorreu,
                // para que ela não se repita ao rolar para cima e para baixo.
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Inicia a observação para cada um dos cards
    cards.forEach(card => {
        observer.observe(card);
    });
});