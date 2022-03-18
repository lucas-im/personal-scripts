// ==UserScript==
// @name         mql5
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.mql5.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=mql5.com
// @require      http://code.jquery.com/jquery-3.4.1.min.js
// @run-at       document-end
// @grant        none
// ==/UserScript==

const observer = new MutationObserver((_) => {
    if ($('.notify-icon_jobs') !== null) {
        $('#cover')[0].style.background = 'red'
    }
})
const config = {
    childList: true,
    subtree: true
}
observer.observe(document, config)