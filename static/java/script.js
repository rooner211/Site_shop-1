$(document).ready(function() {
    $('.btn-minus').click(function() {
        var id = $(this).data('id');
        updateCart(id, 'remove');
    });

    $('.btn-plus').click(function() {
        var id = $(this).data('id');
        updateCart(id, 'add');
    });

    $('.btn-clear').click(function() {
        updateCart(null, 'clear');
    });

    function updateCart(id, action) {
        $.ajax({
            type: 'POST',
            url: '/update_cart',
            contentType: 'application/json',
            data: JSON.stringify({'id': id, 'action': action}),
            success: function(response) {
                $('.cart-items').empty();
                response.cart.forEach(function(item) {
                    var itemHtml = `
                        <li class="cart-item">
                            <span class="item-name">${item.name}</span>
                            <span class="item-price">$${item.price}</span>
                            <div class="quantity">
                                <button class="btn-minus" data-id="${item.id}">-</button>
                                <span class="item-quantity">${item.quantity}</span>
                                <button class="btn-plus" data-id="${item.id}">+</button>
                            </div>
                        </li>
                    `;
                    $('.cart-items').append(itemHtml);
                });
                $('.total-price').text('$' + response.total_price);
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    }
});
