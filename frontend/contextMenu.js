// contextMenu.js
// Create a context menu item
chrome.contextMenus.create({
  id: "aiActorContextMenuId",
  title: "Scan Page For Job Description And Generate Cover Letter",
  contexts: ["all"]
});

function copyToClipboard(text) { 
  let textarea = document.createElement("textarea");
  textarea.value = text;
 
  textarea.style.position = "fixed";
  textarea.style.left = "-9999px";
 
  document.body.appendChild(textarea); 
  textarea.select();

  try {
    // Execute the copy command
    document.execCommand("copy"); 
  } catch (err) {
    console.error("Unable to copy content", err);
  }

  // Remove the textarea from the document
  document.body.removeChild(textarea);
}

 // Fetch the entire page's HTML
function getDom() {
  return document.documentElement.outerHTML;
} 

chrome.contextMenus.onClicked.addListener(function (info, tab) {
  console.log(tab);
  if (info.menuItemId === "aiActorContextMenuId") {
    setTimeout(async () => {
      const result = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: getDom,
      });

      if (chrome.runtime.lastError) {
        console.log(chrome.runtime.lastError);
        return;
      }
      console.log(result[0])
      const res = await fetch("http://127.0.0.1:5000/read_page", {
        method: "POST",
        mode: "no-cors",
        body: JSON.stringify(result[0].result),
      });

      const currentCoverLetter = await res.text();
      console.log("----------------------------------------------------");
      console.log(typeof currentCoverLetter);
      chrome.scripting.executeScript({
        target: { tabId: tab.id, allFrames: true },
        args: [currentCoverLetter],
        func: copyToClipboard,
      }); 
    }, 2000);
  }
});
