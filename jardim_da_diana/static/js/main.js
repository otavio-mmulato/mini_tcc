document.addEventListener('DOMContentLoaded', () => {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    function updateCart(productId, quantity) {
        const url = '/sacola/update/';
        const formData = new FormData();
        formData.append('product_id', productId);
        formData.append('quantity', quantity);

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'X-Requested-With': 'XMLHttpRequest',
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'ok') {
                // Converte o texto recebido para número antes de formatar
                const itemSubtotal = parseFloat(data.item_subtotal);
                const cartTotalPrice = parseFloat(data.cart_total_price);

                const productRow = document.querySelector(`tr[data-product-id="${productId}"]`);
                if (productRow) {
                    const subtotalElement = productRow.querySelector('.item-subtotal');
                    if (subtotalElement) {
                        subtotalElement.textContent = `R$ ${itemSubtotal.toFixed(2).replace('.', ',')}`;
                    }
                }
                const summarySubtotal = document.getElementById('summary-subtotal');
                const summaryTotal = document.getElementById('summary-total');
                if (summarySubtotal) {
                    summarySubtotal.textContent = `R$ ${cartTotalPrice.toFixed(2).replace('.', ',')}`;
                }
                if (summaryTotal) {
                    summaryTotal.textContent = `R$ ${cartTotalPrice.toFixed(2).replace('.', ',')}`;
                }
                const cartCountElement = document.getElementById('cart-total-items');
                if (cartCountElement) {
                    cartCountElement.textContent = data.cart_total_items;
                }
            }
        })
        .catch(error => console.error('Erro ao atualizar o carrinho:', error));
    }

    function debounce(func, delay = 350) {
        let timeout;
        return (...args) => {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                func.apply(this, args);
            }, delay);
        };
    }
    const debouncedUpdateCart = debounce(updateCart);

    document.querySelectorAll('.quantity-selector').forEach(selector => {
        const minusBtn = selector.querySelector('.minus');
        const plusBtn = selector.querySelector('.plus');
        const input = selector.querySelector('.quantity-input');
        
        if (!minusBtn || !plusBtn || !input) return;
        
        const productId = plusBtn.dataset.productId;

        minusBtn.addEventListener('click', () => {
            let currentValue = parseInt(input.value);
            if (currentValue > 1) {
                input.value = currentValue - 1;
                if (productId) {
                    debouncedUpdateCart(productId, input.value);
                }
            }
        });
        plusBtn.addEventListener('click', () => {
            let currentValue = parseInt(input.value);
            if (currentValue < 99) {
                input.value = currentValue + 1;
                if (productId) {
                    debouncedUpdateCart(productId, input.value);
                }
            }
        });
    });
});