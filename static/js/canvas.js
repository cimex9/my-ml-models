var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

var painting = document.getElementById('canvas-app');
var paint_style = getComputedStyle(painting);
canvas.width = parseInt(paint_style.getPropertyValue('width'));
canvas.height = parseInt(paint_style.getPropertyValue('height'));

var mouse = {x: 0, y: 0};

canvas.addEventListener('mousemove', function(e) {
  mouse.x = e.pageX - this.offsetLeft;
  mouse.y = e.pageY - this.offsetTop;
}, false);

ctx.lineWidth = 20;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.strokeStyle = '#fff';

canvas.addEventListener('mousedown', function(e) {
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);

    canvas.addEventListener('mousemove', onPaint, false);
}, false);

canvas.addEventListener('mouseup', function() {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function() {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};

function clearCanvas() {
    ctx.clearRect(0, 0, 1000, 1000);
}

function updateImgPath() {
    let imgPath = document.querySelector(".model-form > input:nth-child(2)");
    imgPath.value = canvas.toDataURL("image/jpeg");
}
