document.addEventListener('DOMContentLoaded', function () {
    const accordionButtons = document.querySelectorAll('.accordion-button');

    accordionButtons.forEach(function (accordionButton) {
        accordionButton.addEventListener('click', function () {
            const accordionPanel = document.getElementById(this.getAttribute('data-name'));

            // Toggle 'active' class on the panel
            accordionPanel.classList.toggle('active');

            // Close other panels with the same name
            const otherPanels = document.querySelectorAll(`.accordion-panel[id="${this.getAttribute('data-name')}"]`);
            otherPanels.forEach(function (panel) {
                if (panel !== accordionPanel && panel.classList.contains('active')) {
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