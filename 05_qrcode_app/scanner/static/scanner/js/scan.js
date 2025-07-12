const qrInput = document.getElementById('qr-input');

qrInput.addEventListener('change', function(event) {
	const file = event.target.files[0];
	// console.log(file)
	
	if(file) {
		const reader = new FileReader();
		reader.onload = function(e) {
			const img = document.createElement('img');
			img.src = e.target.result;
			img.alt = 'QR Code preview';
			img.style.maxWidth = '200px';
			img.style.border = '1px solid #ddd';
			img.style.borderRadius = '8px';
			img.style.padding = '5px';

			const previewContainer = document.querySelector('.qr-preview');
			console.log(previewContainer)
			if(previewContainer.querySelector('img')) {
				previewContainer.querySelector('img').remove();
			}
			previewContainer.prepend(img);
		};
		reader.readAsDataURL(file)
	}
});