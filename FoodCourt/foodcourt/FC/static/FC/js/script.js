document.addEventListener('DOMContentLoaded', () => {
    const orderForm = document.getElementById('orderForm');
    const submitBtn = document.getElementById('submitBtn');
    
    submitBtn.addEventListener('click', (event) => {
        const menuItem = document.querySelector('select[name="menu_item"]').value;
        if (menuItem === '') {
            event.preventDefault();
            alert('Please select an item from the list.');
        }
    });
});
