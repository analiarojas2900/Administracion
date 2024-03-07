document.addEventListener('DOMContentLoaded', function () {
    const accordionItems = document.querySelectorAll('.accordion-item');
  
    accordionItems.forEach(function (item) {
      const button = item.querySelector('.accordion-button');
      const panel = item.querySelector('.accordion-panel');
  
      button.addEventListener('click', function () {
        if (button.getAttribute('aria-expanded') === 'true') {
          button.setAttribute('aria-expanded', 'false');
          panel.style.display = 'none';
        } else {
          button.setAttribute('aria-expanded', 'true');
          panel.style.display = 'block';
        }
      });
    });
  });



  