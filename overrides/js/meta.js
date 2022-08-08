if (location.pathname.toLowerCase().includes('configuration')) {
  //const options = { behavior: "smooth", block: "start", inline: "nearest" };
  const yOffset = -75;

  /* anchors */
  for (const anchorElement of document.getElementsByClassName('headerlink')) {
    anchorElement.addEventListener('click', (event) => {
      event.preventDefault();
      const anchor = anchorElement.getAttribute('href');

      window.history.pushState(null, '', anchor);
      const y = anchorElement.parentElement.getBoundingClientRect().top + window.pageYOffset + yOffset;
      window.scrollTo({top: y, behavior: 'smooth'});
      //anchorElement.parentElement.scrollIntoView(options);
    });
  }

  /* side bar */
  for (const anchorElement of document.getElementsByClassName('md-nav__link')) {
    anchorElement.addEventListener('click', (event) => {
      event.preventDefault();
      const anchor = anchorElement.getAttribute('href');

      const headerElement = document.getElementById(anchorElement.innerText);

      window.history.pushState(null, '', anchor);
      const y = headerElement.getBoundingClientRect().top + window.pageYOffset + yOffset;
      window.scrollTo({top: y, behavior: 'smooth'});
      //headerElement.scrollIntoView(options);
    });
  }
}
