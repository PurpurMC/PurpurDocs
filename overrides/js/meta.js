const meta = [
    [{attribute: 'property', value: 'og:type'}, {attribute: 'content', value: 'website'}],
    [{attribute: 'property', value: 'og:title'}, {attribute: 'content', value: 'Purpur Documentation'}],
    [{attribute: 'property', value: 'og:description'}, {attribute: 'content', value: 'The official documentation for Purpur. Purpur is a fork of Paper and Tuinity with the goal of providing new and interesting configuration options, which allow for creating a unique gameplay experience not seen anywhere else.'}],
    [{attribute: 'property', value: 'og:url'}, {attribute: 'content', value: '{{ page.canonical_url }}'}],
    [{attribute: 'name', value: 'twitter:site'}, {attribute: 'content', value: 'granny'}],
    [{attribute: 'name', value: 'twitter:creator'}, {attribute: 'content', value: 'granny'}],
    [{attribute: 'name', value: 'twitter:title'}, {attribute: 'content', value: 'Purpur Documentation'}],
    [{attribute: 'name', value: 'twitter:description'}, {attribute: 'content', value: 'This wiki was last updated to Build [#945](https://ci.pl3x.net/job/Purpur/945/) ([dd65bd1](https://github.com/pl3xgaming/Purpur/commit/dd65bd110910340703368db9ea3fea5887a2309a))'}],
];

const metaElements = [];

meta.forEach(tag => {
    const element = document.createElement('meta');
    tag.forEach(val => {
        element.setAttribute(val.attribute, val.value);
    });
    return metaElements.push(element);
});

document.head.append(...metaElements);
console.log(metaElements);


/* if (location.pathname.includes('Configuration')) {
    const title = [document.head.querySelector("[property~=og\\:title][content]"), document.querySelector('meta[name="twitter:title"]')];
    console.log(title);
} */