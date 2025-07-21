document.addEventListener('DOMContentLoaded', () => {
    // Lógica para todos os seletores de quantidade da página
    const quantitySelectors = document.querySelectorAll('.quantity-selector');

    quantitySelectors.forEach(selector => {
        const minusBtn = selector.querySelector('.minus');
        const plusBtn = selector.querySelector('.plus');
        const input = selector.querySelector('.quantity-input');

        minusBtn.addEventListener('click', () => {
            let currentValue = parseInt(input.value);
            if (currentValue > 1) {
                input.value = currentValue - 1;
            }
        });

        plusBtn.addEventListener('click', () => {
            let currentValue = parseInt(input.value);
            if (currentValue < 99) { // Limite máximo
                input.value = currentValue + 1;
            }
        });
    });
});