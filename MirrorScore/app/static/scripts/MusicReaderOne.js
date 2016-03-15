$( document ).ready(function() {
	draw();
var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
var analyser = audioCtx.createAnalyser();

analyser.fftSize = 256;
var bufferLength = analyser.frequencyBinCount;
console.log(bufferLength);
var dataArray = new Uint8Array(bufferLength);

function draw() {
  analyser.getByteFrequencyData(dataArray);

  for(var i = 0; i < bufferLength; i++) {
    document.write(dataArray[i]);
  }
};
});