
'use strict';
document.addEventListener('DOMContentLoaded', () => {
    const createTabButton = document.getElementById('createTab');
    
        createTabButton.addEventListener('click', () => {
            chrome.tabs.create({ url: 'https://garv-p.github.io' });
        });

    const scrapeButton = document.getElementById('scrapeButton');

    scrapeButton.addEventListener('click', () => {
        chrome.tabs.query({  currentWindow: true }, (tabs) => {
        for(let i =0; i < tabs.length; i++){
            let activeTab = tabs[i];
            let data =  chrome.scripting.executeScript({
                target: { tabId: activeTab.id },
                files: ['scraping.js'],

            });
            data.tabID = activeTab.id;
            chrome.runtime.sendMessage(data);
        }
        processData();
        
        cleanData();
        });
    });
});

function addToTabGroup(tabId, groupId) {
    chrome.tabs.group({
        groupId: groupId,
        tabIds: tabId
    });
}

async function processData(){
    const url = "http://127.0.0.1:8000/process";
    const response = await fetch(url);

    response.json().then((data) => {    
        console.log("processing: ");
        console.log(data);
        console.log("data type: ", typeof(data));
        Object.keys(data).forEach((key) => {
            const tabIds = data[key];
            console.log(tabIds)
            createTabGroupWithExistingTabs(tabIds);
    });

});
    
}
function cleanData(){
    const url = "http://127.0.0.1:8000/delete";
    const response = fetch(url);
    return response.json();
}
function createTabGroupWithExistingTabs(tabIds) {
    chrome.tabs.group({
        tabIds: tabIds
    }, (groupId) => {
        console.log(`Created new group with ID: ${groupId}`);
    });
}
function sendData(data, id){
    data.tabID = id;
    const url = "http://127.0.0.1:8000/store";
    const response = fetch( url ,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
    
};

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    sendData(message, sender.tab.id).then((response) => {
        console.log(response);
    });
  });