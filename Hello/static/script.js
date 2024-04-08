const sideMenu = document.querySelector ("aside");
const menuBtn = document.querySelector ("#menu-btn");
const closeBtn = document.querySelector ("#close-btn");
const themeToggler=document.querySelector(".theme-Toggler")
menuBtn.addEventListener('click', () => {
sideMenu.style.display = 'block';
})
closeBtn.addEventListener('click', () => {
sideMenu.style.display = 'none';
})
themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');
    themeToggler.querySelector('span')
    .classList.toggle ('active');
    themeToggler.querySelector('span')
    .classList.toggle('active');
})



Orders.slice(0,5).forEach(order =>{
    const tr= document.createElement('tr');
    const trContent =`<td>${order.productName}</td><td>${order.productNumber}</td><td>${order.paymentStatus}</td><td class="${order.shipping==='Declined' ? 'danger':order.shipping==='pending' ? 'warning':'primary'}">${order.shipping}</td><td class="primary">Details</td>`;
    const trsliced=trContent.slice(0, 5);
    tr.innerHTML=trContent;
    const top5 = Orders.slice(0, 5);
    

    document.querySelector('table tbody').appendChild(tr)
});
Orders.forEach(order =>{
    const tr= document.createElement('tr');
    const trContent =`<td>${order.productName}</td><td>${order.productNumber}</td><td>${order.paymentStatus}</td><td class="${order.shipping==='Declined' ? 'danger':order.shipping==='pending' ? 'warning':'primary'}">${order.shipping}</td><td class="primary">Details</td>`;
    const trsliced=trContent.slice(0, 5);
    tr.innerHTML=trContent;
    const top5 = Orders.slice(0, 5);
    

    document.querySelector('#table1 #tbody1').appendChild(tr)
})
// Assuming you have an HTML element representing the customer's page
const customerPageElement = document.getElementById('customer');

// Add a click event listener to the element
customerPageElement.addEventListener('click', function() {
  // Perform the AJAX request or update the content using SPA techniques
  fetch('another-page.html')
    .then(response => response.text())
    .then(html => {
      // Update a specific element on the current page with the content from another-page.html
      document.getElementById('target-element').innerHTML = html;
    })
    .catch(error => {
      console.log('An error occurred: ', error);
    });
});

