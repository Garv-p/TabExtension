'use strict';
chrome.tabs.onCreated.addListener((tab) => {
    console.log(`Tab created: ${tab.id}`);
  });
  
  chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete') {
      console.log(`Tab updated: ${tabId}`);
    }
  });
  
  chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.create({ url: 'https://www.google.com' });
  });
