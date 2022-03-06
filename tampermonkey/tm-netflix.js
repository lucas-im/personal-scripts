// ==UserScript==
// @name         netflix
// @namespace    https://netflix.com/*
// @version      0.1
// @description  netflix helper
// @author       me
// @match        https://www.netflix.com/*
// @icon         https://www.google.com/s2/favicons?domain=netflix.com
// @grant        none
// @run-at       document-end
// @require      http://code.jquery.com/jquery-3.4.1.min.js
// ==/UserScript==



if ($('.profile-gate-label')[0] !== null) {
    $('.profile-icon')[0].click()

}

const observer = new MutationObserver((_) => {
})
const config = {
    childList: true,
    subtree: true
}
observer.observe(document, config)