var textAreaElem = document.getElementById("id_1-violation_summary");
var displayCountElem = document.getElementById("display_count");
var countMessageElem = document.getElementById("count_message");
var wordLimitAlert = document.getElementById("word-limit-alert");
var wordCountArea = document.getElementById("word_count_area");

// Show word count area for JS-enabled browsers:
wordCountArea.removeAttribute('hidden');

function updateWordCount (e) {
    // Ignore `e` and read the value directly from the textarea here;
    // we want this function to work even if the user hasn't typed
    // anything (e.g. if textarea has initial content).
    var value = textAreaElem.value;
    var words = value ? value.match(/\S+/g).length : 0;

    displayCountElem.innerHTML = (500 - words);

    if (words >= 500) {
      // Word count greater than or equal to 500 word limit.
      // Trim the text down to the first 500 words:
      var trimmed = textAreaElem.value.split(" ", 500).join(" ")
                                      .split("\t", 500).join("\t")
                                      .split("\n", 500).join("\n");
      textAreaElem.value = trimmed;

      // Update display for user:
      displayCountElem.innerHTML = '0';
      textAreaElem.classList.add('bg-gold-outline');
      wordLimitAlert.removeAttribute('hidden');
    } else {
      displayCountElem.innerHTML = (500 - words);
      textAreaElem.classList.remove('bg-gold-outline');
      wordLimitAlert.setAttribute('hidden', '');
    }
};

if (textAreaElem) {
  // Fire `updateWordCount()` on page load because textarea may have
  // some initial content; for example if the user fills in the textarea,
  // presses "Next" and then uses the back button to navigate back.
  updateWordCount();

  document.addEventListener('keyup', updateWordCount);
};