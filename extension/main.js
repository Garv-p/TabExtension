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

async function processData(){
    const url = "http://127.0.0.1:8000/process";
    const response = await fetch(url);
    return response.json();
}

async function sendData(data){
    const url = "http://127.0.0.1:8000/store";
    const response = await fetch( url ,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
    
};

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    sendData(message).then((response) => {
        console.log(response);
    });
  });