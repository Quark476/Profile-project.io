// Данные товаров
const products = [
    {
        id: 1,
        name: "Boost to plat",
        price: 25,
        image: "https://i.pinimg.com/originals/28/4e/5f/284e5fac5426484f9732d8050e7a50f8.gif"
    },
    {
        id: 2,
        name: "Boost to diamond",
        price: 50,
        image: "https://i.pinimg.com/originals/ef/cd/ad/efcdadd68bd27777062d90f2a8ac8ef3.gif"
    }, 
];

let cart = [];

function init() {
    const cartItems = document.getElementById('cart-items');
    const totalElement = document.getElementById('total');
    const productsContainer = document.getElementById('products');
    const checkoutBtn = document.getElementById('checkout-btn');

    function renderProducts() {
        productsContainer.innerHTML = '';
        products.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';
            productCard.innerHTML = `
                <img src="${product.image}" alt="${product.name}" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">${product.name}</h3>
                    <div class="product-price">${product.price.toLocaleString()} $</div>
                    <div class="btn-group">
                        <button class="btn btn-buy" data-id="${product.id}">В корзину</button>
                        <button class="btn btn-details">Подробнее</button>
                    </div>
                </div>
            `;
            productsContainer.appendChild(productCard);
        });
        document.querySelectorAll('.btn-buy').forEach(button => {
            button.addEventListener('click', function() {
                const productId = parseInt(this.getAttribute('data-id'));
                addToCart(productId);
            });
        });
    }

    function addToCart(productId) {
        const product = products.find(p => p.id === productId);
        const button = document.querySelector(`.btn-buy[data-id="${productId}"]`);
        
        button.textContent = '✓ Добавлено';
        button.style.background = 'linear-gradient(to right, #4facfe, #00f2fe)';
        setTimeout(() => {
            button.textContent = 'В корзину';
            button.style.background = 'linear-gradient(to right,rgb(255, 255, 255),rgb(255, 255, 255))';
        }, 1500);
        
        const existingItem = cart.find(item => item.id === productId);
        if (existingItem) {
            existingItem.quantity++;
        } else {
            cart.push({...product, quantity: 1});
        }
        
        updateCart();
    }

    function updateCart() {
        if (cart.length > 0) {
            cartItems.innerHTML = '';
        } else {
            cartItems.innerHTML = '<div class="empty-cart">Корзина пуста</div>';
            totalElement.textContent = '0';
            return;
        }
        
        let total = 0;
        cart.forEach(item => {
            const itemTotal = item.price * item.quantity;
            total += itemTotal;
            
            const cartItem = document.createElement('div');
            cartItem.className = 'cart-item';
            cartItem.innerHTML = `
                <div>
                    <strong>${item.name}</strong>
                    <div>${item.quantity} × ${item.price.toLocaleString()} $</div>
                </div>
                <div>
                    <strong>${itemTotal.toLocaleString()} $</strong>
                </div>
            `;
            cartItems.appendChild(cartItem);
        });
        
        totalElement.textContent = total.toLocaleString();
    }

    function checkout() {
        if (cart.length === 0) {
            alert('Корзина пуста! Добавьте товары перед оформлением.');
            return;
        }
        
        const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        alert(`Заказ оформлен!\nТоваров: ${cart.length}\nСумма: ${total.toLocaleString()} ₽`);
        cart = [];
        updateCart();
    }

    checkoutBtn.addEventListener('click', checkout);
    renderProducts();
    updateCart();
}

document.addEventListener('DOMContentLoaded', init);