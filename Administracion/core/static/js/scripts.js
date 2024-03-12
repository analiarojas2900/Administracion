document.addEventListener('DOMContentLoaded', function () {
    const accordionButtons = document.querySelectorAll('.accordion-button');

    accordionButtons.forEach(function (accordionButton) {
        accordionButton.addEventListener('click', function () {
            const targetPanelClass = this.getAttribute('data-target');
            const accordionPanel = document.querySelector('.accordion-panel.' + targetPanelClass);

            // Toggle 'active' class on the panel
            accordionPanel.classList.toggle('active');

            // Close other panels
            const otherPanels = document.querySelectorAll('.accordion-panel:not(.' + targetPanelClass + ')');
            otherPanels.forEach(function (panel) {
                if (panel.classList.contains('active')) {
                    panel.classList.remove('active');
                    const button = panel.previousElementSibling;
                    button.classList.remove('active');
                }
            });

            // Toggle 'active' class on the button
            this.classList.toggle('active');
        });
    });
});

