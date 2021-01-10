const metaTags = [
    [{attribute: 'property', value: 'og:type'}, {attribute: 'content', value: 'website'}],
    [{attribute: 'property', value: 'og:title'}, {attribute: 'content', value: 'Purpur Documentation'}],
    [{attribute: 'property', value: 'og:description'}, {attribute: 'content', value: 'The official documentation for Purpur. Purpur is a fork of Paper and Tuinity with the goal of providing new and interesting configuration options, which allow for creating a unique gameplay experience not seen anywhere else.'}],
    [{attribute: 'property', value: 'og:url'}, {attribute: 'content', value: location.href}],
    [{attribute: 'property', value: 'og:image'}, {attribute: 'content', value: 'https://pl3xgaming.github.io/PurpurDocs/images/purpur-small.png'}],
];

document.onreadystatechange = function(){
    if (document.readyState == 'interactive'){
        if (location.pathname.includes('Configuration') && location.hash) {
            const configName = location.hash.slice(1);
            const descElement = document.getElementById(configName);

            if (descElement && descElement.nextElementSibling) {
                // meta[title][content].value
                metaTags[1][1].value = configName;
                
                // meta[description][content].value
                metaTags[2][1].value = descElement.nextElementSibling.innerText;
            }
        }
        
        const metaElements = [];
        
        metaTags.forEach(tag => {
            const element = document.createElement('meta');
            tag.forEach(val => {
                element.setAttribute(val.attribute, val.value);
            });
            return metaElements.push(element);
        });
        
        document.head.append(...metaElements);
    }
};