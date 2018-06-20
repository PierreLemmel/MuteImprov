"use strict";

const MuteImprov = (function() {

	let timeout = null;
	const clearTimeoutIfNeeded = function() {
		if (timeout !== null) {
			clearTimeout(timeout);
		}
	};

	const setTextImmediate = function(text) {
		clearTimeoutIfNeeded();

		const paragraphs = text.split('\n');
		const div = $('div.frame-text')
		div.empty();

		paragraphs.forEach(function(paragraph) {
			const pElt = $('<p></p>');
			pElt.text(paragraph);
			div.append(pElt);
		});
	};

	const setTextTimed = async function(text, minDelay, maxDelay) {
		clearTimeoutIfNeeded();

		if (maxDelay == null) {
			maxDelay = minDelay;
		}

		if (maxDelay < minDelay) {
			const tmp = minDelay;
			minDelay = maxDelay;
			maxDelay = tmp;
		}

		const paragraphs = text.split('\n');

		const divElt = $('div.frame-text');
		divElt.empty();

		const scrollBox = $('div.frame-text-scrollbox');

		let charIndex = 0;
		let paragraphIndex = 0;
		let currentParagraphElt = null;

		console.log(paragraphs);
		const timeoutFunction = function() {
			console.log(charIndex);
			if (paragraphIndex < paragraphs.length) {

				const paragraph = paragraphs[paragraphIndex];
				console.log(paragraph);
				if (charIndex < paragraph.length) {

					if (charIndex == 0) {
						console.log('new element!');
						currentParagraphElt = $('<p></p>');
						divElt.append(currentParagraphElt);
					}

					currentParagraphElt.append(paragraph[charIndex]);

					charIndex++;
				}
				else {
					paragraphIndex++;
					charIndex = 0;
				}

				const nextDelay = minDelay + Math.random() * (maxDelay - minDelay);
				timeout = setTimeout(timeoutFunction, nextDelay);

				scrollBox.scrollTop(scrollBox[0].scrollHeight);
			}
		};

		timeoutFunction();
	}

	return {
		setTextImmediate: setTextImmediate,
		setTextTimed: setTextTimed
	};

})();