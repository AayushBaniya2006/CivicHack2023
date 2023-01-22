/*!
* Start Bootstrap - Agency v7.0.11 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 
const drugPrices = document.querySelector("[data-drug-prices]")

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'dd5fb89b79msh6373beaf106d4b5p1f8fbcjsn6a74372dc4e9',
		'X-RapidAPI-Host': 'drug-info-and-price-history.p.rapidapi.com'
	}
};

fetch('https://drug-info-and-price-history.p.rapidapi.com/1/druginfo?drug=advil', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));


const drugprices = document.querySelector("[data-drug-price]")
fetch("https://api.fda.gov/drug/event.json?search=patient.drug.openfda.brand_name:Aspirin&limit=1")
.then(res => res.json())
.then(data => {
    data.forEach(user => {
        const card = drugprices.content.cloneNode(true).children[0]
        console.log(card)

    })
});


window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === -1) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});