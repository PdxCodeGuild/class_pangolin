let app = new Vue({
    el: "#app",
    data: {
        product: "Boots",
        description: "These are for rain.",
        image: './assets/vmSocks-green-onWhite.jpg',
        link: './assets/vmSocks-green-onWhite.jpg',
        inventory: 0,
        onSale: 0,
        details: ["80% cotton", "20% polyester", "Gender-neutral"],
        variants: [
            {
                variantId: 2234,
                variantColor: "green"
            },
            {
                variantId: 2235,
                variantColor: "blue"
            },
        ],
        sizes: ['S', 'M', 'L', 'XL'],
        
    }
});