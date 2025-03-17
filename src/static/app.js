const codes=document.querySelectorAll('pre');
codes.forEach((element)=>{
    var copyButton = document.createElement("span");
    copyButton.innerText = 'Copy';
    copyButton.classList.add("copy-button");
    element.appendChild(copyButton);
    copyButton.addEventListener("click", () => {
        // Hide the copy button temporarily
        copyButton.style.display = "none";

        // Create a range and select the text inside the <pre> tag
        const range = document.createRange();
        range.selectNode(element);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);

        try {
            // Copy the selected text to the clipboard
            document.execCommand("copy");

            // Alert the user that the text has been copied
            copyButton.innerText = "Copied!";
            setTimeout(function(){
                copyButton.innerText = "Copy";
            }, 2000);
        } catch (err) {
            console.error("Unable to copy text:", err);
        } finally {
            // Show the copy button again
            copyButton.style.display = "inline";

            // Deselect the text
            window.getSelection().removeAllRanges();
        }
    });
});
