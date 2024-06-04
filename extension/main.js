'use strict';
document.addEventListener('DOMContentLoaded', () => {
    const createTabButton = document.getElementById('createTab');
    
        createTabButton.addEventListener('click', () => {
            chrome.tabs.create({ url: 'https://garv-p.github.io' });
        });
});
'use strict';
document.addEventListener('DOMContentLoaded', () => {
    const createTabButton = document.getElementById('scrapeButton');
    
    createTabButton.addEventListener('click', () => {
        chrome.tabs.query({  currentWindow: true }, (tabs) => {
        for(let i =0; i < tabs.length; i++){
            let activeTab = tabs[i];
            chrome.scripting.executeScript({
                target: { tabId: activeTab.id },
                files: ['scraping.js']
            });
        }
        });
    });
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log(message);
  });