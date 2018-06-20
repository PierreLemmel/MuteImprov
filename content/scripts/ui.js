// @TODO: handle runtime modifications
// @TODO: validate data
MuteImprov.UISettings = (function() {

	let _showVideoInBackground = true;
	let _animateFrameContainer = true;

	let _animationMinDelay = 100;
	let _animationMaxDelay = 180;
	let _smallAnimationMaxDeltaX = 0.18;
	let _smallAnimationMaxDeltaY = 0.18;
	let _bigAnimationMaxDeltaX = 1.0;
	let _bigAnimationMaxDeltaY = 1.0;
	let _animationProbability = 0.05;

	let settings = {};
	Object.defineProperty(settings, 'animationMinDelay', {
		get() { return _animationMinDelay; },
		set(value) { _animationMinDelay = value; }
	});

	Object.defineProperty(settings, 'animationMaxDelay', {
		get() { return _animationMaxDelay; },
		set(value) { _animationMaxDelay = value; }
	});

	Object.defineProperty(settings, 'bigAnimationMaxDeltaX', {
		get() { return _bigAnimationMaxDeltaX; },
		set(value) { _bigAnimationMaxDeltaX = value; }
	});

	Object.defineProperty(settings, 'bigAnimationMaxDeltaY', {
		get() { return _bigAnimationMaxDeltaY; },
		set(value) { _bigAnimationMaxDeltaY = value; }
	});

	Object.defineProperty(settings, 'smallAnimationMaxDeltaX', {
		get() { return _smallAnimationMaxDeltaX; },
		set(value) { _smallAnimationMaxDeltaX = value; }
	});

	Object.defineProperty(settings, 'smallAnimationMaxDeltaY', {
		get() { return _smallAnimationMaxDeltaY; },
		set(value) { _smallAnimationMaxDeltaY = value; }
	});

	Object.defineProperty(settings, 'animationProbability', {
		get() { return _animationProbability; },
		set(value) { _animationProbability = value; }
	});

	Object.defineProperty(settings, 'animateFrameContainer', {
		get() { return _animateFrameContainer; },
		set(value) { _animateFrameContainer = value; }
	});

	Object.defineProperty(settings, 'showVideoInBackground', {
		get() { return _showVideoInBackground; },
		set(value) { _showVideoInBackground = value; }
	});

	return settings;
})();


$(function() {
	const settings = MuteImprov.UISettings;


	if (settings.showVideoInBackground !== true) {
		$('div.fullscreen-video-background').hide();
	}

	let transform = {
		translateX: 0,
		translateY: 0
	};

	const frameContainer = $('div.frame-container');
	const animateContainer = function() {

		if (settings.animateFrameContainer !== true) {
			return;
		}

		let r = Math.random();
		const delay = r * settings.animationMinDelay + (1 - r) * settings.animationMaxDelay;

		let target;
		

		let maxDeltaX, maxDeltaY;

		r = Math.random();
		if (r <= settings.animationProbability) {
			maxDeltaX = settings.bigAnimationMaxDeltaX;
			maxDeltaY = settings.bigAnimationMaxDeltaY;
		}
		else {
			maxDeltaX = settings.smallAnimationMaxDeltaX;
			maxDeltaY = settings.smallAnimationMaxDeltaY;
		}

		r = Math.random();
		const targetX = (2.0 * r - 1.0) * maxDeltaX;

		r = Math.random();
		const targetY = (2.0 * r - 1.0) * maxDeltaY;

		target = {
			translateX: targetX,
			translateY: targetY
		}

		$(transform).animate(target, {
			duration: delay,
			step: function(val) {
				const transformStr = 'translate(' + transform.translateX + '%, ' + transform.translateY + '%)';
				frameContainer.css('transform', transformStr);
			},
			complete: animateContainer
		});
	};

	animateContainer();
})