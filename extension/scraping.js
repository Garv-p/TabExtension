
function scrape() {
  var url = window.location.href;

  var title = document.title;
  var body = document.body.innerHTML;
  var data = {
    url: url,
    title: title,
    body: body
  };
  chrome.runtime.sendMessage(data);
}
scrape();